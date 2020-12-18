from dataclasses import dataclass
import random
import uuid


def factory(data):
    return dict(x for x in data if x[1] is not None)


@dataclass
class CreatePost:
    title: str
    body: str
    userId: int

    @classmethod
    def generate(cls):
        return cls(title=f"{uuid.uuid4()}", body=f"some unique text: {uuid.uuid4()}", userId=random.randint(1, 100))


@dataclass
class Post:
    id: int
    title: str
    body: str
    userId: int
