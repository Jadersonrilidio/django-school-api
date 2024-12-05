import os, django, random, sys

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from apps.school.models import Course

data = [
    ('CPOO1', 'Curso de Python Orientação à Objetos 01'),
    ('CPOO2', 'Curso de Python Orientação à Objetos 02'),
    ('CPOO3', 'Curso de Python Orientação à Objetos 03'),
    ('CDJ01', 'Curso de Django 01'),
    ('CDJ02', 'Curso de Django 02'),
    ('CDJ03', 'Curso de Django 03'),
    ('CDJ04', 'Curso de Django 04'),
    ('CDJ05', 'Curso de Django 05'),
    ('CDJRF01', 'Curso de Django REST Framework 01'),
    ('CDJRF02', 'Curso de Django REST Framework 02'),
    ('CDJRF03', 'Curso de Django REST Framework 03'),
    ('CDJRF04', 'Curso de Django REST Framework 04')
]

levels = ['B', 'I', 'A']

def create_courses():
    for code, description in data:
        level = random.choice(levels)
        Course.objects.create(code=code, description=description, level=level)

create_courses()