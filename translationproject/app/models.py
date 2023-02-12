from django.db import models


class Person(models.Model):
    name = models.CharField(
        ('Name'), max_length=200, help_text='Input book\'s genre (for example: detective)')
    author = models.ForeignKey(
        'School', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'


class School(models.Model):
    name = models.CharField(
        'Name', max_length=200, help_text='Input book\'s genre (for example: detective)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'School'
        verbose_name_plural = 'Schools'
