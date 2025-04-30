from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Blog



class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "email", "username", "first_name", "last_name", "bio", "job_title", "profile_picture",
                  "facebook", "youtube", "instagram", "twitter"]


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id", "username", "email", "first_name", "last_name", "password",
            "bio", "job_title", "profile_picture"
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = get_user_model().objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class SimpleAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "first_name", "last_name", "email", "profile_picture"]

class BlogSerializer(serializers.ModelSerializer):
    author = SimpleAuthorSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'author', 'category', 'content', 'featured_image', 'published_date', 'created_at', 'updated_at', 'is_draft']



class UserInfoSerializer(serializers.ModelSerializer):
    author_posts = serializers.SerializerMethodField()
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email", "first_name", "last_name", "job_title", "bio", "profile_picture", "author_posts"]

    
    def get_author_posts(self, user):
        blogs = Blog.objects.filter(author=user)[:9]
        serializer = BlogSerializer(blogs, many=True)
        return serializer.data