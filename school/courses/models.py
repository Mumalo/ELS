from django.db import models
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
from .fields import OrderField
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

class Subject(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Course(models.Model):
    creator = models.ForeignKey(User,
                                related_name='Courses_created', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='Courses', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(User, related_name='courses_joined', blank=True)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        ordering = ['order']

    def __str__(self):
        return '{}. {}'.format(self.order, self.title)

    def __str__(self):
        return self.title

class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, limit_choices_to={'model__in': ('Image',
                                                                                 'Text',
                                                                                  'Video',
                                                                                  'File')}, on_delete=models.CASCADE)
    object_id = models.IntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']

class BaseItem(models.Model):
    creator = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def render(self):
        return render_to_string('courses/content/{}.html'.format(self._meta.model_name), {'item': self})

class Image(BaseItem):
    file = models.ImageField(upload_to='files')

class Text(BaseItem):
    content = models.TextField()

class Video(BaseItem):
    url = models.URLField()

class File(BaseItem):
    file = models.FileField(upload_to='images')






# Create your models here.
