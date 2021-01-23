from django.db import models
class InfoModelForm(models.Model):
    jan = models.CharField('日本語',max_length=255)
    eng = models.CharField('英語',max_length=255)
    def __str__(self):
        return '<id:' + str(self.id) + ',' + self.jan+ ',' + self.eng + '>'
# Create your models here.
