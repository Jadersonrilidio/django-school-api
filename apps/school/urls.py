from django.urls import path, include
from apps.school.views import \
    StudentViewSet, CourseViewSet, EnrollmentViewSet, StudentEnrollmentsListViewSet, CourseEnrollmentsListViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename = 'Students')
router.register('courses', CourseViewSet, basename = 'Courses')
router.register('enrollments', EnrollmentViewSet, basename = 'Enrollments')

school_urlpatterns = [
    path('', include(router.urls)),
    path('students/<int:pk>/enrollments', StudentEnrollmentsListViewSet.as_view()),
    path('courses/<int:pk>/enrollments', CourseEnrollmentsListViewSet.as_view()),
]
