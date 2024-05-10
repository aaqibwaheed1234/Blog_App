from .views import SignUpView, CustomLoginView, GetPosts,BaseView,BlogHomeView, CreatePost,PostDetail, StoreComment, DeletePost, UpdatePost, DeleteComment, ProfileView ,LikePost
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', BaseView.as_view(), name='base'), 
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLoginView.as_view(), name='logout'),

    path('posts/',GetPosts.as_view(),name='posts'),
    path('home/',BlogHomeView.as_view(), name='home'),
    path('create-post/',CreatePost.as_view(), name='create-post'),
    path('post/<int:id>/',PostDetail.as_view(), name='post-details'),
    path('post/<int:pk>/delete/', DeletePost.as_view(),name='delete-post'),
    path('post/<int:pk>/update/', UpdatePost.as_view(), name='update-post'),
    # path('<slug:slug>/',PostDetail.as_view(), name='post-details'),

    path('store-comment/', StoreComment.as_view(), name='store-comment'),
    path('delete-comment/<int:pk>/',DeleteComment.as_view(), name='delete-comment'),
    path('like-post/<int:pk>/',LikePost.as_view(), name='like-post'),

    path('user-profile/', ProfileView.as_view(), name='user-profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

