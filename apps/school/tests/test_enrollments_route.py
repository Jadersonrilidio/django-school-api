from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

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
