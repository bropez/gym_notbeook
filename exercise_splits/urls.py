from django.urls import path

from . import views


app_name = 'workouts'
urlpatterns = [
    path('', views.WD_ListView.as_view(), name='index'),
    path('workout_day/new/', views.WD_CreateView.as_view(), name='wd_create'),
    path('workout_day/<int:pk>/update/', views.WD_UpdateView.as_view(), name='wd_update'),
    path('workout_day/<int:pk>/delete/', views.WD_DeleteView.as_view(), name='wd_delete'),
    path('workout_day/<int:pk>/exercises/', views.WD_DetailView.as_view(), name='wd_detail'),

    # TODO: change this to have workout_day's id at the beginning of the url
    path('exercise/<int:wd_id>/new/', views.E_CreateView.as_view(), name='e_create'),
    path('exercise/<int:pk>/update/', views.E_UpdateView.as_view(), name='e_update'),
    path('exercise/<int:pk>/delete', views.E_DeleteView.as_view(), name='e_delete'),
    path('exercise/<int:pk>/sets/', views.E_DetailView.as_view(), name='e_detail'),

    path('exercise/<int:ex_id>/set/new/', views.S_CreateView.as_view(), name='s_create'),
    path('exercise/<int:ex_id>/set/<int:pk>/update/', views.S_UpdateView.as_view(), name='s_update'),
    path('exercise/<int:ex_id>/set/<int:pk>/delete/', views.S_DeleteView.as_view(), name='s_delete'),
    path('exercise/<int:ex_id>/set/<int:pk>/<int:set_number>/', views.S_DetailView.as_view(), name='s_detail'),
]