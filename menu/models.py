from django.db import models
from django.urls import reverse
from django.http import Http404


class MenuItem(models.Model):
    """Модель меню"""
    name = models.CharField(max_length=50, verbose_name="Название Меню")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name="Родительская таблица")
    explicit_url = models.CharField(max_length=100, blank=True, null=True, unique=True, verbose_name="Явный адрес",
                                    help_text="Нужно указывать в таком формате - app/желаемый_номер. Номер должен быть "
                                              "свободен")
    named_url = models.CharField(max_length=100, blank=True, null=True, unique=True, verbose_name="Именованный адрес",
                                 help_text="Нужно указывать в таком формате - app:new желаемый_номер(пробел обязателен)")

    def save(self, *args, **kwargs):
        """ Сохранение в БД, а так же создание адреса под конкретную менюшку """
        if self.named_url:
            named_url_parts = self.named_url.split()
            url_name = named_url_parts[0]
            params = named_url_parts[1:len(named_url_parts)]
            reversed_named_url = reverse(url_name, args=params)
            if self.explicit_url:
                if self.explicit_url != reversed_named_url:
                    raise Http404('explicit_url does not match named_url')
            else:
                self.explicit_url = reversed_named_url
        super(MenuItem, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def children(self):
        return self.menuitem_set.all()

    def get_elder_ids(self):
        """Получаем id родителя"""
        if self.parent:
            return self.parent.get_elder_ids() + [self.parent.id]
        else:
            return []

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Список Меню"
