from django.db import models

class User(models.Model):
    user_ID = models.CharField(max_length=20, blank=False)
    user_PW = models.CharField(max_length=20, blank=False)
    e_mail = models.CharField(max_length=20, null=True, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=False)
    adress = models.CharField(max_length=20, null=True, blank=False)
    user_date = models.DateTimeField(null=True, blank=False)
    user_gender = models.BooleanField(default=True)

class Recipe(models.Model):
    user_ID = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=False)
    Recipe_name = models.CharField(max_length=20, blank=False)
    type_list = (('1','한식'), ('2','일식'),('3','중식'),('4','분식'),('5','야식'),('6','아시안'))
    type = models.CharField(max_length=20, choices=type_list, blank=False)
    Recipe_date = models.DateTimeField(null=True, blank=False)
    Recipe_image = models.ImageField(null=True, blank=True, default="photo")
    Recipe_etc = models.CharField(max_length=20, null=True, blank=False)
    Recipe_recommend = models.IntegerField(default=0)
