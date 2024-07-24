"""
URL configuration for maimoontraders project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp import views as mainapp
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.splash_page,name='splash_page'),
    path('home/', mainapp.homePage,name='homepage'),
    path('adminpage/', mainapp.adminpage,name='adminpage'),
    path('signup/', mainapp.registerPage,name='registerpage'),
    path('signin/', mainapp.siginpage,name='loginpage'),
    # path('adminlogout/', mainapp.admin_signout,name='adminlogout'),
    path('uploadphoto/', mainapp.uploadphoto,name='uploadphoto'),
    path('signout/', mainapp.signout,name='signout'),
    path('category/', mainapp.categoryPage,name='categorypage'),
    path('salespage/', mainapp.AdminSalesaPage,name='admin_sales_page'),
    path('category/<str:product_category>/', mainapp.categoryfilter, name='category_filter'),
    
    path('productlist/', mainapp.AdminProductList,name='admin_ProductList'),
    path('salesreport/', mainapp.Admin_Salesreport,name='admin_salesreport'),
    path('websiteorders/', mainapp.notify_website_order_to_admin, name='websiteorders'),
    path('admindashboard/', mainapp.AdminDashboard,name='admin_dashboard'),
    path('api/inventory-data/', mainapp.get_inventory_data, name='get_inventory_data'),
    # path('test/', mainapp.testin_whatspp, name='testin_whatspp'),
    path('cart/<str:product>', mainapp.add_to_cart, name='add_to_cart'),
    path('cart_purchase', mainapp.purchase_cart, name='purchase_cart'),
    path('cart/remove/<str:product_code>/', mainapp.remove_from_cart, name='remove_from_cart'),
    path('cart/', mainapp.cart, name='cart'),
    path('ordered/', mainapp.order_placed, name='ordered'),
    path('footer_query_form/', mainapp.queryform_data, name='queryform_data'),
    path('history/', mainapp.user_past_purchase, name='history'),
    
]


if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
