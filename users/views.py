from main.views import status

from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate

from .models import User

@method_decorator(csrf_exempt, name="dispatch")
class users(View):

    def post(self, request):
        account = User()
        message = ""
        
        if not User.objects.filter(username=request.POST['username']).exists():
            try:
                account.username = request.POST['username']
                account.set_password(request.POST['password'])
                account.save()
                return JsonResponse(status(status="success", message="Success create user, you can generate API KEY now!"))
            except Exception as e:
                message = "Username and Password field is required!"
                    
        else:
            message="Username is already exist"
        return JsonResponse(status("error", message))

@method_decorator(csrf_exempt, name="dispatch")
class generateAPIKEY(View):

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            account = User.objects.get(username=username)
            apikey = account.api_key

            if apikey is None:
                account.api_key = self.generateAPIKEY()
                response = status(status="success", message="Success Generate API KEY!")
                response['apikey'] = account.api_key

                account.save()

                return JsonResponse(response, safe=False)

            response = status(status="info", message="You already have API KEY")
            response['apikey'] = apikey

            return JsonResponse(response, safe=False)

        return JsonResponse(status(status="error", message="Account is not valid!"), safe=False)

    def generateAPIKEY(self):
        import secrets
        import hashlib

        hexbytes = secrets.token_bytes(26)
        hash = hashlib.sha256()
        hash.update(hexbytes)
        return hash.hexdigest()