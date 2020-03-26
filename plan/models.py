from django.db import models
from taggit.managers import TaggableManager


class Tag(models.Model):
    """タグ"""
    name = models.CharField("名称", max_length=64, unique=True)

# class Tag(models.Model):
#     """ タグ """
#     name = models.CharField("名称", max_length=64, unique=True)

#     @classmethod
#     def get_or_create(cls, name):
#         """ 指定された名称のタグを生成して返す、既にあればそれを取得して返す """
#         ret = cls.objects.filter(name=name).first()
#         if not ret:
#             ret = cls.objects.create(name=name)
#         return ret

#     @classmethod
#     def multi_get_or_create(cls, names):
#         if not names:
#             return []
#         tags = []
#         for name in names:
#             tags.append(Tag.get_or_create(name))
#         return tags

#     def __str__(self):
#         return self.name

#     class Meta:
#         db_table = "tag"


class Plan(models.Model):

    class Meta:
        verbose_name_plural = "プラン"

    title = models.CharField("プランタイトル", max_length=255)
    description = models.CharField("プランの説明", max_length=255)
    image = models.ImageField("イメージ画像", upload_to='', default="")
    price = models.PositiveIntegerField("料金", default=0)
    tags = models.ManyToManyField(Tag)

    # tags = models.ManyToManyField(Tag)
    # tags = TaggableManager("タグ", blank=True)

    def __str__(self):
        return self.title


# python manage.py migrate --fake kakeibo zero
# python manage.py dbshell
