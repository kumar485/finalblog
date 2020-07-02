
from django.urls import path,include
from .views import PostListView,PostDetailView,PostCreateView,PostUpdaeView,PostDeleteView
urlpatterns = [
    # path('posts',views.home),
    path('posts',PostListView.as_view(),name='posts'),
    path('postdetail/<int:pk>/',PostDetailView.as_view(),name='postsdetail'),
    path('postupdate/<int:pk>/',PostUpdaeView.as_view(),name='postupdate'),
    path('postdelete/<int:pk>/',PostDeleteView.as_view(),name='postdelete'),
    path('postcreate/',PostCreateView.as_view()),
]