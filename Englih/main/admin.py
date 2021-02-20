from django.contrib import admin
from .models import InfoModelForm
from .models import SecondInfoModelForm
from .models import ThirdInfoModelForm

admin.site.register(InfoModelForm)
admin.site.register(SecondInfoModelForm)
admin.site.register(ThirdInfoModelForm)

# Register your models here.
