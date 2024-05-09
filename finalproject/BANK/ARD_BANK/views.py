from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from .models import Cunsumer
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm

def main_page(request):
    return render(request, 'HOME.html')

def add(request):
    return render(request, 'adding.html')

def customer(request):
    obj = Cunsumer.objects.all()
    return render(request, 'Customer.html',{'obj':obj})

def detail(request, id):
    obj = get_object_or_404(Cunsumer, pk=id)
    return render(request, 'details.html', {'obj': obj})
def personal_bank(request):
    return render(request,'personal.html')

def adding(request):
    c=request.POST['name']
    d=request.POST['phone']
    e=request.POST['account_no']
    f=request.POST['dob']
    q=request.POST['addr']
    g=request.POST['email']
    h=request.POST['image']
    obj=Cunsumer(name=c,phone=d,account_no=e,dob=f,addr=q,email=g,image=h)
    obj.save()
    return redirect("/")


def customer_range(request):
    queryset = Cunsumer.customers.get_customer_amount_range(10000,20000)
    context = {'obj': queryset}
    return render(request, 'Customer.html', context)

def search(request):
    query = request.GET.get('query')
    if query:
        results = Cunsumer.customers.search(query)
    else:
        results = 'No data'
    return render(request, 'search.html', {'results': results})

def Car(request):
    return render(request, 'Carloan.html')

def Gold_Loan(request):
    return render(request,'goldloan.html')



def user_signup(request):
     if request.method=='POST' :
          form = SignupForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('login')
     else:
              form=SignupForm()
     return render(request,'signup.html',{'form' :form})
         

#login
def user_login(request):
     if request.method=='POST':
       form = LoginForm(request.POST)
       if form.is_valid():
          username=form.cleaned_data['username']
          password=form.cleaned_data['password']
          user = authenticate(request, username=username, password=password)
          if user:
               login(request, user)
               return redirect('Home')
     else:
         form=LoginForm()
     return render(request, 'login.html',{'form':form})

#logout
def user_logout(request):
     logout(request)
     return redirect('login')