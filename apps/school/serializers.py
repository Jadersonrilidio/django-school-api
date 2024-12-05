from rest_framework import serializers
from apps.school.models import Student, Course, Enrollment
from apps.school.validators import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, attrs):
        if invalid_name(attrs['name']):
            raise serializers.ValidationError({'name': 'only alphanumirec characters are allowed for name field'})
        if invalid_cpf(attrs['cpf']):
            raise serializers.ValidationError({'cpf': 'invalid cpf value'})
        if invalid_phone_number(attrs['phone_number']):
            raise serializers.ValidationError({'phone_number': 'wrong phone number format (Ex: XX XXXXX-XXXX)'})
        return attrs

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class StudentEnrollmentsListSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source = 'course.description')
    period = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = ['course', 'period']

    def get_period(self, obj):
        return obj.get_period_display()

class CourseEnrollmentsListSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source = 'student.name')

    class Meta:
        model = Enrollment
        fields = ['student_name']

class StudentSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'phone_number']