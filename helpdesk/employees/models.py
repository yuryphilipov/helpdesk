from django.db import models
from django.urls import reverse


class Person(models.Model):

    first_name = models.CharField(max_length=30, help_text="Имя", verbose_name="Имя")
    last_name = models.CharField(max_length=30, help_text="Фамилия", verbose_name="Фамилия")
    middle_name = models.CharField(max_length=30, help_text="Отчество", verbose_name="Отчество", default="", null=True,
                                   blank=True)
    birthdate = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    department = models.ForeignKey("Department", help_text="Подразделение", verbose_name="Подразделение",
                                   on_delete=models.SET_NULL, null=True)
    job_position = models.CharField(max_length=50, help_text="Должность", verbose_name="Должность", null=True,
                                    blank=True)
    tabn = models.CharField(max_length=10, help_text="Табельный номер", verbose_name="Табельный номер")
    
    class Meta:
        ordering = ["last_name", "first_name"]
        permissions = (("can_view", "Право просмотра записи"),)
    
    def __str__(self):
        return ' '.join((self.last_name, self.first_name, self.middle_name if self.middle_name else ''))

    def get_absolute_url(self):
        return reverse('person-detail', args=[str(self.id)])
        

class Department(models.Model):
    
    name = models.CharField(max_length=50, help_text="Наименование подразделения", verbose_name="Наименование")
    short_name = models.CharField(max_length=30, help_text="Краткое наименование", verbose_name="Краткое наименование")
    main_department = models.ForeignKey("self", help_text="Вышестоящее подразделение",
                                        verbose_name="Вышестоящее подразделение", on_delete=models.SET_NULL, null=True,
                                        blank=True)
    
    def __str__(self):
        return self.short_name