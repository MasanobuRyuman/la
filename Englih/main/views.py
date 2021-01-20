from django.shortcuts import render
from django.views import generic
from googletrans import Translator

class IndexView(generic.TemplateView):
    template_name="index.html"
# Create your views here.

def exercise(request):
    text = 'テストです。'
    print(request.POST)
    try:
        input_text = request.POST['text_input']
        translator = Translator(service_urls=['translate.googleapis.com'])
        rans_en = translator.translate(input_text,src="en",dest="ja").text
    
        text = rans_en
    except:
        return render(request, 'index.html')
    print("ok")

    
    context = {
        'text': text,
    }
    return render(request, 'index.html', context)
