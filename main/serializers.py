from rest_framework import serializers

from .models import *


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['title', 'created_at', 'starts_at', 'mentor', 'limit', 'capacity', 'tags', 'detail_url', 'mentor_id']

    tags = serializers.SerializerMethodField(method_name='get_tags')
    capacity = serializers.SerializerMethodField(method_name='get_capacity', read_only=True)
    mentor = serializers.SerializerMethodField(method_name='mentor_name')
    mentor_id = serializers.IntegerField()
    detail_url = serializers.SerializerMethodField(method_name='get_detail_url', read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    starts_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    limit = serializers.IntegerField()

    def get_detail_url(self, plan: Plan):
        Base_url = 'http://127.0.0.1:8000'
        return "{}/app/plans/{}/".format(Base_url, plan.id)

    def get_tags(self, plan: Plan):
        tags = []
        for t in plan.tags.all():
            tags.append(t.title)
        return tags

    def get_capacity(self, plan: Plan):
        return plan.limit - plan.member_set.all().count()

    def mentor_name(self, plan: Plan):
        return plan.mentor.first_name + ' ' + plan.mentor.last_name


class PlanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['title', 'description', 'created_at', 'updated_at', 'starts_at', 'mentor', 'limit', 'capacity',
                  'tags']

    tags = serializers.SerializerMethodField(method_name='get_tags')
    title = serializers.CharField(max_length=100, allow_blank=True, allow_null=True, required=False)
    description = serializers.CharField(max_length=1000, allow_blank=True, allow_null=True, required=False)
    capacity = serializers.SerializerMethodField(method_name='get_capacity', read_only=True)
    mentor = serializers.SerializerMethodField(method_name='mentor_name', read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    starts_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    limit = serializers.IntegerField(required=False)

    def get_tags(self, plan: Plan):
        tags = []
        for t in plan.tags.all():
            tags.append(t.title)
        return tags

    def get_capacity(self, plan: Plan):
        return plan.limit - plan.member_set.all().count()

    def mentor_name(self, plan: Plan):
        return plan.mentor.first_name + ' ' + plan.mentor.last_name


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title', 'plans_count', 'detail_url']

    plans_count = serializers.SerializerMethodField(method_name='get_plans_count', read_only=True)
    detail_url = serializers.SerializerMethodField(method_name='get_detail_url', read_only=True)

    def get_detail_url(self, tag: Tag):
        Base_url = 'http://127.0.0.1:8000'
        return "{}/app/tags/{}/".format(Base_url, tag.id)

    def get_plans_count(self, tag: Tag):
        return tag.plan_set.all().count()


class TagDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title', 'plans_count']

    plans_count = serializers.SerializerMethodField(method_name='get_plans_count')

    def get_plans_count(self, tag: Tag):
        return tag.plan_set.all().count()
