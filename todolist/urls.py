from django.urls import path
from .views import DailyPlanner, update_task, delete_task, delete_all
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('todolist', DailyPlanner, name="todolist"),
    path('update/<int:pk>/', update_task, name='update'),
    path('delete/<int:pk>/', delete_task, name='delete'),
    path('deleteAll', delete_all, name='deleteAll'),
]