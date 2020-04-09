"""to create a data repository of courses, students, and instructors"""

import os
from HW08_Akhil_Manchikanti import file_reader
from typing import Dict, DefaultDict, List, Tuple, Iterator
from collections import defaultdict
from prettytable import PrettyTable

class Major:
    """ Stores information about each major and if it is required or elective and the course name itself"""
    
    pt_hdr: Tuple[str, str, str] = ("Major", "Required Courses", "Electives")
    
    def __init__(self, major: str) -> None:
        self._major: str = major
        self._required: List = list()
        self._elective: List = list()
    
    def add_course(self, rORe: str, course: str) -> None:
        """ Add course to the required or elective list based on the attribute from the file """
        
        if rORe == "R":
            self._required.append(course)
        elif rORe == "E":
            self._elective.append(course)
        else:
            print("Error in specifying Required/Elective course")

    def info(self) -> List:
        """ list of information to be printed in pretty table """
        return [self._major, sorted(self._required), sorted(self._elective)]

class Student:
    """ Stores information about a single student with all of the relevant information including:
        cwid, name, major, Container of courses and grades"""

    pt_hdr: Tuple[str, str, str, str, str, str, str] = ("CWID", "Name", "Major", "Completed Courses", "Remaining Required", "Remaining Electives", "GPA")
    grades_to_gpa: Dict[str, float] = {'A': 4.0, 'A-': 3.75, 'B+': 3.25, 'B': 3.0, 'B-':2.75, 'C+': 2.25, 'C': 2.0, 'C-': 0, 'D+': 0, 'D': 0, 'D-': 0, 'F': 0}

    def __init__(self, cwid: str, name: str, major: str, required: List[str], electives: List[str]) -> None:
        self._cwid: str = cwid
        self._name: str = name
        self._major: str = major
        self._courses: Dict[str, str] = dict() #key: courses value: str with grade
        self._remaining_required: List[str] = required
        self._remaining_electives: List[str] = electives
    
    def course_grade(self, course: str, grade: str) -> None:
        """ store the students grade for each course """
        
        if Student.grades_to_gpa[grade] > 0:
            self._courses[course] = grade
            if course in self._remaining_required:
                self._remaining_required.remove(course)
            elif course in self._remaining_electives:
                self._remaining_electives = list()

    def claculate_gpa(self) -> float:
        """ Function to caluclate the students GPA """
        scores: List = [Student.grades_to_gpa[course_gpa] for course_gpa in self._courses.values()]
        if len(scores) > 0:
            return round(sum(scores)/len(scores),2)
        return 0

    def info(self) -> List:
        """ list of the information returned to be printed in pretty table"""
        return [self._cwid, self._name, self._major, sorted(self._courses.keys()), sorted(self._remaining_required), sorted(self._remaining_electives), self.claculate_gpa()]
        

class Instructor:
    """ Stores information about a single Instructor with all of the relevant information including:
        cwid, name, department, Container of courses taught and the number of students in each course"""
    
    pt_hdr: List[str] = ["CWID", "Name", "Dept", "Course", "Students"]
    
    def __init__(self, cwid: str, name: str, department: str) -> None:
        self._cwid: str = cwid
        self._name: str = name
        self._department: str = department
        self._courses: DefaultDict[str, int] = defaultdict(int) #key: course value: number of students
    
    def course_student(self, course_name: str) -> None:
        """ Stores the count of courses taught by the instructor """
        self._courses[course_name] += 1

    def info(self) -> Iterator[Tuple]:
        """ information returned to be printed in pretty table """
        # all_subjects_instructor: List[List] = list()

        # for offset, (course, no_students) in enumerate(self.courses.items()):
        #     all_subjects_instructor[offset] = [self.cwid, self.name, self.department, course, no_students]
        
        # return all_subjects_instructor

        for course, no_students in self._courses.items():
            yield (self._cwid, self._name, self._department, course, no_students)


