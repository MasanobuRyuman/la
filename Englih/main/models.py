from django.db import models
class InfoModelForm(models.Model):
    name = models.CharField('ユーザID',max_length=255)
    def __str__(self):
        return '<id:' + str(self.id) + ',' + self.name + ',' + '>'
# Create your models here.
class SecondInfoModelForm(models.Model):
    name = models.CharField('ユーザID',max_length=255)
    wordID = models.CharField('単語ID',max_length=255)
    eng = models.CharField('英語',max_length=255)
    jan = models.CharField('日本語',max_length=255)
    def __str__(self):
        return '<id:' + str(self.id) + ',' + self.name + ',' + self.wordID + ',' + self.eng + ',' + self.jan + ',' + '>'

class ThirdInfoModelForm(models.Model):
    name = models.CharField('名前',max_length=255)
    password = models.CharField('パスワード',max_length=255)
    def __str__(self):
        return '<id:' + str(self.id) + ',' + self.name + ',' + self.password + ',' + '>'
