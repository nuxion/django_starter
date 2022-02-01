from django.urls import reverse

def get_menu(request):

    return {
        "menu": [
            { 
                "name": "Home", 
                "url": reverse("index"),
            },
        ]
    }