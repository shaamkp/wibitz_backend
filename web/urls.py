from django.urls import path
from django.urls.conf import include
from web.models import Contact
from web.views import index, subscribe, contact, product
from django.conf import settings
from django.conf.urls.static import static


app_name = "web"


urlpatterns = [
    path("",index,name="index"),
    path("subscribe/",subscribe,name="subscribe"),
    path("contact/",contact,name="contact"),
    path("product/<int:pk>/",product,name="product")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

