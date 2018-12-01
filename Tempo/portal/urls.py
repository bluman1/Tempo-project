from . import views
from django.urls import path

app_name='portal'

urlpatterns = [
    path('',views.formpage, name='formpage'),
    path('<int:staff_id>/',views.approval),
    path('requests/',views.requests)
]
