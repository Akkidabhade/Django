from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.main_page, name="Home"),
    path('login/',views.user_login,name='login'),
    path('signup/',views.user_signup,name='signup'),
    path('logout/',views.user_logout,name='logout'),
    path('add/', views.add, name="ADD"),
    path('Customer/', views.customer, name="Customer"),
    path('customer/<int:id>/', views.detail, name='detail'),
    path('personal-banking/', views.personal_bank, name='personal'),
    path('rangelist/',views.customer_range),
    path('search/', views.search, name='search_view'),
    path('Car/', views.Car, name='car'),
    path('gold-banking/', views.Gold_Loan, name='gold'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
