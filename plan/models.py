from django.db import models
from taggit.managers import TaggableManager


class Plan(models.Model):

    class Meta:
        verbose_name_plural = "プラン"

    title = models.CharField("プランタイトル", max_length=255)
    description = models.CharField("プランの説明", max_length=255)
    image = models.ImageField("イメージ画像", upload_to='', default="")
    price = models.PositiveIntegerField("料金", default=0)
    tags = TaggableManager("タグ", blank=True)

    def __str__(self):
        return self.title
