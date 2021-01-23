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
    print("test")
    infodata = InfoModelForm.objects.all()
    header = ['ID','日本語','英語']
    print("ok")
    print(infodata)
    
    my_dict2 = {
        'title':'テスト',
        'val':infodata,
        'header':header


        
    }
    return render(request,'review.html',my_dict2)

def move(request):
    print("haitta")

fromlang="en"
tolang="ja"

def exercise(request):
    text = 'テストです。'
    print(request.POST)
    try:
        if (request.POST['tolang']=='ja'):
            fromlang="en"
            tolang="ja"
        else :
            fromlang="ja"
            tolang="en"
        input_text = request.POST['text_input']
        translator = Translator(service_urls=['translate.googleapis.com'])
        rans_en = translator.translate(input_text,src=fromlang,dest=tolang).text
    
        text = rans_en
    except:
        return render(request, 'index.html')
    print("ok")

    
    context = {
        'text': text,
        'tolang':tolang,
    }
    return render(request, 'index.html', context)

#データベース
    

