from django.shortcuts import render, redirect
from .models import Contacts, Task
from .forms import Form, RegAuth
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages



base_endpoint = "http://127.0.0.1:8000/"

# new

# class CreateCheckoutSessionView(View):

#     def post(self, request, *args, **kwargs):
#         YOUR_DOMAIN = 'http://127.0.0.1:8000/'
#         checkout_session = stripe.checkout.Session.create(
#             line_items=[
#                 {
#                     # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
#                     'price': '{{PRICE_ID}}',
#                     'quantity': 1,
#                 },
#             ],
#             mode='payment',
#             success_url=YOUR_DOMAIN + '/success',
#             cancel_url=YOUR_DOMAIN + '/cancel',
#         )
#         return JsonResponse({
#             'id': checkout_session.id
#         })

# Create your views here.


class Home(LoginRequiredMixin ,TemplateView):
    template_name = 'manage/home.html'
    login_url = "login"



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["forms"] = Form() 
        context['tags'] = Task.objects.all()
        return context



def contacts(request):
    forms = Form

    if request.method == 'POST':
        forms = Form(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
        
    else:
        return render(request, 'manage/home.html', {'forms':forms})
    
def registration(request):
    form = RegAuth

    if request.method == 'POST':
        form = RegAuth(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        return render(request, 'manage/register.html', {'form':form})
    
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.info(request, "Username or Password is Incorrect")



    return render(request, 'manage/login.html')


def logoutt(request):
    logout(request)
    return redirect('home')

