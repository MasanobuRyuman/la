from django.shortcuts import render
from django.views import generic
from googletrans import Translator
from .models import InfoModelForm
from .models import SecondInfoModelForm
from .models import ThirdInfoModelForm
import random

class formView(generic.TemplateView):
    template_name="form.html"



class Index2View(generic.TemplateView):
    template_name="index.html"

# Create your views here.


#ログイン
def confirmation(request):
    global username
    #print(request.POST['name_input'])
    #print(request.POST['password_input'])
    username=request.POST['name_input']
    userpassword=request.POST['password_input']
    alldatecount=ThirdInfoModelForm.objects.all().count()
    if (alldatecount==0):
        answer={
            "text":"名前かパスワードが間違っています。"
        }
        return render(request,'login.html',answer)
    alldate=ThirdInfoModelForm.objects.all()
    for i in alldate:
        if(username==i.name and userpassword==i.password):
            return render(request,'index.html')
    answer={
        "text":"名前かパスワードが間違っています。"
    }
    return render(request,'login.html',answer)

#新規登録
def registration(request):
    global username
    #print(request.POST['name_input'])
    #print(request.POST['password_input'])
    username=request.POST['name_input']
    userpassword=request.POST['password_input']
    alldatecount=ThirdInfoModelForm.objects.all().count()
    #print(alldatecount)
    if (alldatecount==0):
        print("なにも入っていない")
        addDate=ThirdInfoModelForm(name=username,password=userpassword)
        addDate.save()
        update=InfoModelForm(name=username)
        update.save()
        return render(request,'index.html')
    alldate=ThirdInfoModelForm.objects.all()
    for i in alldate:
        if (username==i.name):
            print("すでに入っていた")
            answer={
                "text":"すでに使われてる名前です"
            }
            return render(request,'newlogin.html',answer)
    newdate=ThirdInfoModelForm(name=username,password=userpassword)
    newdate.save()
    update=InfoModelForm(name=username)
    update.save()
    return render(request,'index.html')



def review(request):
    #print("test")
    infodata = SecondInfoModelForm.objects.filter(name=username)
    header = ['番号','日本語','英語','']
    #print("ok")
    #print(infodata)

    my_dict2 = {
        'title':'フレーズリスト',
        'val':infodata,
        'header':header,



    }
    return render(request,'review.html',my_dict2)

def test(request):
    number=SecondInfoModelForm.objects.filter(name=username).count()
    if (number==0):
        answer={
            "text":"フレーズが保存されていません"
        }
        return render(request,'review.html',answer)
    quantity=random.randint(1,number)
    outputDate=SecondInfoModelForm.objects.get(name=username,wordID=quantity)
    #print(outputDate.eng)
    word={
        'japanese':outputDate.jan,
        'englih':outputDate.eng,
    }
    return render(request,'test.html',word)

def login(request):
    return render(request,'login.html')

def newlogin(request):
    return render(request,'newlogin.html')

rans_ja="no"
rans_en="no"

#翻訳
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
    #print("hitta")
    number=SecondInfoModelForm.objects.filter(name=username).count()
    addDate=SecondInfoModelForm(name=username,wordID=number+1,jan=rans_ja,eng=rans_en)
    addDate.save()
    return render(request,'index.html')

def delete(request):
    key_name=request.POST.get("key")
    #print(key_name)
    SecondInfoModelForm.objects.filter(jan=key_name).delete()

    infodata = SecondInfoModelForm.objects.filter(name=username)
    #print(infodata)
    global changenum
    changenum=1
    for i in infodata:
        #print(i.jan)
        i.wordID=changenum
        i.save()
        #print(i.wordID)
        changenum+=1
    header = ['番号','日本語','英語',""]
    #print("ok")
    #print(infodata)

    my_dict2 = {
        'title':'フレーズリスト',
        'val':infodata,
        'header':header,
    }
    return render(request,'review.html',my_dict2)

def next(request):
    number=SecondInfoModelForm.objects.filter(name=username).count()
    quantity=random.randint(1,number)
    #print(quantity)
    outputDate=SecondInfoModelForm.objects.get(name=username,wordID=quantity)
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
    number=SecondInfoModelForm.objects.filter(name=username).count()
    quantity=random.randint(1,number)
    #print(quantity)
    outputDate=SecondInfoModelForm.objects.filter(name=username).get(wordID=quantity)
    #print(outputDate.eng)
    word={
        'japanese':outputDate.jan,
        'englih':outputDate.eng,
        'chan':chan
    }
    return render(request,'test.html',word)



#ログイン・新規登録からフォームまで戻る
def back(request):
    return render(request,'form.html')


#データベース
