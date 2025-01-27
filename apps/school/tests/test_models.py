from django.test import TestCase

from apps.school.models import Student, Course, Enrollment

class StudentTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name = 'Test Model',
            email = 'testmodel@example.com',
            cpf = '20479304050',
            birth_date = '2023-02-02',
            phone_number = '31 98765-3456',
        )

    def test_verify_student_atrributes(self):
        """Test to verify if Student model attributes are correctly inserted"""
        self.assertEqual(self.student.name, 'Test Model')
        self.assertEqual(self.student.email, 'testmodel@example.com')
        self.assertEqual(self.student.cpf, '20479304050')
        self.assertEqual(self.student.birth_date, '2023-02-02')
        self.assertEqual(self.student.phone_number, '31 98765-3456')

class CourseTestCase(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            code='MAT101',
            description='Applied Math',
            level='Advanced',
        )

    def test_verify_course_attributes(self):
        """Test to verify if Course model attributes are correctly inserted"""
        self.assertEqual(self.course.code, 'MAT101')
        self.assertEqual(self.course.description, 'Applied Math')
        self.assertEqual(self.course.level, 'Advanced')

class EnrollmentTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name = 'Test Model',
            email = 'testmodel@example.com',
            cpf = '20479304050',
            birth_date = '2023-02-02',
            phone_number = '31 98765-3456',
        )
        self.course = Course.objects.create(
            code='MAT101',
            description='Applied Math',
            level='Advanced',
        )
        self.enrollment = Enrollment.objects.create(
            student=self.student,
            course=self.course,
            period='Morning',
        )

    def test_verify_enrollment_attributes(self):
        """Test to verify if Enrollment model attributes are correctly inserted"""
        self.assertEqual(self.enrollment.student, self.student)
        self.assertEqual(self.enrollment.course, self.course)
        self.assertEqual(self.enrollment.period, 'Morning')