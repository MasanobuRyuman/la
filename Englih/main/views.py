from django.shortcuts import render
from django.views import generic
from googletrans import Translator

class IndexView(generic.TemplateView):
    template_name="index.html"

class ReviewView(generic.TemplateView):
    template_name="review.html" 

# Create your views here.
def review(request):
    return render(request,'review.html')

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
