import pytest

from core.fixtures.user import user
from core.fixtures.post import post
from core.comment.models import Comment

@pytest.mark.django_db
def test_create_comment(user, post):
    comment = Comment.objects.create(
        body="Test Comment Content",
        author=user,
        post=post
    )
    assert comment.body == "Test Comment Content"
    assert comment.author == user
    assert comment.post == post
