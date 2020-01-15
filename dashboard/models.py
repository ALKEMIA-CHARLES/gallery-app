from django.db import models
from pyuploadcare.dj.forms import ImageField
import pyperclip
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=25)
    category_description = models.CharField(max_length=25)


    def __str__(self):
        return self.category_name
    
    def save_catgeory(self):
        return self.save()

class Location(models.Model):
    city = models.CharField(max_length=25)
    country = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.city}, {self.country}"
    
    def save_location(self):
        return self.save()

class Images(models.Model):
    image = ImageField(manual_crop="700x700")
    image_name= models.CharField(max_length=100)
    image_descrition = models.CharField(max_length=100)
    image_category = models.ManyToManyField(Category)
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=250)

    def __str__(self):
        return self.image_name
    def save_image(self): 
        return self.save()
    def get_remote_image(self):
        if self.image_url and not self.image:
            result = request.urlretrieve(self.image_url)
        self.image.save(
                os.path.basename(self.image_url),
                File(open(result[0], 'rb'))
                )
        self.save()
    def admin_image(self):
        return '<img src="%s"/>' % self.image
    admin_image.allow_tags = True
    @classmethod
    def copy_url(cls,id):
        image = cls.objects.get(id=id)
        pyperclip.copy(image.image.url)
    @classmethod
    def delete_image(cls,id):
        return cls.objects.filter(id=id).delete() 
    @classmethod
    def show_images(cls):
        return cls.objects.order_by("post_date")[::1]
    @classmethod
    def filter_by_location(cls,id):
        return cls.objects.filter(location__id=id)
    @classmethod
    def get_image_by_id(cls, id):
        return cls.objects.filter(id=id)[0]
    @classmethod
    def search_image_by_category(cls,search):
        return cls.objects.filter(categories=search)