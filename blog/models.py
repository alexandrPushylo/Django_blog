from django.db import models

# Create your models here.


class Post(models.Model):
    author = models.CharField(max_length=20, default='User', verbose_name='Автор')
    image = models.ImageField(upload_to='static/posts',verbose_name='Изображение')
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name='Название')
    desc = models.TextField(max_length=500, verbose_name='Описанние')

    def __str__(self):
        return f"Автор {self.author} - {self.title}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

