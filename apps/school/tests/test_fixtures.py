from django.test import TestCase

from apps.school.models import Student, Course, Enrollment

class FixturesTestCase(TestCase):
    fixtures = ["db_prototype.json"]

    def test_loading_fixtures(self):
        """Test verifies if database fixtures have being correctly loaded"""
        # Student { "pk": 20, "name": "Vitor Gabriel Fonseca", "email": "vitorgabrielfonseca@hotmail.com", "cpf": "91194014429", "birth_date": "1998-01-01", "phone_number": "43 94538-8809" }
        # Course {"pk": 1, "code": "MAT012", "description": "matematica calculo diferencial I", "level": "B" }
        student = Student.objects.get(cpf="91194014429")
        course = Course.objects.get(pk=1)
        enrollment = Enrollment.objects.get(pk=1)
        self.assertEqual(student.name, "Vitor Gabriel Fonseca")
        self.assertEqual(course.code, "MAT012")
        self.assertEqual(enrollment.period, "M")