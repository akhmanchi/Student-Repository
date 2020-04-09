"""to create a data repository of courses, students, and instructors"""

import os
from HW08_Akhil_Manchikanti import file_reader
from typing import Dict, DefaultDict, List, Tuple, Iterator
from collections import defaultdict
from prettytable import PrettyTable

class Student:
    """ Stores information about a single student with all of the relevant information including:
        cwid, name, major, Container of courses and grades"""

    pt_hdr:Tuple[str, str, str] = ("CWID", "Name", "Completed Courses")
    
    def __init__(self, cwid: str, name: str, major: str) -> None:
        self._cwid: str = cwid
        self._name: str = name
        self._major: str = major
        self._courses: Dict[str, str] = dict() #key: courses value: str with grade
    
    def course_grade(self, course: str, grade: str) -> None:
        """ store the students grade for each course """
        self._courses[course] = grade

    def info(self) -> List:
        """ list of the information returned to be printed in pretty table"""
        return [self._cwid, self._name, sorted(self._courses.keys())]
        

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
        
        try:
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
            print("Student summary")
            self.student_pretty_table()

            print("\nInstructor Summary")
            self.instructor_pretty_table()
    
    def _student_data(self) -> None:
        """ creates instances of students and updates it in the container"""
        try:
            for cwid, name, major in file_reader(os.path.join(self._dir_path, "students.txt"), 3, "\t", False):
                if cwid in self._students:
                    print(f"{cwid} is duplicate")
                else:
                    self._students[cwid] = Student(cwid, name, major)
        except (FileNotFoundError, ValueError) as e:
            print(e)
    
    def _instructor_data(self) -> None:
        """ creates instances of instructors and updates it in the container """
        try:
            for cwid, name, department in file_reader(os.path.join(self._dir_path, "instructors.txt"), 3, "\t", False):
                if cwid in self._instructors:
                    print(f"{cwid} is duplicate")
                else:
                    self._instructors[cwid] = Instructor(cwid, name, department)
        except (FileNotFoundError, ValueError) as e:
            print(e)
    
    def _grades_data(self) -> None:
        """ Reads the grades file and updates the student and instructor instances accordingly """
        try:
            for cwid, course, grade, instructor_cwid in file_reader(os.path.join(self._dir_path, "grades.txt"), 4, "\t", False):
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


def main():
    try:
        stevens: Repository = Repository('D:\MS\Stevens Institute of Technology\SSW810\Assignment9\Stevens') # read files and generate prettytables
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()