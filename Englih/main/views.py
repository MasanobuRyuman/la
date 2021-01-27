from django.shortcuts import render
from django.views import generic
from googletrans import Translator
from .models import InfoModelForm


class IndexView(generic.TemplateView):
    template_name="index.html"



class Index2View(generic.TemplateView):
    template_name="index.html"

# Create your views here.
def review(request):
    #print("test")
    infodata = InfoModelForm.objects.all()
    header = ['番号','日本語','英語']
    id=0
    #print("ok")
    #print(infodata)
    
    my_dict2 = {
        'title':'フレームリスト',
        'val':infodata,
        'header':header,
        'id':id,


        
    }
    return render(request,'review.html',my_dict2)



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
    cou=InfoModelForm.objects.all().count()
    for i in range(cou+1):
        print(i)
        if f'{i}' in request.POST:
            InfoModelForm.objects.filter(num=i).delete()

    return render(request,'index.html')
#データベース
    

