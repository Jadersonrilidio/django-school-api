from apps.school.models import Student, Course, Enrollment
from apps.school.serializers import \
    StudentSerializer,CourseSerializer, EnrollmentSerializer, StudentEnrollmentsListSerializer, \
    CourseEnrollmentsListSerializer, StudentSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name', 'email', 'birth_date']
    search_fields = ['name', 'email', 'cpf']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        return StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'code']

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id']

class StudentEnrollmentsListViewSet(generics.ListAPIView):
    serializer_class = StudentEnrollmentsListSerializer

    def get_queryset(self):
        return Enrollment.objects.filter(student_id = self.kwargs['pk'])

class CourseEnrollmentsListViewSet(generics.ListAPIView):
    serializer_class = CourseEnrollmentsListSerializer

    def get_queryset(self):
        return Enrollment.objects.filter(course_id = self.kwargs['pk'])
