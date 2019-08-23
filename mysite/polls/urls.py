from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('select_board/', views.SelectBoard, name='select'),
    path('gen_board/', views.GenBoard, name = 'gen_board'),
]