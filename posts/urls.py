from django.urls import path
from .views import PostListView, PostDetailView, HomePageView
from . import views 


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path("", views.HomePageView.as_view(), name='home'),

]