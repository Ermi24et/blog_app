from django.shortcuts import render
from .models import Category, Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# def home(request):
#     categories = Post.objects.all()
#     context = {'posts': posts}
#     return render(request, 'blog/home.html', context=context)

class PostHomeListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/home.html'

    def get_queryset(self):
        return Post.objects.all()[:4]

class PostUserListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/user_posts.html'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/posts.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'content', 'featured_image', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'content', 'featured_image', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/posts'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# def technology(request):
#     num_visits = request.session.get('num_visits', 0)
#     num_visits += 1
#     request.session['num_visits'] = num_visits

#     context = {
#         'num_visits': num_visits
#     }

#     return render(request, 'blog/technology.html', context=context)

class CategoryPostListView(PostHomeListView):
    model = Post
    slug = None

    def get_template_names(self):
        return [f'blog/{self.slug}.html']

    def get_queryset(self):
        return Post.objects.filter(slug=self.slug)

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

class TechnologyListView(CategoryPostListView):
    slug = 'technology'

class DesignListView(CategoryPostListView):
    slug = 'design'

class BusinessListView(CategoryPostListView):
    slug = 'business'

class LifestyleListView(CategoryPostListView):
    slug = 'lifestyle'

class TravelListView(CategoryPostListView):
    slug = 'travel'

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')
