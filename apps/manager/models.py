from django.conf import settings
from django.db import models


# Create your models here.


class OperationType(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False,
                                verbose_name="Пользователь")
    name = models.CharField(max_length=32, blank=False, null=False, verbose_name="Тип операции")

    def __str__(self):
        return f"{self.user_id} | {self.name}"

    class Meta:
        verbose_name = "тип операции"
        verbose_name_plural = "Типы операций"


class Category(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False,
                                verbose_name="Пользователь")
    name = models.CharField(max_length=32, blank=False, null=False, verbose_name="Имя категории")
    type_id = models.ForeignKey(OperationType, on_delete=models.CASCADE, blank=False, null=False,
                                verbose_name="Тип операции")

    def __str__(self):
        return f"{self.user_id} | {self.name}"

    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "Категории"


class Currency(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False,
                                verbose_name="Пользователь")
    name = models.CharField(max_length=32, blank=False, null=False, verbose_name="Название валюты")
    sign = models.CharField(max_length=4, blank=True, null=True, verbose_name="Обозначение валюты")

    def __str__(self):
        return f"{self.user_id} | {self.name}"

    class Meta:
        verbose_name = "валюту"
        verbose_name_plural = "Валюты"


class Operation(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False,
                                verbose_name="Пользователь")
    date = models.DateTimeField(verbose_name="Дата операции")
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False,
                                    verbose_name="Категория")
    type_id = models.ForeignKey(OperationType, on_delete=models.CASCADE, blank=False, null=False,
                                verbose_name="Тип операции")
    value = models.FloatField(blank=False, null=False, verbose_name="Сумма операции")
    currency_id = models.ForeignKey(Currency, on_delete=models.CASCADE, blank=False, null=False,
                                    verbose_name="Валюта операции")
    info = models.TextField(blank=True, null=True, verbose_name="Информация об операции")

    def __str__(self):
        return f"{self.user_id} | {self.date} | {self.type_id} | {self.value} {self.currency_id.sign}"

    class Meta:
        verbose_name = "операцию"
        verbose_name_plural = "Операции"
