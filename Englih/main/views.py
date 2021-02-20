from django.shortcuts import render
from django.views import generic
from googletrans import Translator
from .models import InfoModelForm
from .models import SecondInfoModelForm
from .models import ThirdInfoModelForm
import random

class IndexView(generic.TemplateView):
    template_name="index.html"



class Index2View(generic.TemplateView):
    template_name="index.html"

# Create your views here.
def review(request):
    #print("test")
    infodata = InfoModelForm.objects.all()
    header = ['番号','日本語','英語']
    #print("ok")
    #print(infodata)

    my_dict2 = {
        'title':'フレーズリスト',
        'val':infodata,
        'header':header,



    }
    return render(request,'review.html',my_dict2)

def test(request):
    number=InfoModelForm.objects.all().count()
    quantity=random.randint(1,number)
    outputDate=InfoModelForm.objects.get(num=quantity)
    print(outputDate.eng)
    word={
        'japanese':outputDate.jan,
        'englih':outputDate.eng,
    }
    return render(request,'test.html',word)

rans_ja="no"
rans_en="no"
def exercise(request):
    text = 'テストです。'
    #print(request.POST)
    try:
        global rans_ja
        global rans_en
        if (request.POST['tolang']=='ja'):
            fromlang="en"
            tolang="ja"
            rans_en = request.POST['text_input']
            translator = Translator(service_urls=['translate.googleapis.com'])
            rans_ja = translator.translate(rans_en,src=fromlang,dest=tolang).text
            text = rans_ja

        else :
            fromlang="ja"
            tolang="en"
            rans_ja = request.POST['text_input']
            translator = Translator(service_urls=['translate.googleapis.com'])
            rans_en = translator.translate(rans_ja,src=fromlang,dest=tolang).text
            text = rans_en

    except:
        return render(request, 'index.html')
    #print("ok")


    context = {
        'text': text,
        'tolang':tolang,
    }
    return render(request, 'index.html', context)

#保存ボタンが押されたら
def move(request):
    print("hitta")
    number=InfoModelForm.objects.all().count()
    addDate=InfoModelForm(jan=rans_ja,eng=rans_en,num=number+1)
    addDate.save()
    return render(request,'index.html')

def delete(request):
    key_name=request.POST.get("key")
    print(key_name)
    InfoModelForm.objects.filter(jan=key_name).delete()

    infodata = InfoModelForm.objects.all()
    print(infodata)
    global changenum
    changenum=1
    for i in infodata:
        print(i.jan)
        i.num=changenum
        i.save()
        print(i.num)
        changenum+=1
    header = ['番号','日本語','英語']
    #print("ok")
    #print(infodata)

    my_dict2 = {
        'title':'フレーズリスト',
        'val':infodata,
        'header':header,
    }
    return render(request,'review.html',my_dict2)

def next(request):
    number=InfoModelForm.objects.all().count()
    quantity=random.randint(1,number)
    print(quantity)
    outputDate=InfoModelForm.objects.get(num=quantity)
    if(request.POST['chan']=='ja'):
        chan="ja"
    else:
        chan="en"
    #print(outputDate.eng)
    word={
        'japanese':outputDate.jan,
        'englih':outputDate.eng,
        'chan':chan
    }
    return render(request,'test.html',word)

def change(request):
    global chan
    if(request.POST['chan']=="ja"):
        print("no")
        chan="en"
    else:
        print('okです')
        chan="ja"
    number=InfoModelForm.objects.all().count()
    quantity=random.randint(1,number)
    print(quantity)
    outputDate=InfoModelForm.objects.get(num=quantity)
    #print(outputDate.eng)
    word={
        'japanese':outputDate.jan,
        'englih':outputDate.eng,
        'chan':chan
    }
    return render(request,'test.html',word)





#データベース
