from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

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
