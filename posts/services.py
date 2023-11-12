from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from .models import Post
from django.utils import timezone

@dataclass
class Post_DTO:
    id: int
    content: str
    created_at: datetime
    updated_at: datetime


class IPostService(ABC):

    @classmethod
    @abstractmethod
    def list(cls) -> list[Post]:
        pass

    @classmethod
    @abstractmethod
    def create(cls) -> Post:
        pass
