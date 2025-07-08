from django.urls import path
from .views import student_add, student_list, student_update, student_delete


urlpatterns = [
    path('', student_list, name='student_list'),
    path('add/', student_add, name='student_add'),
    path('update/<int:stud_id>/',student_update, name='student_update'),
    path('delete/<int:stud_id>/', student_delete, name='student_delete'),
]