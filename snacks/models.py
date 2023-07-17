from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Snack(models.Model):
    title =models.CharField(max_length=64,help_text='snack title',default='Snack')
    # Defult table by using cascading properity
    purchaser=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    # text input
    description= models.TextField(default='description')

    def __str__(self):
        return self.title
   
    
    # class Meta:
    #     ordering =['-pk']

    def get_absolute_url(self):
        return reverse('snacks_detail', args=[self.id]) 