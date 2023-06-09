from django.urls import path
from . import views

urlpatterns = [
    path('ils_admin', views.ilsadmin, name="n_ilsadmin"),
    path('ils_admin/staff_treasury', views.staff_treasury,name="n_staff_treasury"),
    path('ils_admin/staff/fut', views.view_fut, name="n_view_fut"),
    path('viewsend/', views.view_send, name='view_send'),
    path('ils_admin/staff/fut_postulated', views.postulated, name="n_postulated"),
    path('ils_admin/staff/fut_pending', views.pending, name="n_pending"),
    path('ils_admin/staff/fut_send', views.send, name="n_send"),
    path('send_01/', views.send_01_treasurer, name="n_send_01"),
    path('admin_login/', views.admin_login, name="n_admin_login"),
    path('send_inssued/', views.send_inssued, name="n_send_inssued")
]