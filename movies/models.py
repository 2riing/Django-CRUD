
from django.db import models
# 이거 뭔지 모름
from django.conf import settings

class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    # settings.py에 있는 AUTH USER MODEL에서 user id 가져오기
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=100)
    # on delete CASCADE가 뭔지 모름
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # settings.py에 있는 AUTH USER MODEL에서 user id 가져오기
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)