from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.apps import apps
from django.core import serializers
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Q

from .models import Article
from users.models import User
from main.views import status, createJsonResponse, createQuery

# Create your views here.

@method_decorator(csrf_exempt, name="dispatch")
class index(View):
    def get(self, request, *args, **kwargs):

        data = Article.objects.all()
        if data.count()==0:
            return JsonResponse(status(status="info", message="Article is empty!"))
        return JsonResponse(createJsonResponse(data), safe=False)
    def post(self, request, *args, **kwargs):
        return JsonResponse(status(status="error", message="Method not valid!"))

@method_decorator(csrf_exempt, name="dispatch")
class addPost(View):
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            article = Article()
            data = request.POST

            try:
                users = User.objects.get(api_key=data['apikey'])

                article.title=data['title']
                article.description=data['desc']
                article.author=users

                article.save()

            except Exception as e:
                return JsonResponse(status(status="error", message=f"Data {e} not found!"))

            return JsonResponse(status(status="ok", message="Success Upload Article"))
    def get(self, request, *args, **kwargs):
        return JsonResponse(status(status="error", message="Method not valid!"))

@method_decorator(csrf_exempt, name="dispatch")
class updatePost(View):
    def post(self, request, *args, **kwargs):
        from django.utils import timezone

        if request.method == "POST":
            
            try:
                id = request.GET['id']
                data = Article.objects.get(pk=id)
                body = request.POST
                
                users = User.objects.get(api_key=body['apikey'])
                if users is not None:        
                    if users.api_key == data.author.api_key:
                        data.title = body['title']
                        data.description = body['desc']

                        data.save()
                        return JsonResponse(status(status="success", message="Success Update Article"), safe=False)

                    return JsonResponse(status(status="error", message="You are not the author!"), safe=False)

                return JsonResponse(status(status="error", message="Your API KEY is invalid!"), safe=False)
            except Exception as e:
                return JsonResponse(status(status="error", message=f"Data {e} not found!"))
    def get(self, request, *args, **kwargs):
        return JsonResponse(status(status="error", message="Method not valid!"))

def viewPost(request):
    query = createQuery(request)

    data = Article.objects.filter(query).all()

    if data.count()==0:
        return JsonResponse(status(status="info", message="Article is empty!"), safe=False)
    return JsonResponse(createJsonResponse(data), safe=False)

def viewUserPost(request, user):
    if (User.objects.filter(username=user).exists()):
        try:
            user = User.objects.get(username=user).pk
            query = createQuery(request, user=user)

            data = Article.objects.filter(query, author=user).all()
            if data.count()==0:
                return JsonResponse(status(status="info", message="Article is empty!"), safe=False)
            return JsonResponse(createJsonResponse(data), safe=False)
        except ValueError as e:
            return JsonResponse(status(status="error", message="Parameter invalid, Please input it Correctly!"))

@method_decorator(csrf_exempt, name="dispatch")
class deletePost(View):
    def post(self, request, *args, **kwargs):
        try:
            id = request.GET['id']
            data = Article.objects.get(pk=id)
            body = request.POST
            try:
                users = User.objects.get(api_key=body['apikey'])
                if users is not None:
                    if users.api_key == data.author.api_key:
                        data.delete()
                        return JsonResponse(status(status="success", message="Success Delete Article"), safe=False)

                    return JsonResponse(status(status="error", message="You are not the author!"), safe=False)
            except:
                return JsonResponse(status(status="error", message="Your API KEY is invalid!"), safe=False)
        except Exception as e:
            return JsonResponse(status(status="error", message=f"Data {e} not found!"))
