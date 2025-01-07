from django.views.generic import TemplateView

# Create your views here.

class MessageView(TemplateView):
    template_name = 'home.html'
    

# def messageView(request):
#     return render(request, 'home.html')
