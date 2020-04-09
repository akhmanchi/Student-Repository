import unittest
from HW09_Akhil_Manchikanti import Student, Instructor, Repository

class TestRepository(unittest.TestCase):
    """ Tests all the methods in HW09_Akhil_Manchikanti """
    def test_Student(self) -> None:
        """ Tests the student repository """
        data: Repository = Repository("D:\MS\Stevens Institute of Technology\SSW810\Assignment9\Stevens")
        student_data = {cwid: stud.info() for cwid, stud in data._students.items()}
        expected = {'10103': ['10103','Baldwin, C',['CS 501','SSW 564', 'SSW 567', 'SSW 687']],
                    '10115': ['10115','Wyatt, X',['CS 545','SSW 564', 'SSW 567', 'SSW 687']],
                    '10172': ['10172','Forbes, I',['SSW 555', 'SSW 567']],
                    '10175': ['10175','Erickson, D',['SSW 564', 'SSW 567', 'SSW 687']],
                    '10183': ['10183','Chapman, O',['SSW 689']],
                    '11399': ['11399','Cordova, I',['SSW 540']],
                    '11461': ['11461','Wright, U',['SYS 611','SYS 750', 'SYS 800']],
                    '11658': ['11658','Kelly, P',['SSW 540']],
                    '11714': ['11714','Morton, A',['SYS 611','SYS 645']],
                    '11788': ['11788','Fuller, E',['SSW 540']]}
        self.assertEqual(student_data, expected)

    def test_Instructor(self) -> None:
        """ Tests the instructor repository """
        data: Repository = Repository("D:\MS\Stevens Institute of Technology\SSW810\Assignment9\Stevens")
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

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)