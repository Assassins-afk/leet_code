from django.db import models


class Articles(models.Model):
    user = models.CharField('Фио', max_length=50)
    mail = models.CharField('Эл.Почта', max_length=250)
    sex = models.CharField('Пол', max_length=10)
    phone = models.CharField('Номер телефона', max_length=20)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'