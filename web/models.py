from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import TextField
from django.db.models.fields.files import ImageField

CONTENT_TYPE = (
    ("blog_post", "Blog Post"),
    ("webinar", "Webinar"),
    ("project", "Project")
)

COMPANY_SIZE = (
    ("1", "1-10"),
    ("2", "11-15"),
    ("3", "51-200"),
    ("4", "201-500")
)

INDUSTRY = (
    ("1", "Agriculture"),
    ("2", "Banking & Finance"),
    ("3", "Business Services & Software")
)


JOB_ROLE = (
    ("1", "C-Suite"),
    ("2", "VP"),
    )

COUNTRY = (
    ("US", "United States"),
    ("albania", "Albania"),
    )


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Costumer(models.Model):
    product = models.ForeignKey("web.product",on_delete=models.CASCADE)
    logo = models.FileField(upload_to = "costumers/")
    white_logo = models.FileField(upload_to = "costumers/",blank=True,null=True)
    

class Feature(models.Model):
    image = models.ImageField(upload_to = "features/") 
    icon = models.FileField(upload_to="features/")
    title = models.CharField(max_length=255)
    icon_background = models.CharField(max_length=255)  
    description = models.TextField(blank=True, null=True)
    testimonial_description = models.TextField(blank=True, null=True)
    testimonial_author = models.CharField(max_length=255)
    author_designation = models.CharField(max_length=255)
    testimonial_logo = models.FileField(upload_to="features/")


class VideoBlog(models.Model):
    image = models.ImageField(upload_to = "videoBlog/")
    play = models.FileField(upload_to = "videoBlog/")
    logo = models.FileField(upload_to = "videoBlog/")
    title = models.CharField(max_length=255)


class Testimonial(models.Model):
    image = models.ImageField(upload_to = "videoBlog/")
    logo = models.FileField(upload_to = "videoBlog/",null=True,blank=True)
    description = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    is_featured = models.BooleanField(blank=True, null= True)



class MarketingFeature(models.Model):
    image = models.FileField(upload_to = "marketingFeatures/")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)


class Product(models.Model):
    logo = models.FileField(upload_to = "product/")
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    background_color = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to = "product/")
    hero_image = models.FileField(upload_to = "product/hero_image")
    

class Blog(models.Model):
    image = models.FileField(upload_to = "product/")
    title = models.CharField(max_length=255)
    content_type = models.TextField(max_length=255,null=True,blank=True,choices=CONTENT_TYPE)


class Contact(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    company = models.CharField(max_length=255)
    company_size = models.CharField(max_length=255,choices=COMPANY_SIZE)
    industry = models.CharField(max_length=255,choices=INDUSTRY)    
    job_role = models.CharField(max_length=255, choices=JOB_ROLE)
    country = models.CharField(max_length=255, choices=COUNTRY)
    user_agreement = models.BooleanField(default = False)


    class Meta:
        db_table = "web_contact"
        ordering = ["-id"]

    def __str__(self):
        return self.first_name