import pytest

from core.fixtures.user import user
from core.fixtures.post import post

from core.comment.models import Comment

@pytest.fixture
def comment(db, user, post):
  return Comment.objects.create(
    body="Test Comment Content",
    author=user,
    post=post
  )
