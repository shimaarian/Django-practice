from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# approach1
# create personnel manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

# approach2
# add method for defualt manager
class PublidhYearManager(models.Manager):
    def filter_year(self, year):
        return self.filter(publish__year=year)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PUB', 'Published'
        REJECTED = 'REJECTED', 'Rejected'

    # posts fields
    title = models.CharField(max_length=150)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)

    # relations
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')

    # date post
    publish = models.DateTimeField(default=timezone.now)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255)


    # cusum manager
    # objects = PublidhYearManager()

    objects = models.Manager()
    # define new mangers
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title



