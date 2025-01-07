from django.views.generic import ListView
from .models import Message

# Create your views here.

class MessageView(ListView):
    model = Message
    template_name = 'home.html'
    

# def messageView(request):
#     return render(request, 'home.html')
