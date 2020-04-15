import unittest
from Student_Repository_Akhil_Manchikanti import Student, Instructor, Repository

class TestRepository(unittest.TestCase):
    """ Tests all the methods in Student_Repository_Akhil_Manchikanti """

    def test_Major(self) -> None:
        """ Tests the Major repository """
        data: Repository = Repository("D:\MS\Stevens Institute of Technology\SSW810\Assignment11\data")
        major_data = {major: maj.info() for major, maj in data._majors.items()}
        expected = {
            'SFEN': ['SFEN', ['SSW 540', 'SSW 555', 'SSW 810'] ,['CS 501', 'CS 546']],
            'CS': ['CS', ['CS 546', 'CS 570'], ['SSW 565', 'SSW 810']]}
        self.assertEqual(expected, major_data)

    def test_Student(self) -> None:
        """ Tests the student repository """
        data: Repository = Repository("D:\MS\Stevens Institute of Technology\SSW810\Assignment11\data")
        student_data = {cwid: stud.info() for cwid, stud in data._students.items()}
        expected = {'10103': ['10103', 'Jobs, S', 'SFEN', ['CS 501', 'SSW 810'], ['SSW 540', 'SSW 555'], [], 3.38],
                    '10115': ['10115', 'Bezos, J', 'SFEN', ['SSW 810'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 546'], 2.0],
                    '10183': ['10183', 'Musk, E', 'SFEN', ['SSW 555', 'SSW 810'], ['SSW 540'], ['CS 501', 'CS 546'], 4.0],
                    '11714': ['11714', 'Gates, B', 'CS', ['CS 546', 'CS 570', 'SSW 810'], [], [], 3.5]
                    }
        self.assertEqual(student_data, expected)

    def test_Instructor(self) -> None:
        """ Tests the instructor repository """
        data: Repository = Repository("D:\MS\Stevens Institute of Technology\SSW810\Assignment11\data")
        instructor_data = {tuple(each_instructor) for inst in data._instructors.values() for each_instructor in inst.info()}
        expected = {('98764', 'Cohen, R', 'SFEN', 'CS 546', 1),
                    ('98763', 'Rowland, J', 'SFEN', 'SSW 810', 4),
                    ('98763', 'Rowland, J', 'SFEN', 'SSW 555', 1),
                    ('98762', 'Hawking, S', 'CS', 'CS 501', 1),
                    ('98762', 'Hawking, S', 'CS', 'CS 546', 1),
                    ('98762', 'Hawking, S', 'CS', 'CS 570', 1)
                    }
        self.assertEqual(instructor_data, expected)

    def test_Student_Grade_Summary(self) -> None:
        """ Tests the student grade summary from the db """
        data: Repository = Repository("D:\MS\Stevens Institute of Technology\SSW810\Assignment11\data")
        student_grade_summary_data = data.student_grades_table_db("D:\MS\Stevens Institute of Technology\SSW810\Assignment11\data\HW11.sql")
        expected = [
            ('Bezos, J', '10115', 'SSW 810', 'A', 'Rowland, J'),
            ('Bezos, J', '10115', 'CS 546', 'F', 'Hawking, S'),
            ('Gates, B', '11714', 'SSW 810', 'B-', 'Rowland, J'),
            ('Gates, B', '11714', 'CS 546', 'A', 'Cohen, R'),
            ('Gates, B', '11714', 'CS 570', 'A-', 'Hawking, S'),
            ('Jobs, S', '10103', 'SSW 810', 'A-', 'Rowland, J'),
            ('Jobs, S', '10103', 'CS 501', 'B', 'Hawking, S'),
            ('Musk, E', '10183', 'SSW 555', 'A', 'Rowland, J'),
            ('Musk, E', '10183', 'SSW 810', 'A', 'Rowland, J') ]
        # self.assertEqual(expected, student_grade_summary_data)
        self.assertEqual(student_grade_summary_data[0][1], '10115')
        self.assertEqual(student_grade_summary_data[2][1], '11714')
        self.assertEqual(student_grade_summary_data[5][1], '10103')
        self.assertEqual(student_grade_summary_data[8][1], '10183')

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)