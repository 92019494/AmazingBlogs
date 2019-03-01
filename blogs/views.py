from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from.models import Author,Post

def about(request):

    return render(request, 'about.html', )


def posts(request): # this is the home view

    try:
        posts = Post.objects.all().order_by('-publish_date')
    except Post.DoesNotExist:
        raise Http404('Posts not found')

    return render(request, 'posts.html', {'posts': posts})

def post_detail(request, id):

    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404('Post not found')

    return render(request, 'post_detail.html', {'post': post})

def authors(request):

    try:
        authors = Author.objects.all()
    except Post.DoesNotExist:
        raise Http404('Authors not found')

    return render(request, 'authors.html', {'authors': authors})

def author_detail(request, id):

    try:
        author = Author.objects.get(id=id)
        posts = Post.objects.all().order_by('-publish_date')
    except Post.DoesNotExist:
        raise Http404('Author not found')

    return render(request, 'author_detail.html', {'author': author, 'posts': posts})



from django.views import generic

class PostListView(generic.ListView):
    model = Post
    template_name = 'posts.html'

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'authors.html'
