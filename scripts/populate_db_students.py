import os, django, random, sys
from faker import Faker
from validate_docbr import CPF

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from apps.school.models import Student

def create_students(people_number):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(people_number):
        name = fake.name()
        email = '{}@{}'.format(name.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = CPF()
        cpf = cpf.generate()
        birth_date = fake.date_of_birth(minimum_age=18, maximum_age=30)
        phone_number = "{} 9{}-{}".format(random.randrange(10, 89), random.randrange(4000, 9999), random.randrange(4000, 9999))

        student = Student(name=name, email=email, cpf=cpf, birth_date=birth_date, phone_number=phone_number)
        student.save()

create_students(50)