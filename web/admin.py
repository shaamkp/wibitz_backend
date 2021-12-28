from django.contrib import admin
from web.models import Blog, Contact, MarketingFeature, Product, Subscribe, Costumer, Feature, Testimonial,VideoBlog

admin.site.register(Subscribe)


class CostumerAdmin(admin.ModelAdmin):
    list_display = ["id","logo","white_logo"]
admin.site.register(Costumer, CostumerAdmin)


class FeatureAdmin(admin.ModelAdmin):
    list_display = ["id", "image", "icon","title", "icon_background", "description", "testimonial_description", "testimonial_author","author_designation", "testimonial_logo"]
admin.site.register(Feature,FeatureAdmin)


class VideoBlogAdmin(admin.ModelAdmin):
    list_display = ["id","play", "image",  "logo", "title"]
admin.site.register(VideoBlog,VideoBlogAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["id","image","logo","description","name","designation","company_name","is_featured"]
admin.site.register(Testimonial,TestimonialAdmin)


class MarketingFeatureAdmin(admin.ModelAdmin):
    list_display = ["id","image","title","description"]
admin.site.register(MarketingFeature,MarketingFeatureAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","logo","title","description","image"]
admin.site.register(Product,ProductAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ["id","image","title","content_type"]
admin.site.register(Blog,BlogAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "last_name", "company", "company_size", "industry", "job_role", "country", "user_agreement"]
admin.site.register(Contact,ContactAdmin)