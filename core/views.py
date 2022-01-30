from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets

from .models import CustomUser
from .serializers import GroupSerializer, UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def profile(request):
    username = "No user"
    if request.user.is_authenticated:
        username = request.user.email

    return HttpResponse(username)

