from django.db import models

# Create your models here.

class CategoryGirls(models.Model):
    title = models.CharField(max_length=25,blank=True)
    keywords = models.CharField(max_length=150,blank=True)
    description = models.CharField(max_length=150,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 

class Girls(models.Model):
    COLOR = (
        ('1','Choco'),
        ('2','Blondinka'),
        ('3','Rijinkiy'),
        ('4','Jaydari'),
    )
    FIGURE = (
        ('1','90*60*90'),
        ('2','va boshqalar'),
    )
    first_name = models.CharField(max_length=25,blank=True)
    last_name = models.CharField(max_length=25,blank=True)
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    color = models.CharField(max_length=15,choices=COLOR,default='1')
    figure = models.CharField(max_length=20,choices=FIGURE,default='1')
    hair = models.CharField(max_length=30,blank=True)
    category = models.ForeignKey(CategoryGirls,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name 



    