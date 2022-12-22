from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    def course_count(self, obj):
        return obj.plan_set.all().count()

    course_count.short_description = 'number of courses'
    list_display = ('title', 'course_count')
    list_per_page = 10
    ordering = ('title',)
    search_fields = ('title', 'course_count')


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    def get_tags(self, obj):
        return "\n".join([t.title for t in obj.tags.all()])

    def get_capacity(self, obj):
        return obj.limit - obj.member_set.all().count()

    get_tags.short_description = 'tags'
    get_capacity.short_description = 'capacity'
    list_display = (
        'title', 'get_tags', 'description', 'created_at', 'updated_at', 'starts_at', 'limit', 'get_capacity')
    list_per_page = 10
    ordering = ('-created_at',)
    search_fields = (
        'title', 'get_tags', 'description', 'created_at', 'updated_at', 'starts_at', 'limit', 'get_capacity')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    def get_creator(self, obj):
        return obj.plan.mentor

    get_creator.short_description = 'creator'
    list_display = ('title', 'description', 'created_at', 'updated_at', 'deadline', 'plan', 'get_creator')
    list_per_page = 10
    ordering = ('-created_at',)
    search_fields = ('title', 'description', 'created_at', 'updated_at', 'deadline', 'plan', 'get_creator')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'birth_date', 'join_date', 'user')
    list_per_page = 10
    ordering = ('user',)
    search_fields = ('first_name', 'last_name', 'phone', 'birth_date', 'join_date', 'user')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('plan', 'profile')
    list_per_page = 10
    ordering = ('plan', 'profile')
    search_fields = ('plan', 'profile')


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('plan', 'profile')
    list_per_page = 10
    ordering = ('plan', 'profile')
    search_fields = ('plan', 'profile')
