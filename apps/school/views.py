from apps.school.models import Student, Course, Enrollment
from apps.school.serializers import \
    StudentSerializer,CourseSerializer, EnrollmentSerializer, StudentEnrollmentsListSerializer, CourseEnrollmentsListSerializer
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser

class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class StudentEnrollmentsListViewSet(generics.ListAPIView):
    serializer_class = StudentEnrollmentsListSerializer

    def get_queryset(self):
        return Enrollment.objects.filter(student_id = self.kwargs['pk'])

class CourseEnrollmentsListViewSet(generics.ListAPIView):
    serializer_class = CourseEnrollmentsListSerializer

    def get_queryset(self):
        return Enrollment.objects.filter(course_id = self.kwargs['pk'])
