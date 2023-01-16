from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comments
from .forms import PostForm, EditForm, NewCommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


def CategoryView(request, tag):
    postlist = Post.objects.filter(category=tag)
    return render(request=request, template_name='category_view.html', context={'tag': tag, 'postlist': postlist})


def AllCategoryes(request):
    Categorys = Category.objects.all()
    return render(request=request, template_name='all_categoryes.html', context={'cats_list': Categorys})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'

    ## TODO: Extend html
    def get_context_data(self, *args, **kwargs):
        cats_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cats_menu'] = cats_menu
        return context


class DetailArticleView(DetailView):
    model = Post
    template_name = 'artiale_ditails.html'

    def get_context_data(self, *args, **kwargs):
        cats_menu = Category.objects.all()
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        likes_count = stuff.likes_count()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = False
        else:
            liked = True
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        context['cats_menu'] = cats_menu
        context['likes_count'] = likes_count
        context['is_liked'] = liked
        return context


class NewPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    # fields = '__all__'
    form_class = PostForm


class EditPostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = EditForm


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'add_category.html'
    success_url = reverse_lazy('home')


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

class NewCommentView(CreateView):
    model = Comments
    template_name = 'add_comment.html'
    # fields = '__all__'
    form_class = NewCommentForm
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)