import dataclasses
import json

from .models import CreatePost, Post, factory

import requests


class Client:
    def __init__(self, base_url=None, await_timeout=None):
        self.base_url = base_url if base_url else "https://jsonplaceholder.typicode.com"
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json;q=0.9,*/*;q=0.8"
        }

        self.await_timeout = await_timeout if await_timeout else 10
        self.assert_status_code = True

    def create_post(self, request: CreatePost):
        data = dataclasses.asdict(request, dict_factory=factory) if isinstance(request, CreatePost) else request
        response = requests.post(url=f"{self.base_url}/posts",
                                 headers=self.headers,
                                 data=json.dumps(data))
        if response.status_code == 201:
            return Post(**response.json())

        return response

    def get_post(self, post_id: int):
        response = requests.get(url=f"{self.base_url}/posts/{post_id}",
                                headers=self.headers)

        if response.status_code == 200:
            return Post(**response.json())

        return response

    def delete_post(self, post_id: int):
        response = requests.delete(url=f"{self.base_url}/posts/{post_id}")

        return response
