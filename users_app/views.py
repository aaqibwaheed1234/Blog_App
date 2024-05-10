from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, DeleteView, UpdateView, View, DetailView, FormView
from .models import Post, Comment, Like
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .forms import CommentForm, ProfilePictureForm
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

class LogoutView(LogoutView):
    next_page = '/login/'

class BaseView(LoginRequiredMixin, CreateView): 
    model = Post
    template_name = 'base.html'
    fields = ['title', 'slug', 'intro', 'body']

class GetPosts(ListView):
    model=Post
    template_name='frontpage.html'
    context_object_name= 'posts_list'

class BlogHomeView(TemplateView):
    template_name='home.html'

class CreatePost(CreateView):
    model=Post
    template_name="home.html"
    fields=['title', 'body', 'image']
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    # def get(self, request):
    #     return render(request, 'detail.html')
    # def post(self, request, id):
    #     post=Post.objects.get()


class PostDetail(TemplateView):
    def get(self, request, id):
        post = Post.objects.get(pk=id)
        form=CommentForm()
        comments = post.comments.all()
        comment = Comment()
        username=comment.user = request.user
        # print(username)
        return render(request, "detail.html", {"post": post, 'form':form, 'comments':comments, 'username': username})

class DeletePost(DeleteView):
    model=Post
    success_url=reverse_lazy('posts')
    template_name='confirm_delete.html'


class UpdatePost(UpdateView):
    model = Post
    fields = ['title', 'intro', 'body']
    template_name = 'update_post.html' 
    success_url=reverse_lazy('posts')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
    
# class StoreComment(CreateView):
#     model = Comment
#     fields=['name','email','body']
#     template_name = 'detail.html'
#     context_object_name = 'comments'

#     def post(self, request, *args, **kwargs):
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

class StoreComment(View):
    def get(self, request):
        return render(request, 'detail.html', {'form': CommentForm()})

    def post(self, request):
        post_id = request.POST.get('post_id')
        # print(post_id)
        post = get_object_or_404(Post, id=post_id)
        comment = Comment()
        comment.body=request.POST.get("body")
        comment.post = post
        username=comment.user = request.user
        # print(username)
        comment.save()
        comments = post.comments.all()
        return render(request, 'detail.html', {'post': post, 'form': CommentForm(), 'comments': comments, 'username': username})

class DeleteComment(DeleteView):
    model=Comment
    template_name='comment_confirm_delete.html'
    context_object_name='object'

    def get_success_url(self):
        post_id = self.object.post.id
        return reverse_lazy('post-details', kwargs={'id': post_id})


class LikePost(View):
    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('pk')
        # print(post_id)
        post = get_object_or_404(Post, pk=post_id)
        if Like.objects.filter(post=post, user=request.user).exists():
            return JsonResponse({'message': 'You have already liked this post'}, status=400)
        like = Like.objects.create(post=post, user=request.user)
        return JsonResponse({'success': True})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        # Set is_liked_by_current_user for each post in the context
        for post in context['posts']:
            post.is_liked_by_current_user = Like.objects.filter(post=post, user=self.request.user).exists()
        return context


class ProfileView(LoginRequiredMixin, FormView):
    template_name = 'user_profile.html'
    form_class = ProfilePictureForm
    success_url = reverse_lazy('user-profile')

    def get(self, request):
        return render(request, 'user_profile.html', {'user': request.user})
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.instance = request.user
            form.save()
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)


# class ProfileView(FormView):
#     template_name = 'user_profile.html'
#     form_class = ProfilePictureForm
#     success_url = reverse_lazy('posts')

#     def get(self, request):
#         return render(request, 'user_profile.html')
    
#     def post(self, request, *args, **kwargs):
#     #     picture=request.FILES.get('image')
#     #     return render(request, 'user_profile.html', {'picture': picture})
#         form = self.get_form()
#         if form.is_valid():
#             form.save()
#             return redirect(self.get_success_url())
#         else:
#             return self.form_invalid(form)
        
    