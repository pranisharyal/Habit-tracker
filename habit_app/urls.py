from django.urls import path
from habit_app import views

urlpatterns = [
    path('',views.habit_list,name='habit-list'),
    path('create/',views.add_habit,name='add-habit'),
    path("delete/<int:id>/", views.habit_delete, name="habit-delete"),
    path('mark-done/<int:id>/', views.mark_done, name='mark_done'),
    path('view-streak/', views.view_streak, name='view_streak'),
    path('edit/<int:id>/', views.edit_habit, name='edit_habit'), 
    path('charts/', views.view_charts, name='view_charts'),

]