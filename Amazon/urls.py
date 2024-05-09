from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path('',views.list_page,name="list"),
    path('login/',views.user_login,name='login'),
    path('signup/',views.user_signup,name='signup'),
    path('logout/',views.user_logout,name='logout'),
    path ('<int:id>',views.detail_page,name="detail"),  
    path('Home/',views.bootstarp_page,name="bootstarppage"),
    path('Product',views.Product_page,name="Productpage"),
    path('rangelist/',views.student_range),
    path('Product1',views.Product1_file,name="Productfile"),
    path('search/', views.search, name='search_view'),
    path('index/',views.product_list,name='product_list'),
    path('cart/',views.view_cart,name='view_cart'),
    path('add/<int:product_id>',views.add_to_cart,name='add_to_cart'),
    path('remove/<int:item_id>',views.remove_from_cart,name='remove_from_cart'),
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)