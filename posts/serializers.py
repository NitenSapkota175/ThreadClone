from rest_framework import serializers
from .models import Post, Like, Repost


class PostSerializers(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ["content", "img"]

    def create(self, validated_data):

        request = self.context["request"]
        if request and request.user:
            post = Post.objects.create(
                user=request.user,
                context=validated_data.get("content"),
                img=validated_data.get("img"),
            )
            return post
        else:
            raise serializers.ValidationError("User is not authenticated")


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        field = ["post"]

    def create(self, validate_data):
        request = self.context["request"]

        if request and request.user:
            post = validate_data.get("post")

            like, created = Like.objects.get_or_create(user=request.user, post=post)

            if not created:
                like.delete()
                return None
            return like
        else:
            raise serializers.ValidationError("user is not authenticated")


class RepostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Repost
        field = ["repost"]

        def create(self, validated_data):
            request = self.content["request"]

            if request and request.user:
                post = validated_data.get("post")
                repost, created = Post.objects.get_or_create(
                    user=request.user, post=post
                )

                if not created:
                    raise ValueError("repost already done")
                return repost
