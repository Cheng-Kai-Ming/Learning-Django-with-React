from django.db import models
from django.utils import timezone
from core.abstract.models import AbstractModel, AbstractManager
# Create your models here.
class PostManager(AbstractManager):
    pass

class Post(AbstractModel):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    author = models.ForeignKey(to='core_user.User', on_delete=models.CASCADE)
    body = models.TextField()
    edited = models.BooleanField(default=False)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2,
                            choices=Status.choices,
                            default=Status.DRAFT)

    objects = PostManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
                models.Index(fields=['-publish']),
                ]
    def __str__(self):
        return f"{self.author.name}"
