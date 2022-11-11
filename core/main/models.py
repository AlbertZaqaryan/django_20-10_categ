from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Category name', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Firm(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Categ')
    name = models.CharField('Firm name', max_length=30)
    about = models.TextField('Firm about')
    history = models.TextField('Firm history', null=True)
    img = models.ImageField('Firm image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Firm'
        verbose_name_plural = 'Firms'


class History(models.Model):
    text = models.TextField('History Text')


    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'History'
        verbose_name_plural = 'Histories'