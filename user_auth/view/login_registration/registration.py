# # users/views.py
#
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from user_auth.serializers.login_and_registration_serializer.registration_serializer import RegisterSerializer
#
# class RegisterView(APIView):
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'Пользователь успешно зарегистрирован'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
