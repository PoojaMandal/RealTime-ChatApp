from user.helpers import (add_update_user, set_userlogout, set_logoutall,reset_password)
from knox.models import AuthToken
from rest_framework.decorators import api_view
from realtime_chatapp.utils import convert_data
from rest_framework.response import Response

from rest_framework import generics, status
from user.serializers import LoginSerializer

def return_token(request):
    
    username = None
    knox_object = None

    token = request.META.get('HTTP_AUTHORIZATION', '')
    token = token.strip()
    if len(token) == 70:
        token = token[6:]
    
    knox_object = AuthToken.objects.filter(token_key__startswith=token[:8]).first()

    if knox_object:
        username = knox_object.user.username
    
   
    return username


@api_view(['POST'])
def createuser(request):
    data = {}
    user = None
    if request.method == "POST":
        post_data = convert_data(request.body)
        if post_data:
            username = post_data.get("username", None)
            name = post_data.get("name", None)
            email = post_data.get("email", None)
            password = post_data.get("password", None)
            phone_number = post_data.get("phone_number",None)
            role = post_data.get("role", None)
            coaching_center = post_data.get("coaching_center",None)
            is_active = post_data.get("is_active", None)

            #department = post_data.get("department", None)
            #manager = post_data.get("manager", None)

            print("----------------------------------")
            print(phone_number)
            print("----------------------------------")

            data = add_update_user({
                "username":username,
                "name":name,
                "password": password,
                "phone_number":phone_number,
                "role":role,
                "email":email,
                "coaching_center":coaching_center,
                "is_active": is_active,
                })

            print(data)
            user = data["user"]
            #user
            if user:
                data["user"] = {
                        "username": user.username,
                        "user_id":user.id,
                        "name":user.first_name
                        }
                data["success"] = True
                data["email"] = data["email"]
            else:
                data["user"] = None
                data["success"] = False
                data["error"] = "User not created"
                data["email"] = data["email"]
        else:
            data["success"] = False
            data["error"] = "Invalid data"

    return Response(data)


#-------------------------------------------------------------------------------------


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        return Response({
			#'user': UserSerializer(user).data,
			'token': AuthToken.objects.create(user)[1]
		})

#------------------------------------------------------------------------------


@api_view(['POST'])
def logout(request):
    data ={}
    data["success"] = False
    username = return_token(request)
    #username = Token.objects.get(key=token)
    #username = username.user

    if request.method =="POST":
        post_data = convert_data(request.body)
        if post_data:
            #username = post_data.get("username", None)
            device_token = post_data.get("device_token", None)

            data = set_userlogout({"username": username,
                "device_token": device_token})

    return Response(data)

@api_view(['POST'])
def logoutall(request):
    data = {}
    username = return_token(request)
    #username = Token.objects.get(key=token)
    #username = username.user

    if request.method == "POST":
        post_data = convert_data(request.body)
        if post_data:
            #username = post_data.get("username", None)
            success = set_logoutall({"username":username})
            data["success"] = success
    return Response(data)


#-----------------------------------------------------------------------------

@api_view(['POST'])
def resetpassword(request):
    data={}

        
    if request.method=="POST":
        print("below the POST ")
        post_data = convert_data(request.body)
        if post_data:
            #email = post_data.get("email", None)
            #phone_number = post_data.get("phone_number", None)
            username = post_data.get("username", None)
            '''success, username = reset_password({"email": email, 
                "phone_number": phone_number,
                "username":username})'''
            success, username = reset_password({"username":username})
                        

            #data["username"] = username
            data["success"] = success
            
    return Response(data)
