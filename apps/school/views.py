from rest_framework import viewsets, generics, filters, throttling
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from apps.school.models import Student, Course, Enrollment
from apps.school.serializers import *
from apps.school.throtllers import EnrollmentAnonRateThrottle

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name', 'email', 'birth_date']
    search_fields = ['name', 'email', 'cpf']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        return StudentSerializer
    
    @action(detail=True, methods=['get'])
    def enrollments_list(self, request, pk=None):
        student = Student.objects.get(id=pk)
        enrollments = Enrollment.objects.filter(student_id = student.id).order_by('id')
        enrollments_list = StudentEnrollmentsListSerializer(enrollments, many=True)
        return Response(data=enrollments_list.data)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'code']
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def enrollments_list(self, request, pk=None):
        course = Course.objects.get(id=pk)
        enrollments = Enrollment.objects.filter(course_id = course.id).order_by('id')
        enrollments_list = CourseEnrollmentsListSerializer(enrollments, many=True)
        return Response(data=enrollments_list.data, status=status.HTTP_200_OK)

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
