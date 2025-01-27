from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json

from apps.school.models import Course
from apps.school.serializers import CourseSerializer

class CoursesRouteTestCase(APITestCase):
    fixtures = ['db_prototype.json']

    def setUp(self):
        self.user = User.objects.get(username='jay')
        self.url = reverse('Courses-list')
        self.client.force_authenticate(user=self.user)
        # {"pk": 1, "code": "MAT012", "description": "matematica calculo diferencial I", "level": "B"},
        self.course_01 = Course.objects.get(pk=1)
        # {"pk": 2, "code": "CPOO1", "description": "Curso de Python Orientação à Objetos 01", "level": "A"},
        self.course_02 = Course.objects.get(pk=2)

    def test_get_request_to_list_courses(self):
        """Test to make a GET request for listing courses"""
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_course_data = CourseSerializer([self.course_01, self.course_02], many=True).data
        for expected, response in zip(expected_course_data, response.data['results']):
            self.assertEqual(expected, response)

    def test_get_request_to_get_course_by_id(self):
        """Test to make a GET request for retrieving a existent course by id"""
        response = self.client.get(path=f"{self.url}1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_course_data = CourseSerializer(instance=self.course_01).data
        self.assertEqual(response.data, expected_course_data)

    def test_post_request_to_create_course(self):
        """Test to make a POST request in order to persist a new course"""
        course_data = json.dumps({
            'code': 'MAT201',
            'description': 'Applied Mathematics Calculum 2',
            'level': 'I',
        }, indent=4)
        response = self.client.post(path=self.url, data=course_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_request_to_update_course(self):
        """Test to make a PUT request in order to update course"""
        course_data = json.dumps({
            'id': 1,
            'code': 'MAT222',
            'description': 'Applied Mathematics Calculum 2.0',
            'level': 'A',
        }, indent=4)
        response = self.client.put(path=f"{self.url}1/", data=course_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_course = Course.objects.get(id=1)
        self.assertEqual(updated_course.code, 'MAT222')

    def test_delete_request_to_destroy_course(self):
        """Test to make a DELETE request in order to destroy a course from database"""
        response = self.client.delete(path=f"{self.url}1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(path=f"{self.url}1/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)