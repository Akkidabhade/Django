from django.shortcuts import redirect, render,get_object_or_404
from .models import StudentProfile
from .models import CustomeManager
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from.models import Product
from.models import CartItems

def product_list(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})


def view_cart(request):
    cart_items= CartItems.objects.filter(user=request.user)
    total_price= sum(item.product.price*item.quantity for item in cart_items)
    return render(request,'cart.html',{'cart_items': cart_items,'total_price':total_price})

def add_to_cart(request,product_id):
    product= Product.objects.get(id=product_id)
    cart_item,created=CartItems.objects.get_or_create(product=product,user=request.user)
    cart_item.quantity +=1
    cart_item.save()
    return redirect('view_cart')

def remove_from_cart(request,item_id):
    cart_item = CartItems.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')


#signup or register form
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
               return redirect('Productpage')
     else:
         form=LoginForm()
     return render(request, 'login.html',{'form':form})

#logout
def user_logout(request):
     logout(request)
     return redirect('Productpage')

def list_page(request):
    obj=StudentProfile.objects.all()
    return render(request,'list.html',{'obj':obj})

def detail_page(request,id):
    obj=get_object_or_404(StudentProfile,pk=id)
    return render(request,'details.html',{'obj':obj})

def bootstarp_page(request):
    return render(request,'bootstarp.html')


def Product_page(request):
    return render(request,'Product.html')

def student_range(request):
    queryset = StudentProfile.students.get_student_percentage_range(30,35)
    context = {'obj': queryset}
    return render(request, 'list.html', context)

def Product1_file(request):
    return render(request,'Product1.html')

def search(request):
    query = request.GET.get('query')
    if query:
        results = StudentProfile.students.search(query)
    else:
        results = 'No data'
    return render(request, 'search_results.html', {'results': results})
