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
        students = self.__hidrate_students(response)
        self.assertEqual(students[0].id, self.student_1.id)
        self.assertEqual(students[1].id, self.student_2.id)

    def test_get_request_to_get_student_by_id(self):
        """Test to make a GET request for retrieving a existent student by id"""
        response = self.client.get(path=f"{self.url}1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # student_data = Student.objects.get(id=self.student_1.id)
        serialized_student_data = StudentSerializer(instance=self.student_1).data
        self.assertEqual(response.data, serialized_student_data)

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

    # Helper private methods

    def __hidrate_student(self, student_dict) -> Student:
        """Hidrate Student instance from a student_dict format"""
        return Student(
            id=student_dict['id'],
            name=student_dict['name'],
            email=student_dict['email'],
            cpf=student_dict['cpf'],
            birth_date=student_dict['birth_date'],
            phone_number=student_dict['phone_number'],
        )

    def __hidrate_students(self, response) -> list[Student]:
        """Hidrate Student instances from raw dict data retrieved from an HTTP response.json() method"""
        students = []
        for student_dict in response.json()['results']:
            students.append(self.__hidrate_student(student_dict))
        return students