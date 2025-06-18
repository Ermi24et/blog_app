from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    DesignListView,
    BusinessListView,
    LifestyleListView,
    TravelListView,
    TechnologyListView, 
    PostDetailView,
    PostHomeListView,
    PostListView,
    PostUserListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path("", PostHomeListView.as_view(), name='home'),
    path("posts/", PostListView.as_view(), name='posts'),
    path("posts/user/", PostUserListView.as_view(), name='user-posts'),
    path("posts/<int:pk>/", PostDetailView.as_view(), name='post-detail'),
    path("posts/new/", PostCreateView.as_view(), name='post-create'),
    path("posts/<int:pk>/update/", PostUpdateView.as_view(), name='post-update'),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name='post-delete'),
    path("technology/", TechnologyListView.as_view(), name='technology'),
    path("design/", DesignListView.as_view(), name='design'),
    path("business/", BusinessListView.as_view(), name='business'),
    path("lifestyle/", LifestyleListView.as_view(), name='lifestyle'),
    path("travel/", TravelListView.as_view(), name='travel'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
]