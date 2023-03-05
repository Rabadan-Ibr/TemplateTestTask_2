from django.db import models


class Menu(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)
    url = models.CharField(verbose_name='URL', max_length=200, blank=True)
    named_url = models.CharField(
        verbose_name='named_URL',
        max_length=200,
        blank=True,
        null=True,
    )
    childes = models.ManyToManyField(
        'Menu',
        related_name='parents',
        blank=True,
    )

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = 'name',

    def __str__(self):
        return self.name


class HeadMenu(models.Model):
    menu = models.OneToOneField(
        'Menu',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    title = models.SlugField(verbose_name='Название меню')

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.title
