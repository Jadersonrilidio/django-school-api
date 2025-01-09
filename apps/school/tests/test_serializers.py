from django.test import TestCase

from apps.school.models import Student, Course, Enrollment
from apps.school.serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer, \
        StudentSerializerV2, StudentEnrollmentsListSerializer, CourseEnrollmentsListSerializer


class StudentSerializerTestCase(TestCase):
    def setUp(self):
        self.student = Student(
            name = 'Test Model',
            email = 'testmodel@example.com',
            cpf = '20479304050',
            birth_date = '2023-02-02',
            phone_number = '31 98765-3456',
        )
        self.serialized_student = StudentSerializer(instance=self.student)

    def test_verify_student_serialized_field_keys_are_correct(self):
        """
        Test to verify if the serialized Student Model contains all expected fields
        """
        data = self.serialized_student.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'email', 'cpf', 'birth_date', 'phone_number']))

    def test_verify_student_serialized_field_values_are_correct(self):
        """
        Test to verify if the serialized Student Model fields contains the exact values
        """
        data = self.serialized_student.data
        self.assertEqual(data['id'], self.student.id)
        self.assertEqual(data['name'], self.student.name)
        self.assertEqual(data['email'], self.student.email)
        self.assertEqual(data['cpf'], self.student.cpf)
        self.assertEqual(data['birth_date'], self.student.birth_date)
        self.assertEqual(data['phone_number'], self.student.phone_number)



class CourseSerializerTestCase(TestCase):
    def setUp(self):
        self.course = Course(
            code='MAT101',
            description='Applied Math',
            level='Advanced',
        )
        self.serialized_course = CourseSerializer(instance=self.course)

    def test_verify_course_serialized_field_keys_are_correct(self):
        """
        Test to verify if the serialized Course Model contains all expected fields
        """
        data = self.serialized_course.data
        self.assertEqual(set(data.keys()), set(['id', 'code', 'description', 'level']))

    def test_verify_course_serialized_field_values_are_correct(self):
        """
        Test to verify if the serialized Course Model fields contains the exact values
        """
        data = self.serialized_course.data
        self.assertEqual(data['id'], self.course.id)
        self.assertEqual(data['code'], self.course.code)
        self.assertEqual(data['description'], self.course.description)
        self.assertEqual(data['level'], self.course.level)


class EnrollmentSerializerTestCase(TestCase):
    def setUp(self):
        self.student = Student(
            id = 101,
            name = 'Test Model',
            email = 'testmodel@example.com',
            cpf = '20479304050',
            birth_date = '2023-02-02',
            phone_number = '31 98765-3456',
        )
        self.course = Course(
            id = 101,
            code='MAT101',
            description='Applied Math',
            level='Advanced',
        )
        self.enrollment = Enrollment(
            student=self.student,
            course=self.course,
            period='Morning',
        )
        self.serialized_enrollment = EnrollmentSerializer(instance=self.enrollment)

    def test_verify_enrollment_serialized_field_keys_are_correct(self):
        """
        Test to verify if the serialized Enrollment Model contains all expected fields
        """
        data = self.serialized_enrollment.data
        self.assertEqual(set(data.keys()), set(['id', 'student', 'course', 'period']))

    def test_verify_enrollment_serialized_field_values_are_correct(self):
        """
        Test to verify if the serialized Enrollment Model fields contains the exact values
        """
        data = self.serialized_enrollment.data
        self.assertEqual(data['id'], self.enrollment.id)
        self.assertEqual(data['student'], self.enrollment.student.id)
        self.assertEqual(data['course'], self.enrollment.course.id)
        self.assertEqual(data['period'], self.enrollment.period)


# todo
class StudentSerializerV2TestCase(TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_verify_student_v2_serialized_field_keys_are_correct(self):
        """
        Test to verify if the v2 serialized Student Model contains all expected fields
        """
        pass

    def test_verify_student_v2_serialized_field_values_are_correct(self):
        """
        Test to verify if the v2 serialized Student Model fields contains the exact values
        """
        pass


# todo
class StudentEnrollmentsListSerializerTestCase(TestCase):
    def setUp(self):
        pass

    def test_verify_serialized_enrollments_list_per_student_are_retrieved_correctly(self):
        """
        Description goes here...
        """
        pass


# todo
class CourseEnrollmentsListSerializerTestCase(TestCase):
    def setUp(self):
        pass

    def test_verify_serialized_enrollments_list_per_course_are_retrieved_correctly(self):
        """
        Description goes here...
        """
        pass