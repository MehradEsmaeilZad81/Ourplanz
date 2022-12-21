from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    def course_count(self, obj):
        return obj.course_set.all().count()

    course_count.short_description = 'number of courses'
    list_display = ('title', 'number of courses')
    list_per_page = 10
    ordering = ('title',)
    search_fields = ('title', 'number of courses')


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    def get_tags(self, obj):
        return "\n".join([t.title for t in obj.tags.all()])

    def get_capacity(self, obj):
        return obj.limit - obj.member_set.all().count()

    get_tags.short_description = 'tags'
    get_capacity.short_description = 'capacity'
    list_display = ('title', 'tags', 'description', 'created_at', 'updated_at', 'limit', 'capacity')
    list_per_page = 10
    ordering = ('-created_at',)
    search_fields = ('title', 'tags', 'description', 'created_at', 'updated_at', 'limit', 'capacity')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    def get_plan(self, obj):
        return obj.plan.title

    get_plan.short_description = 'plan_title'
    list_display = ('title', 'description', 'created_at', 'updated_at', 'deadline', 'plan', 'plan_title')
    list_per_page = 10
    ordering = ('-created_at',)
    search_fields = ('title', 'description', 'created_at', 'updated_at', 'deadline', 'plan', 'plan_title')


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    def get_plan(self, obj):
        return obj.plan.title

    get_plan.short_description = 'plan_title'
    list_display = ('first_name', 'last_name', 'phone', 'birth_date', 'join_date', 'user', 'plan', 'plan_title')
    list_per_page = 10
    ordering = ('user',)
    search_fields = ('first_name', 'last_name', 'phone', 'birth_date', 'join_date', 'user', 'plan', 'plan_title')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    def get_plan(self, obj):
        return obj.plan.title

    get_plan.short_description = 'plan_title'
    list_display = ('first_name', 'last_name', 'phone', 'birth_date', 'join_date', 'user', 'plan', 'plan_title')
    list_per_page = 10
    ordering = ('user',)
    search_fields = ('first_name', 'last_name', 'phone', 'birth_date', 'join_date', 'user', 'plan', 'plan_title')
