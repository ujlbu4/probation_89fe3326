from .models import CreatePost
from .client import Client

import pytest


@pytest.fixture(scope='function')
def fixture_existed_post():
    client = Client()
    new_post = CreatePost.generate()
    return client.create_post(new_post)


class TestPosts:
    @classmethod
    def setup_class(cls):
        cls.client = Client()
        pass

    def test_create_post(self):
        # given
        new_post = CreatePost.generate()

        # when
        created_post = self.client.create_post(new_post)

        # then
        assert created_post.title == new_post.title

        # check it exists
        existed_post = self.client.get_post(post_id=created_post.id)
        assert existed_post.title == new_post.title

    def test_get_existed_post(self, fixture_existed_post):
        # given
        existed_post = fixture_existed_post

        # when
        response_post = self.client.get_post(post_id=existed_post.id)

        # then
        assert response_post.title == existed_post.title

    def test_delete_post(self, fixture_existed_post):
        # given
        existed_post = fixture_existed_post

        # when
        response = self.client.delete_post(post_id=existed_post.id)

        # then
        assert response.status_code == 200

        # check it no more exist
        response = self.client.get_post(post_id=existed_post.id)
        assert response.status_code == 404

    # def test_negative_unexist_post(self):
    #     pass
    # ...
