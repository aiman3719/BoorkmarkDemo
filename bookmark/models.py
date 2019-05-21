from django.db import models

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('site URL')

    def __str__(self):
        # 객체를 출력할 떄 나타나는 값
        return "명칭: " + self.site_name + ",    주소 : " + self.url

