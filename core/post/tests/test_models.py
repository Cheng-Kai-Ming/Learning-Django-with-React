import pytest

from core.fixtures.user import user
from core.post.models import Post

@pytest.mark.django_db
def test_create_post(user):
    post = Post.objects.create(
        body="Test Post Content",
        author=user
    )
    assert post.body == "Test Post Content"
    assert post.author == user
