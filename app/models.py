from django.db import models

from django.utils.text import slugify
from django.db.models.signals import pre_save

from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length= 200, unique= True)
    # created_at = models.DateTimeField(auto_now_add= True)
    # updated_at = models.DateTimeField(auto_now= True)
    
    class Meta:
        # to change the name to be displayed in admin panel
        verbose_name = 'Categorie' 
    
    def __str__(self):
        return self.name


STATUS = (
    ('draft', 'Draft'),
    ('published', 'Published')
)
    
SECTION = (
    ('Popular', 'Popular'),
    ('Recent', 'Recent'),
    ('Editors_Pick', 'Editors_Pick'),
    ('Trending', 'Trending'),
    ('Inspiration', 'Inspiration'),
    ('Latest Post', 'Latest Post')
)

class Post(models.Model):
    title = models.CharField(max_length= 250)
    slug = models.SlugField(max_length= 500, null= True, blank= True, unique= True)
    featured_image = models.ImageField(upload_to= 'images')
    author = models.CharField(max_length= 50)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    date = models.DateField(auto_now_add= True)
    content = RichTextField()
    status = models.CharField(choices= STATUS, max_length= 100)
    section = models.CharField(choices= SECTION, max_length= 100)
    main_post = models.BooleanField(default= False)
    
    def __str__(self):
        return self.title
    
    
    
class Tags(models.Model):
    name = models.CharField(max_length= 100)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.name
    

# def create_slug(instance, new_slug= None):
#     slug = slugify(instance.title)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Post.objects.filter(slug = slug).order_by('-id')
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" % (slug, qs.first().id)
#         return create_slug(instance, new_slug= new_slug)
#     return slug


# def pre_save_post_reciver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)
#     pre_save.connect(pre_save_post_reciver, Post)
    
    
