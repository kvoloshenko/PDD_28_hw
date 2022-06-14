from django.db import models
from usersapp.models import BlogUser

# Create your models here.
class TimeStamp(models.Model):
    """
    Abstract - для нее не создаются новые таблицы
    данные хранятся в каждом наследнике
    """
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Hh_Request(TimeStamp):
    keywords = models.TextField(blank=False)
    # user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.keywords

    def get_options_list(self):
        OPTIONS_LIST = [
            ('all', 'Везде'),
            ('company', 'В названии компании'),
            ('name', 'В названии вакансии'),
        ]
        return OPTIONS_LIST

class Hh_Response(models.Model):
    request = models.ForeignKey(Hh_Request, on_delete=models.CASCADE)
    skill_name = models.TextField(blank=False)
    skill_count = models.PositiveIntegerField (blank=False)
    skill_persent = models.PositiveIntegerField (blank=False)

    def __str__(self):
        return f'{self.request} {self.skill_name} {self.skill_count} {self.skill_persent}%'