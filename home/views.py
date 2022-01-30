from django.http import HttpResponse
from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken


def get_user_text(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.email
    return username


def index(request):
    user = get_user_text(request)
    if user:
        tkn = RefreshToken.for_user(request.user)
        rsp = f"Hello, {user}. You're at the index."
        # rsp =  HttpResponse(f"Hello, {user}. You're at the polls index.")
        # rsp.set_cookie("X-AUTH-TKN", str(tkn.access_token) , max_age=300)
        # rsp.set_cookie("X-AUTH-REFRESH",str(tkn) , max_age=1440)
    else:
        rsp = "Hello, you're at the index"

    return render(request, "home/index.html", {"message": rsp})
