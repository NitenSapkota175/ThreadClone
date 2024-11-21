from rest_framework import serializers
from .models import Post, Like, Repost


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["content", "img"]  # Ensure img is also included if needed

    def create(self, validated_data):
        request = self.context.get("request")
        if request and request.user:
            post = Post.objects.create(
                user=request.user,
                content=validated_data.get("content"),  # Fixed field name
                img=validated_data.get("img"),  # Ensure this field exists in the model
            )
            return post
        else:
            raise serializers.ValidationError("User is not authenticated")


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["post"]  # Fixed 'field' to 'fields'

    def create(self, validated_data):
        request = self.context.get("request")
        if request and request.user:
            post = validated_data.get("post")
            like, created = Like.objects.get_or_create(user=request.user, post=post)

            if not created:
                like.delete()
                return None
            return like
        else:
            raise serializers.ValidationError("User is not authenticated")


class RepostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repost
        fields = ["post"]  # Assuming 'post' is the field being reposted

    def create(self, validated_data):
        request = self.context.get("request")
        if request and request.user:
            post = validated_data.get("post")
            repost, created = Repost.objects.get_or_create(user=request.user, post=post)

            if not created:
                raise ValueError("Repost already done")
            return repost
        else:
            raise serializers.ValidationError("User is not authenticated")