class Repository:
    """ holds all of the data of students, instructors data and print pretty tables """

    def __init__(self, dir_path, ptables: bool=True) -> None:
        self._dir_path: str = dir_path #dictionary with the students, instructors and grades file
        self._students: Dict[str, Student] = dict() #key: cwid value:instance of class Student
        self._instructors: Dict[str, Instructor] = dict() #key: cwid value: instance of class Instructor
        self._majors: Dict[str, Major] = dict() #key: major value: instance of class Major
        # self._majors[Major] = Major()

        try:
            self._majors_data()
            self._student_data()
            self._instructor_data()
            self._grades_data()
            
            # self.student_pretty_table()
            # self.instructor_pretty_table()
        except ValueError as ve:
            print(ve)
        except FileNotFoundError as fnfe:
            print(fnfe)

        if ptables:
            print("\nMajor Summary")
            self.major_pretty_table()

            print("\nStudent summary")
            self.student_pretty_table()

            print("\nInstructor Summary")
            self.instructor_pretty_table()

    def _majors_data(self) -> None:
        """ Reads the majors and requried courses for each major """
        try:
            for major, flag, course in file_reader(os.path.join(self._dir_path, "majors.txt"), 3, "\t", True):
                if major in self._majors:
                    self._majors[major].add_course(flag, course)
                else:
                    self._majors[major] = Major(major)
                    self._majors[major].add_course(flag, course)
        except (FileNotFoundError, ValueError) as e:
            print(e)

    def _student_data(self) -> None:
        """ creates instances of students and updates it in the container"""
        try:
            for cwid, name, major in file_reader(os.path.join(self._dir_path, "students.txt"), 3, ";", True):
                if cwid in self._students:
                    print(f"{cwid} is duplicate")
                else:
                    self._students[cwid] = Student(cwid, name, major, self._majors[major]._required, self._majors[major]._elective)
        except (FileNotFoundError, ValueError) as e:
            print(e)
    
    def _instructor_data(self) -> None:
        """ creates instances of instructors and updates it in the container """
        try:
            for cwid, name, department in file_reader(os.path.join(self._dir_path, "instructors.txt"), 3, "|", True):
                if cwid in self._instructors:
                    print(f"{cwid} is duplicate")
                else:
                    self._instructors[cwid] = Instructor(cwid, name, department)
        except (FileNotFoundError, ValueError) as e:
            print(e)
    
    def _grades_data(self) -> None:
        """ Reads the grades file and updates the student and instructor instances accordingly """
        try:
            for cwid, course, grade, instructor_cwid in file_reader(os.path.join(self._dir_path, "grades.txt"), 4, "|", True):
                if cwid in self._students:
                    s: Student = self._students[cwid]
                    s.course_grade(course, grade)
                else:
                    print(f"Student with id: {cwid} doesn't exist in the student repository")
                
                if instructor_cwid in self._instructors:
                    inst: Instructor = self._instructors[instructor_cwid]
                    inst.course_student(course)
                else:
                    print(f"Instructor with id: {cwid} doesn't exist in the instructor repository")

        except (FileNotFoundError, ValueError) as e:
            print(e)
    
    def student_pretty_table(self) -> None:
        """ print student info pretty table """
        pt: PrettyTable = PrettyTable(field_names=Student.pt_hdr)
        for stud in self._students.values():
            pt.add_row(stud.info())
        # print("Student Summary")
        print(pt)

    def instructor_pretty_table(self) -> None:
        """ print student info pretty table """
        pt: PrettyTable = PrettyTable(field_names=Instructor.pt_hdr)
        for inst in self._instructors.values():
            for each_instructor in inst.info():
                pt.add_row(each_instructor)
        # print("Instructor Summary")
        print(pt)

    def major_pretty_table(self) -> None:
        """ print major info pretty table """
        pt: PrettyTable = PrettyTable(field_names=Major.pt_hdr)
        for maj in self._majors.values():
            pt.add_row(maj.info())
        print(pt)

def main():
    try:
        stevens: Repository = Repository('D:\MS\Stevens Institute of Technology\SSW810\Assignment10\Stevens') # read files and generate prettytables
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()