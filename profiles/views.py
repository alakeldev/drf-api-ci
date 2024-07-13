from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer

# Create your views here.

class ProfileList(APIView):
    def get(self,request):
        Profiles = Profile.objects.all()
        serializer = ProfileSerializer(Profiles, many=True)
        return Response(serializer.data)