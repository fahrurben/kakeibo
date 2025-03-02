from rest_framework.views import APIView, Response, status
import datetime

from ..serializers.register_serializer import RegisterSerializer
from ..serializers.user_serializer import UserSerializer
from ..models.custom_user import CustomUser

class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.pop('username')
            email = serializer.validated_data.pop('email')
            password = serializer.validated_data.pop('password')

            user = CustomUser.create(username, email, password, birthday=serializer.validated_data['birthday'])
            user_serializer = UserSerializer(instance=user)

            return Response(user_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({
                'message': serializer.errors,
                'data': None
            }, status=status.HTTP_400_BAD_REQUEST)