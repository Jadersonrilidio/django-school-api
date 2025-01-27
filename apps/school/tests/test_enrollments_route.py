from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json

from apps.school.models import Student, Course, Enrollment
from apps.school.serializers import EnrollmentSerializer

class EnrollmentsRouteTestCase(APITestCase):
    fixtures = ['db_prototype.json']

    def setUp(self):
        self.user = User.objects.get(username='jay')
        self.url = reverse('Enrollments-list')
        self.client.force_authenticate(user=self.user)
        # {"pk": 1, "name": "Mario", "email": "mario@armario.com", "cpf": "11122233344", "birth_date": "2024-11-26", "phone_number": "31999876543"},
        self.student = Student.objects.get(pk=1)
        # {"pk": 1, "code": "MAT012", "description": "matematica calculo diferencial I", "level": "B"},
        self.course = Course.objects.get(pk=1)
        # {"pk": 1, "student": 1, "course": 1, "period": "M"}
        self.enrollment = Enrollment.objects.get(pk=1)

    def test_get_request_to_list_enrollments(self):
        """Test to make a GET request for listing enrollments"""
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for expected, response in zip([EnrollmentSerializer(instance=self.enrollment).data], response.data['results']):
            self.assertEqual(expected, response)

    def test_get_request_to_get_enrollment_by_id(self):
        """Test to make a GET request for retrieving a existent enrollment by id"""
        response = self.client.get(path=f"{self.url}1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_enrollment_data = EnrollmentSerializer(instance=self.enrollment).data
        self.assertEqual(response.data, expected_enrollment_data)

    def test_post_request_to_create_enrollment(self):
        """Test to make a POST request in order to persist a new enrollment"""
        enrollment_data = json.dumps({
            'student': self.student.id,
            'course': self.course.id,
            'period': 'M',
        }, indent=4)
        response = self.client.post(path=self.url, data=enrollment_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_request_to_update_course(self):
        """Test to make a PUT request in order to update course"""
        enrollment_data = json.dumps({
            'id': 1,
            'student': 3,
            'course': self.course.id,
            'period': 'M',
        }, indent=4)
        response = self.client.put(path=f"{self.url}1/", data=enrollment_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_request_to_destroy_enrollment(self):
        """Test to make a DELETE request in order to destroy a enrollment from database"""
        response = self.client.delete(path=f"{self.url}1/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)