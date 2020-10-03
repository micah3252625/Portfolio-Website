from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .models import Blogs, Category
from .forms import NewCommentForm
from django.views.generic import ListView



# Create your views here.
def blog_thmb(request):
    blogs_title = Blogs.newmanager.all()[:6]
    return render(request, 'blog/blog.html', {'blogs_title': blogs_title})

def blog_detail(request, post):

    post = get_object_or_404(Blogs, slug = post, status = 'published')
    comments = post.comments.filter(status = True)
    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit = False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect('../blog-content|' + post.slug)
    else:
        comment_form = NewCommentForm()
    return render(
        request,
        'blog/blog-detail.html',
        {
            'post':post,
            'comments':user_comment,
            'comments': comments,
            'comment_form':comment_form
        }
    )

class CatListView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts':Blogs.objects.filter(category__name = self.kwargs['category']).filter(status = 'published')
        }
        return content

def category_list(request):
    category_list = Category.objects.exclude(name = 'default')
    context = {
        'category_list': category_list,
    }
    return context
