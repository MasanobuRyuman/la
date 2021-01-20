from django.shortcuts import render
from django.views import generic

class IndexView(generic.TemplateView):
    template_name="index.html"
# Create your views here.

def exercise(request):
    text = 'テストです。'
    print(request.POST)
    try:
        input_text = request.POST['text_input']
    
        text = input_text
    except:
        return render(request, 'index.html')
    print("ok")

    
    context = {
        'text': text,
    }
    return render(request, 'index.html', context)
