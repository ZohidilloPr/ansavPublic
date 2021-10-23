from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

length = 150


class Category(models.Model):
    name = models.CharField(max_length=length, blank=True, null=True)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class ItemName(models.Model):
    creater = models.ForeignKey(
        User, related_name='creater', on_delete=models.CASCADE)
    name = models.CharField(max_length=length, blank=True, null=True)
    ijara_turi = models.CharField(max_length=length, blank=True, null=True)
    narx = models.CharField(max_length=length, blank=True, null=True)
    category = models.ForeignKey(
        Category, related_name='category', on_delete=models.CASCADE)
    campany_name = models.CharField(max_length=length, blank=True, null=True)
    work_type = models.CharField(max_length=length, blank=True, null=True)
    image = models.ImageField(default='ish.jpg', upload_to='item_img')
    teaching_subject = models.CharField(
        max_length=length, blank=True, null=True)
    center_or_teacher_name = models.CharField(
        max_length=length, blank=True, null=True)
    region = models.CharField(max_length=length, blank=True, null=True)
    contact_person = models.CharField(max_length=length, blank=True, null=True)
    contact_number = models.CharField(max_length=length, blank=True, null=True)
    contact_person1 = models.CharField(
        max_length=length, blank=True, null=True)
    contact_number1 = models.CharField(
        max_length=length, blank=True, null=True)
    about = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('Ads:Home', kwargs={'pk': self.pk})

    @property
    def allimages(self):
        allImg = self.images_set.all
        return allImg

    def __str__(self):
        return f'{self.name} by {self.creater}'

    def __unicode__(self):
        return self.name


class Images(models.Model):
    itemname = models.ForeignKey(
        ItemName, on_delete=models.CASCADE, blank=True, null=True)
    images = models.ImageField(upload_to='item_img')

    def __str__(self):
        return f'Image of {self.itemname}'

    def __unicode__(self):
        return self.itemname
