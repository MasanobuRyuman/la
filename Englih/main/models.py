from django.db import models
class InfoModelForm(models.Model):
    userID = models.CharField('ユーザID',max_length=255)
    def __str__(self):
        return '<id:' + str(self.id) + ',' + self.userID+ ',' + '>'
# Create your models here.
class SecondInfoModelForm(models.Model):
    wordID = models.CharField('単語ID',max_length=255)
    userID = models.CharField('ユーザID',max_length=255)
    eng = models.CharField('英語',max_length=255)
    jan = models.CharField('日本語',max_length=255)
    def __str__(self):
        return '<id:' + str(self.id) + ',' + self.wordID + ',' + self.userID + ',' + self.eng + ',' + self.jan + ',' + '>'

class ThirdInfoModelForm(models.Model):
    userID = models.CharField('ユーザID',max_length=255)
    name = models.CharField('名前',max_length=255)
    password = models.CharField('パスワード',max_length=255)
    def __str__(self):
        return '<id:' + str(self.id) + ',' + self.userID+ ',' + self.name + ',' + self.password + ',' + '>'
