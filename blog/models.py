from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'portofolio/images/',  default=" ")
    def __str__(self):
        return self.name

class Blogs(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status = 'published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length = 200)
    category = models.ForeignKey(Category, on_delete = models.PROTECT, default = 1)
    slug = models.SlugField(max_length = 250, unique_for_date = 'publish')
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog_posts', default = True)
    description = models.TextField()
    image = models.ImageField(upload_to = 'portfolio/images/')
    publish = models.DateTimeField(default = timezone.now)
    status = models.CharField(max_length = 10, choices = options, default = 'draft')

    objects = models.Manager()
    newmanager = NewManager()

    def get_absolute_url(self):
        return reverse('blog:blog-content', args = [self.slug])
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

#comment system model
class Comment(MPTTModel):
    post = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name = "comments")
    parent = TreeForeignKey('self', on_delete = models.CASCADE, null = True, blank = True, related_name = 'children')
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    message = models.TextField()
    publish = models.DateTimeField(auto_now_add = True)
    status = models.BooleanField(default = True)

    class MPTTPMeta:
        order_insertion_by = ['publish']

    def __str__(self):
        return f"Comment by: {self.name}"

#category system models
