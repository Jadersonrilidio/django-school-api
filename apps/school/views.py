from apps.school.models import Student, Course, Enrollment
from apps.school.serializers import *
from apps.school.throtllers import EnrollmentAnonRateThrottle
from rest_framework import viewsets, generics, filters, throttling
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name', 'email', 'birth_date']
    search_fields = ['name', 'email', 'cpf']
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        return StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'code']
    permission_classes = [IsAuthenticatedOrReadOnly]

class EnrollmentViewSet(viewsets.ModelViewSet):
    throttle_classes = [throttling.UserRateThrottle, EnrollmentAnonRateThrottle]
    queryset = Enrollment.objects.all().order_by('id')
    serializer_class = EnrollmentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id']
    http_method_names = ['get', 'post']

class StudentEnrollmentsListViewSet(generics.ListAPIView):
    """
    View description:
    - List of Enrollments per Student id
    args:
    - id (int): Student id. Should be an integer number
    """
    serializer_class = StudentEnrollmentsListSerializer
    def get_queryset(self):
        return Enrollment.objects.filter(student_id = self.kwargs['id']).order_by('id')

class CourseEnrollmentsListViewSet(generics.ListAPIView):
    """
    View description:
    - List of Enrollments per Course id
    args:
    - id (int): Course id. Should be an integer number
    """
    serializer_class = CourseEnrollmentsListSerializer
    def get_queryset(self):
        return Enrollment.objects.filter(course_id = self.kwargs['id']).order_by('id')
