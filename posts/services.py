from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from .models import Post
from django.utils import timezone

@dataclass
class Post_DTO:
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_django_model(cls, post_service: Post) -> 'Post_DTO':
        return Post_DTO(
            id=post_service.id,
            title=post_service.title,
            content=post_service.content,
            created_at=post_service.created_at,
            updated_at=post_service.updated_at
        )


class IPostService(ABC):

    @classmethod
    @abstractmethod
    def list(cls) -> list[Post]:
        pass

    @classmethod
    @abstractmethod
    def create(cls, title: str, content: str) -> Post_DTO:
        pass

    @classmethod
    @abstractmethod
    def get(cls, id: int) -> Post_DTO:
        pass


class PostNotFound(Exception):
    pass


class PostService(IPostService):

    @classmethod
    def list(cls):
        return [Post_DTO.from_django_model(p) for p in Post.objects.all()]

    @classmethod
    def create(cls, title: str, content: str) -> Post_DTO:
        post = Post.objects.create(
            title=title,
            content=content
        )
        return Post_DTO.from_django_model(post)

    @classmethod
    def get(cls, id: int) -> Post_DTO:
        try:
            return Post_DTO.from_django_model(Post.objects.get(id=id))
        except Post.DoesNotExist:
            raise PostNotFound
