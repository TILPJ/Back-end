from rest_framework import serializers

from .models import ClipperSite, ClipperCourse, ClipperChapter, ClipperSection, MyCourse


class ClipperSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClipperSite
        fields = ["name"]


class ClipperCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClipperCourse
        fields = ["title", "instructor"]


class MyCourseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.email")
    site_info = ClipperSiteSerializer(source="site", read_only=True)
    course_info = ClipperCourseSerializer(source="course", read_only=True)
    site = serializers.PrimaryKeyRelatedField(queryset=ClipperSite.objects.all())
    course = serializers.PrimaryKeyRelatedField(queryset=ClipperCourse.objects.all())

    class Meta:
        model = MyCourse
        fields = ["id", "owner", "site", "course", "site_info", "course_info"]
