from django.urls import path, include
from rest_framework import routers

from apps.school.views import StudentViewSet, CourseViewSet, \
    EnrollmentViewSet, StudentEnrollmentsListViewSet, CourseEnrollmentsListViewSet

router = routers.DefaultRouter()

router.register('students', StudentViewSet, basename = 'Students')
router.register('courses', CourseViewSet, basename = 'Courses')
router.register('enrollments', EnrollmentViewSet, basename = 'Enrollments')

school_urlpatterns = [
    path('', include(router.urls)),
    path('students/<int:id>/enrollments', StudentEnrollmentsListViewSet.as_view()),
    path('courses/<int:id>/enrollments', CourseEnrollmentsListViewSet.as_view()),
]
