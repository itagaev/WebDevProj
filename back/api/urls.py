from django.urls import path
from api import views

# urlpatterns=[
#     path('task_lists/', views.task_lists),
#     #path('task_lists/',views.tasklists),
#     path('task_lists/<int:pk>/', views.tasklist_detail),
#     #path('task_lists/<int:pk>/tasks/', views.tasks),
# ]

urlpatterns = [
    path('task_lists/', views.TaskLists.as_view()),
    path('task_lists/<int:pk>/', views.TaskList_detail.as_view()),
    path('doctors/', views.DoctorList.as_view()),
    path('doctors/<int:pk>/', views.Doctor_detail.as_view()),
    path('patients/', views.PatientList.as_view()),
    path('patients/<int:pk>/', views.Patient_detail.as_view()),
    path('hospitals/', views.TaskLists.as_view()),
    path('hospitals/<int:pk>/', views.TaskList_detail.as_view()),
    path('medicines/', views.TaskLists.as_view()),
    path('medicines/<int:pk>/', views.TaskList_detail.as_view()),
    path('users/', views.UserList.as_view()),
    path('login/', views.user_login),
]
