from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm
from .models import Author
from .models import Post
from .models import Category
from .models import Comment
from .filters import PostFilter

class AuthorList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Author
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'user_rating'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'author.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'author'

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class PostsList(ListView):
    model = Post
    ordering = 'time_post'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class CategoryList(ListView):
    model = Category
    ordering = 'name'
    template_name = 'category.html'
    context_object_name = 'category'

class CommentList(ListView):
    model = Comment
    ordering = 'com_rating'
    template_name = 'comment.html'
    context_object_name = 'comment'

class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        vibor = form.save(commit=False)
        vibor.vibor = 2
        return super().form_valid(form)

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        vibor = form.save(commit=False)
        vibor.vibor = 1
        return super().form_valid(form)

class NewsUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        vibor = form.save(commit=False)
        vibor.vibor = 2
        return super().form_valid(form)

class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        vibor = form.save(commit=False)
        vibor.vibor = 1
        return super().form_valid(form)

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_list')
