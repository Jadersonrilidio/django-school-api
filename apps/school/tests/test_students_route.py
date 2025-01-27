from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json

from apps.school.models import Student
from apps.school.serializers import StudentSerializer

class StudentsRouteTestCase(APITestCase):
    fixtures = ['db_prototype.json']

    def setUp(self):
        self.user = User.objects.get(username='jay')
        self.url = reverse('Students-list')
        self.client.force_authenticate(self.user)
        # {"pk": 1, "name": "Mario", "email": "mario@armario.com", "cpf": "11122233344", "birth_date": "2024-11-26", "phone_number": "31999876543"},
        self.student_1 = Student.objects.get(pk=1)
        # {"pk": 2, "name": "Carol", "email": "carol@armarol.com", "cpf": "12312312345", "birth_date": "2024-11-26", "phone_number": "31912341234"},
        self.student_2 = Student.objects.get(pk=2)

    def test_get_request_to_list_students(self):
        """Test to make a GET request for listing students"""
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_students_data = StudentSerializer([self.student_1, self.student_2], many=True).data
        for expected, response in zip(expected_students_data, response.data['results']):
            self.assertEqual(expected, response)

    def test_get_request_to_get_student_by_id(self):
        """Test to make a GET request for retrieving a existent student by id"""
        response = self.client.get(path=f"{self.url}1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_student_data = StudentSerializer(instance=self.student_1).data
        self.assertEqual(response.data, expected_student_data)

    def test_post_request_to_create_student(self):
        """Test to make a POST request in order to persist a new student"""
        student_data = json.dumps({
            'name': 'TestModel',
            'email': 'testmodel03@example.com',
            'cpf': '67853666071',
            'birth_date': '2023-03-03',
            'phone_number': '31 98765-3456',
        }, indent=4)
        response = self.client.post(path=self.url, data=student_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_request_to_update_student(self):
        """Test to make a PUT request in order to update student"""
        student_data = json.dumps({
            'id': 1,
            'name': 'UpdatedTestModel',
            'email': 'testmodel01@example.com',
            'cpf': '20479304050',
            'birth_date': '2021-01-01',
            'phone_number': '31 98765-1234',
        }, indent=4)
        response = self.client.put(path=f"{self.url}1/", data=student_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_student = Student.objects.get(id=1)
        self.assertEqual(updated_student.name, 'UpdatedTestModel')

    def test_delete_request_to_destroy_student(self):
        """Test to make a DELETE request in order to destroy a student from database"""
        response = self.client.delete(path=f"{self.url}1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(path=f"{self.url}1/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)