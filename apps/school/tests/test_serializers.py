from django.test import TestCase

from apps.school.models import Student, Course, Enrollment
from apps.school.serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer, \
        StudentSerializerV2, StudentEnrollmentsListSerializer, CourseEnrollmentsListSerializer


class BaseSerializerTestCase(TestCase):
    """Base TestCase class for serializer tests, load fixtures and set up shared test data"""
    fixtures = ['db_prototype.json']

    @classmethod
    def setUpTestData(cls):
        cls.student = Student.objects.get(pk=1)
        cls.course = Course.objects.get(pk=1)
        cls.enrollment = Enrollment.objects.get(pk=1)


class StudentSerializerTestCase(BaseSerializerTestCase):
    def setUp(self):
        self.serialized_student = StudentSerializer(instance=self.student)

    def test_verify_student_serialized_field_keys_are_correct(self):
        """Test to verify if the serialized Student Model contains all expected fields"""
        data = self.serialized_student.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'email', 'cpf', 'birth_date', 'phone_number']))

    def test_verify_student_serialized_field_values_are_correct(self):
        """Test to verify if the serialized Student Model fields contains the exact values"""
        data = self.serialized_student.data
        self.assertEqual(list(data.values()), [self.student.id, self.student.name, self.student.email, self.student.cpf, self.student.birth_date.isoformat(), self.student.phone_number])


class CourseSerializerTestCase(BaseSerializerTestCase):
    def setUp(self):
        self.serialized_course = CourseSerializer(instance=self.course)

    def test_verify_course_serialized_field_keys_are_correct(self):
        """Test to verify if the serialized Course Model contains all expected fields"""
        data = self.serialized_course.data
        self.assertEqual(set(data.keys()), set(['id', 'code', 'description', 'level']))

    def test_verify_course_serialized_field_values_are_correct(self):
        """Test to verify if the serialized Course Model fields contains the exact values"""
        data = self.serialized_course.data
        self.assertEqual(list(data.values()), [self.course.id, self.course.code, self.course.description, self.course.level])


class EnrollmentSerializerTestCase(BaseSerializerTestCase):
    def setUp(self):
        self.serialized_enrollment = EnrollmentSerializer(instance=self.enrollment)

    def test_verify_enrollment_serialized_field_keys_are_correct(self):
        """Test to verify if the serialized Enrollment Model contains all expected fields"""
        data = self.serialized_enrollment.data
        self.assertEqual(set(data.keys()), set(['id', 'student', 'course', 'period']))

    def test_verify_enrollment_serialized_field_values_are_correct(self):
        """Test to verify if the serialized Enrollment Model fields contains the exact values"""
        data = self.serialized_enrollment.data
        self.assertEqual(list(data.values()), [self.enrollment.id, self.enrollment.period, self.enrollment.student.id, self.enrollment.course.id])


class StudentSerializerV2TestCase(BaseSerializerTestCase):
    def setUp(self):
        self.serialized_student = StudentSerializerV2(instance=self.student)
    
    def test_verify_student_v2_serialized_field_keys_are_correct(self):
        """Test to verify if the v2 serialized Student Model contains all expected fields"""
        data = self.serialized_student.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'email', 'phone_number']))

    def test_verify_student_v2_serialized_field_values_are_correct(self):
        """Test to verify if the v2 serialized Student Model fields contains the exact values"""
        data  = self.serialized_student.data
        self.assertEqual(list(data.values()), [self.student.id, self.student.name, self.student.email, self.student.phone_number])


class StudentEnrollmentsListSerializerTestCase(BaseSerializerTestCase):
    def setUp(self):
        self.student_enrollments_list = Enrollment.objects.filter(student_id=self.student.id)
        self.serialized_student_enrollments_list = StudentEnrollmentsListSerializer(self.student_enrollments_list, many=True)

    def test_verify_serialized_students_enrollments_list_have_the_correct_lenght(self):
        """Test if the returned enrollments list have the correct number of student enrollments"""
        data = self.serialized_student_enrollments_list.data
        self.assertEqual(len(data), 1)

    def test_verify_serialized_student_enrollments_list_have_correct_keys(self):
        """Test if the returned enrollments list have the correct keys on each enrollment object"""
        data = self.serialized_student_enrollments_list.data
        for enrollment in data:
            self.assertEqual(set(enrollment.keys()), set(['course', 'period']))

    def test_verify_serialized_student_enrollments_list_have_correct_values(self):
        """Test if the returned enrollments list have the correct values on each enrollment object"""
        data = self.serialized_student_enrollments_list.data
        for data, expected in zip(data, self.student_enrollments_list):
            self.assertEqual(list(data.values()), [expected.course.description, expected.period_name()])


class CourseEnrollmentsListSerializerTestCase(BaseSerializerTestCase):
    def setUp(self):
        self.course_enrollments_list = Enrollment.objects.filter(course_id=self.course.id)
        self.serialized_course_enrollments_list = CourseEnrollmentsListSerializer(self.course_enrollments_list, many=True)

    def test_verify_serialized_course_enrollments_list_have_the_correct_lenght(self):
        """Test if the returned enrollments list have the correct number of course enrollments"""
        data = self.serialized_course_enrollments_list.data
        self.assertEqual(len(data), 2)

    def test_verify_serialized_course_enrollments_list_have_correct_keys(self):
        """Test if the returned enrollments list have the correct keys for each enrollment object"""
        data = self.serialized_course_enrollments_list.data
        for enrollment in data:
            self.assertEqual(set(enrollment.keys()), set(['student_name']))

    def test_verify_serialized_course_enrollments_list_have_correct_values(self):
        """Test if the returned enrollments list have the correct values for each enrollment object"""
        data = self.serialized_course_enrollments_list.data
        for data, expected in zip(data, self.course_enrollments_list):
            self.assertEqual(list(data.values()), [expected.student.name])