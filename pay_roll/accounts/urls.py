
from django.urls import path
from . import views
from pay_roll.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [

 path('', views.home, name = "home"),
 path('create_account/', views.Create_Account_View.as_view(), name='create_account'),
 path('account_type/', views.account_type, name='account_type'),
 path('account_select/', views.select_business_step, name='account_select'),
 path('index', views.create_business, name = 'index'),
 path('upload/', views.upload_business, name = 'upload-book'),
 path('update/<int:book_id>', views.update_business),
 path('delete/<int:book_id>', views.delete_business),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
