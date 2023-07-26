from .serializers import RegistrationSerializer
from .models import Registration
from rest_framework import generics

class UserReg(generics.CreateAPIView):
    queryset=Registration.objects.all()
    serializer_class=RegistrationSerializer