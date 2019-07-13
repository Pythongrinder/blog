from . import views
from django.urls import path
from .views import AboutPageView


urlpatterns = [
    path('', views.MainPageView.as_view(), name='home'),
    path('about/',views.AboutPageView.as_view(), name='about'),
    path('blog/',views.PostList .as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
