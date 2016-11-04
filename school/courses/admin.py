from django.contrib import admin
from .models import Subject, Course, Module

@admin.register(Subject)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['creator', 'subject', 'created']
    list_filter = ['subject', 'created']
    search_fields = ['title', 'overview', 'creator']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        ModuleInline,
    ]

# Register your models here.
