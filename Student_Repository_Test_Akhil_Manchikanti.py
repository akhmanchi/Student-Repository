import unittest
from Student_Repository_Akhil_Manchikanti import Student, Instructor, Repository

class TestRepository(unittest.TestCase):
    """ Tests all the methods in HW09_Akhil_Manchikanti """

    def test_Major(self) -> None:
        """ Tests the Major repository """
        data: Repository = Repository("D:\MS\Stevens Institute of Technology\SSW810\Assignment10\Stevens")
        major_data = {major: maj.info() for major, maj in data._majors.items()}
        expected = {
            'SFEN': ['SFEN', ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'] ,['CS 501', 'CS 513', 'CS 545']],
            'SYEN': ['SYEN', ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']]}
        self.assertEqual(expected, major_data)

    def test_Student(self) -> None:
        """ Tests the student repository """
        data: Repository = Repository("D:\MS\Stevens Institute of Technology\SSW810\Assignment10\Stevens")
        student_data = {cwid: stud.info() for cwid, stud in data._students.items()}
        expected = {'10103': ['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [], 3.44],
                    '10115': ['10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [], 3.81], 
                    '10172': ['10172', 'Forbes, I', 'SFEN', ['SSW 555', 'SSW 567'], ['SSW 540', 'SSW 564'], ['CS 501', 'CS 513', 'CS 545'], 3.88], 
                    '10175': ['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 513', 'CS 545'], 3.58], 
                    '10183': ['10183', 'Chapman, O', 'SFEN', ['SSW 689'], ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'],['CS 501', 'CS 513', 'CS 545'], 4.0], 
                    '11399': ['11399', 'Cordova, I', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [], 3.0], 
                    '11461': ['11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800'], ['SYS 612', 'SYS 671'], ['SSW 540', 'SSW 565', 'SSW 810'], 3.92],
                    '11658': ['11658', 'Kelly, P', 'SYEN', [], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'], 0], 
                    '11714': ['11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645'], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'], 3.0], 
                    '11788': ['11788', 'Fuller, E', 'SYEN', ['SSW 540'],['SYS 612', 'SYS 671', 'SYS 800'], [], 4.0] }
        self.assertEqual(student_data, expected)

    def test_Instructor(self) -> None:
        """ Tests the instructor repository """
        data: Repository = Repository("D:\MS\Stevens Institute of Technology\SSW810\Assignment10\Stevens")
        instructor_data = {tuple(each_instructor) for inst in data._instructors.values() for each_instructor in inst.info()}
        expected = {('98765', 'Einstein, A', 'SFEN', 'SSW 567', 4),
                    ('98764', 'Feynman, R', 'SFEN', 'SSW 564', 3),
                    ('98765', 'Einstein, A', 'SFEN', 'SSW 540', 3),
                    ('98764', 'Feynman, R', 'SFEN', 'SSW 687', 3),
                    ('98764', 'Feynman, R', 'SFEN', 'CS 501', 1),
                    ('98764', 'Feynman, R', 'SFEN', 'CS 545', 1),
                    ('98763', 'Newton, I', 'SFEN', 'SSW 555', 1),
                    ('98763', 'Newton, I', 'SFEN', 'SSW 689', 1),
                    ('98760', 'Darwin, C', 'SYEN', 'SYS 800', 1),
                    ('98760', 'Darwin, C', 'SYEN', 'SYS 750', 1),
                    ('98760', 'Darwin, C', 'SYEN', 'SYS 611', 2),
                    ('98760', 'Darwin, C', 'SYEN', 'SYS 645', 1)}
        self.assertEqual(instructor_data, expected)

    # def test_Major(self) -> None:
    #     """ Tests the Major repository """
    #     data: Repository = Repository("D:\MS\Stevens Institute of Technology\SSW810\Assignment10\Stevens")
    #     major_data = {major: maj.info() for major, maj in data._majors.items()}
    #     expected = {
    #         'SFEN': ['SFEN', ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'] ,['CS 501', 'CS 513', 'CS 545']],
    #         'SYEN': ['SYEN', ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']]}
    #     self.assertEqual(expected, major_data)

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)