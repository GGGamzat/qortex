from django.db import models


class Singer(models.Model):
    name = models.CharField('Имя', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class Song(models.Model):
    name = models.CharField(max_length=50)
    singer = models.ManyToManyField(Singer, verbose_name='Исполнитель')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'


class Albom(models.Model):
    name = models.CharField('Название', max_length=50)
    singer = models.ForeignKey(Singer, verbose_name='Исполнитесь', on_delete=models.CASCADE)
    song = models.ManyToManyField(Song, verbose_name='Песня')
    date = models.DateField('Дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'