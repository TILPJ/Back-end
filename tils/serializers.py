from rest_framework import serializers

from .models import Til
from courses.models import MyCourse, ClipperSection, ClipperCourse
from courses.serializers import MyCourseSerializer, ClipperCourseSerializer
from accounts.models import CustomUser


class TilSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.email")
    mycourse = serializers.PrimaryKeyRelatedField(
        queryset=MyCourse.objects.all(), write_only=True
    )

    # def get_user_id(email):
    #     if
    #     print("========", CustomUser.objects.filter(email=email))

    #     return CustomUser.objects.filter(email=email)

    section = serializers.PrimaryKeyRelatedField(
        queryset=ClipperSection.objects.all(),
        write_only=True,
    )
    course_title = serializers.SerializerMethodField()
    section_name = serializers.SerializerMethodField()

    def get_course_title(self, obj):
        return obj.mycourse.course.title

    def get_section_name(self, obj):
        return obj.section.name

    class Meta:
        model = Til
        fields = [
            "id",
            "owner",
            "date",
            "mycourse",
            "section",
            "star",
            "memo",
            "course_title",
            "section_name",
        ]
