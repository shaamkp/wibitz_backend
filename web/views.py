import json
from django import forms
from django.http.response import HttpResponse
from django.urls import reverse
from django.shortcuts import render , get_object_or_404
from django.http.response import HttpResponse
from web.models import Blog, Contact,  MarketingFeature, Product, Subscribe, Costumer,Feature,VideoBlog, Testimonial
from web.forms import ContactForm


def index(request):
    costumer = Costumer.objects.all()
    white_logo = Costumer.objects.all()[:4]
    features = Feature.objects.all()
    videoBlog = VideoBlog.objects.all()
    testimonial = Testimonial.objects.all()
    marketingFeature = MarketingFeature.objects.all()
    product = Product.objects.all()
    blog_post = Blog.objects.filter(content_type = "blog_post")
    webinar = Blog.objects.filter(content_type = "webinar")
    project = Blog.objects.filter(content_type = "project")

    form = ContactForm()

    context = {
        "costumer" : costumer,
        "features" : features,
        "videoblog" : videoBlog,
        "testimonial" : testimonial,
        "markeingfeature" : marketingFeature,
        "product" : product,
        "blog_post" : blog_post,
        "webinar" : webinar,
        "project" : project,
        "form"    : form,
        "white_logo" : white_logo
    }

    return render(request , "index.html",context=context)


def subscribe(request):
    email = request.POST.get("email")

    if not Subscribe.objects.filter(email = email).exists():


        Subscribe.objects.create(
        email = email,
        )

        response_data = {
            "status" : "success",
            "title" : "You Successfully Registered",
            "message" : "You subscribe to our communitty successfully."
        }
    else:
        response_data = {
            "status" : "error",
            "title" : "You are already Subscribed",
            "message" : "You are already a member."
        }

    return HttpResponse(json.dumps(response_data), content_type = "application/javascript")


def contact(request):
    form =ContactForm(request.POST)
    if form.is_valid():
        form.save()

        response_data = {
            "status" : "success",
            "title" : "You Successfully Registered",
            "message" : "You subscribe to our communitty successfully."
        }
    else:
        response_data = {
            "status" : "error",
            "title" : "You are already Subscribed",
            "message" : "You are already a member."
        }

    return HttpResponse(json.dumps(response_data), content_type = "application/javascript")


def product(request,pk):
    products = get_object_or_404(Product.objects.filter(pk=pk))

    Costumers = Costumer.objects.filter(product=products)
    print(product)
    context={
        "products" : products,
        "Costumers" : Costumers
    }
    return render(request,"product.html",context=context)