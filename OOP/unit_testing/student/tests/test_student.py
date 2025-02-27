from unittest import TestCase,main

from unit_testing.student.project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student('testGuy1')
        self.student_with_course = Student('testGuy2', {"Math": ["some note"]})


    def test_correct_initialization(self):
        self.assertEqual('testGuy1', self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({"Math": ["some note"]}, self.student_with_course.courses)

    def test_add_note_to_existing_course(self):
       result = self.student_with_course.enroll("Math", ['second note'])

       self.assertEqual("second note", self.student_with_course.courses["Math"][1])
       self.assertEqual("Course already added. Notes have been updated.", result)

    def test_add_note(self):
        result = self.student.enroll("Bio", ["bio note"])

        self.assertEqual("bio note", self.student.courses["Bio"][0])
        self.assertEqual("Course and course notes have been added.", result)

    def test_add_not_with_y_parameter(self):
        result = self.student.enroll("Bio", ["bio note"], "Y")

        self.assertEqual("bio note", self.student.courses["Bio"][0])
        self.assertEqual("Course and course notes have been added.", result)

    def test_add_notes_on_existing_course(self):
        result = self.student_with_course.add_notes("Math", "hello")
        self.assertEqual("hello", self.student_with_course.courses["Math"][-1]) ## - 1 last element
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_to_non_existing_course_raise_exceptiion(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("math", "some note")

        self.assertEqual("Cannot add notes. Course not found.",str(ex.exception))

    def test_leave_existing_course(self):
        result = self.student_with_course.leave_course("Math")
        self.assertEqual({},self.student_with_course.courses)
        self.assertEqual("Course has been removed",result)

    def test_leave_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Math")
            self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

if __name__ == "__main__":
    main()