from rest_framework.views import APIView, Response, status
from ..serializers.user_serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_serializer = UserSerializer(instance=user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)