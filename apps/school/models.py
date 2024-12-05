from django.db import models
from django.core import validators


class Student(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(blank = False, max_length = 128)
    cpf = models.CharField(max_length = 11, unique = True)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length = 14)

    def __str__(self):
        return self.name


class Course(models.Model):
    LEVEL_OPTIONS = (
        ('B', 'Basic'),
        ('I', 'Intermediate'),
        ('A', 'Advanced')
    )

    code = models.CharField(max_length = 10, unique = True, validators = [validators.MinLengthValidator(3)])
    description = models.TextField(blank = False, max_length = 256)
    level = models.CharField(blank = False, null = False, choices = LEVEL_OPTIONS, default = 'B', max_length = 1)

    def __str__(self):
        return self.code

class Enrollment(models.Model):
    PERIOD_OPTIONS = (
        ('M', 'Morming'),
        ('A', 'Afternoon'),
        ('N', 'Night'),
    )

    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    period = models.CharField(blank = False, null = False, choices = PERIOD_OPTIONS, default = 'M', max_length = 1)