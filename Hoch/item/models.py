from django.db import models
from django.db import migrations
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    # Name the categories in admin
    # Individuals registers
    # Metods
    def __str__(self):
        return self.name
    '''
    Individual URL´s for models
    def get_absolute_url(self):
    return reverse('model-detail-view', args=[str(self.id)])
    '''

    # store and manage items
class Item(models.Model):
    category = models.ForeignKey(Category, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_image', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    # who created and what time was created
<<<<<<< HEAD
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
=======
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE) # (ForeignKey => um-para-muitos)
    created_at = models.DateTimeField(auto_now_add=True)
>>>>>>> a947db235090e827810d69387736356f7be46f93
