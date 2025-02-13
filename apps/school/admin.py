from django.contrib import admin

from apps.school.models import Student, Course, Enrollment

class AdminStudents(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'cpf', 'birth_date', 'phone_number')
    list_display_links = ('id', 'name', 'email', 'cpf')
    list_per_page = 20
    search_fields = ('name', 'email', 'cpf')
    ordering = ('name', 'email', 'birth_date')

admin.site.register(Student, AdminStudents)

class AdminCourses(admin.ModelAdmin):
    list_display = ('id', 'code', 'description', 'level')
    list_display_links = ('id', 'code')
    list_per_page = 20
    search_fields = ('code',)

admin.site.register(Course, AdminCourses)

class AdminEnrollments(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'period')
    list_display_links = ('id',)
    list_per_page = 20
    search_fields = ('id', 'period')

admin.site.register(Enrollment, AdminEnrollments)