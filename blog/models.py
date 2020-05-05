from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): #모델(객체)정의
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) #짧은 문자열
    text = models.TextField() #긴 텍스트 입력, 블로그 컨텐츠 담기
    created_date = models.DateTimeField( #날짜 시간
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): #메서드
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title