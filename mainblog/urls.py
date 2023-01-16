from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('',HomeView.as_view(),name = 'home'),
    path('article/<int:pk>',DetailArticleView.as_view(),name = 'article-detail'),
    path('newpost/',NewPostView.as_view(),name = 'new-post'),
    path('article/<int:pk>/edit',EditPostView.as_view(),name = 'edit-post'),
    path('article/<int:pk>/delete',DeletePostView.as_view(),name = 'delete-post'),
    path('newcategory',AddCategoryView.as_view(),name = 'add-category'),
    path('category/<str:tag>',CategoryView,name = 'category'),
    path('allcategory/',AllCategoryes,name = 'all-categotyes'),
    path('like/<int:pk>',LikeView,name = 'like-post'),
    path('addcomment/<int:pk>',NewCommentView.as_view(),name = 'add-comment'),
]
