from django.contrib.auth.models import User
from user.models import (PhoneNumbers, Role, Profile, UserManagement, ResetPassword)
from django.conf import settings
# from realtime_chatapp.settings import MEDIA_ROOT
from django.core.mail import send_mail

from knox.models import AuthToken
from datetime import datetime, timedelta
from random import randint

def add_update_user(user_info):
    user = None
    data = {}
    data["email"] = "Email does not exist"
    data["user"] = None
    phone_obj = None


    try:
        user = User.objects.get(username=user_info["username"])
        #user = User.objects.get(username=user_info["email"]) (check later)
        user.first_name = user_info["name"]
        user.save()
    except Exception as e:
        print("User doesn't exist")
    
    username_email = None

    try:
        username_email = User.objects.get(username=user_info["email"])
        
    except Exception as e:
        print("User doesn't exist")
    
    user_email = None
    
    try:
        user_email = User.objects.get(email=user_info["email"])
        
    except Exception as e:
        print("User doesn't exist")
    
    try: 
        phone_obj = PhoneNumbers.objects.get(phone= user_info["phone_number"])
    
    except Exception as e: 
        print("Phone does not exist")

    
    if username_email or user_email or phone_obj:

        data["email"] = "Email/Phone already exists"
        data["is_registered"] = True

    else:

        if not user:
            try:
                user = User.objects.create_user(user_info["username"],
                    user_info["email"],
                    user_info["password"])
                user.first_name = user_info["name"]
                user.save()
                print(user)
            except Exception as e:
                print("User save failed %s" % str(e))

        if user:
            profile = None
            try:
                profile = Profile.objects.get(user=user)
            except Exception as e:
                print("Profile not found")

            if not profile:
                try:
                    role = Role.objects.get(shortcode=user_info["role"])
                    
                    # co_cen = CoachingCenter.objects.get(shortcode=user_info["coaching_center"])
                    
                    profile = Profile(user=user, role=role,
                        is_active=True)
                                        
                    profile.save()
                    
                except Exception as e:
                    print("Profile not saved %s" % str(e))

            else:
                try:
                    if "email" in user_info:
                        user.email = user_info["email"]
                        user.save()

                    profile = Profile.objects.get(user=user)
                    # if "coaching_center" in user_info:
                    #     co_cen = CoachingCenter.objects.get(shortcode=user_info["coaching_center"])
                    #     profile.coaching_center = co_cen

                    if "is_active" in user_info:
                        profile.is_active = user_info["is_active"]
                        profile.save()
                except Exception as e:
                    print(str(e))
        
            if not phone_obj: 
                
                
                try: 
                    phone_number = PhoneNumbers()
                    phone_number.user = user
                    phone_number.phone = user_info["phone_number"]
                    phone_number.is_active = True
                    phone_number.is_verified = True

                    phone_number.save()
                
                except Exception as e: 
                    print(str(e))
    
        data["user"] = user
        data["is_registered"] = False


        # send email to counsellor and admin 
        # if user:

        #     if user_info["phone_number"] and user_info["email"]:
               
        #         subject = 'SosinIAS Academy'
        #         message = 'Dear Counselling, '+' We received a contact request from a student and details are '+'name:'+user.first_name+ ' Phone:' + user_info["phone_number"]+' email: '+user_info["email"]+'.'
        #         email_from = settings.EMAIL_HOST_USER
        
        #         recipient_list = ["info@sosinias.com ","counselor2@sosinclasses.com"]

        #         try:
        #             send_mail( subject, message, email_from, recipient_list )
        #         except Exception as e:
        #             print(str(e))
    return data


#--------------------------------------------------------------------------------------------


def set_userlogout(user_info):
    data = {}
    user = None
    success = False
    try:
        user = User.objects.get(username=user_info["username"])
    except:
        pass
    
    
    if user:
        user_manager = None
        try:
            user_manager = UserManagement.objects.get(logged_in=True,
                    user=user, device_token=user_info["device_token"] )
        except Exception as e:
            print(str(e))

        
        if user_manager:
            try:
                user_manager.logged_in = False
                user_manager.save()
                success = True
            except Exception as e:
                print(str(e))
        
        if success:
            user_token = AuthToken.objects.get(user= user)
            user_token.delete()

    data["success"] = success

    return data

def set_logoutall(user_info):
    data = {}
    success = False
    user = None
    try:
        user = User.objects.get(username=user_info["username"])
    except:
        pass

    if user:
        try:
            for x in UserManagement.objects.filter(user=user, logged_in=True):
                x.logged_in = False
                x.save()
            success = True
        except Exception as e:
            print(str(e))

        if success: 
            user_token = AuthToken.objects.filter(user= user)
            for x in user_token:
                x.delete()
        data["success"] = success

    return data

#-----------------------------------------------------------------------------------



def reset_password(reset_info):
    success = False
    user = None
    username = None
    '''try:
        user = User.objects.get(username=reset_info["phone_number"])
        username = user.username
    except Exception as e:
        print(str(e))

    if not user:
        try:
            user = User.objects.get(email=reset_info["email"])
        except Exception as e:
            print(str(e))'''
    
    try:
        username = User.objects.get(username=reset_info["username"])    
    except Exception as e:
        print(str(e))
    
    if username:#user:
        otp = None
        reset = None
        '''try:
            reset = ResetPassword.objects.get(user=user, created__gte=(datetime.now() - timedelta(days=1)))
        except Exception as e:
            print(str(e))'''
        
        try: 
            reset = ResetPassword.objects.get(user=username, created__gte=(datetime.now() - timedelta(days=1)))
        except Exception as e:
            print(str(e))

        if not reset:
            try:
                otp = str(randint(100000, 999999))
                reset = ResetPassword(user=username, otp=otp)
                reset.save()
                success = True
            except Exception as e:
                print(str(e))
        else:
            otp = reset.otp
            success = True

        try:
            subject = 'Sosin Classes - Reset Password'
            message = 'Dear '+username.first_name+', Your OTP for resetting password is '+otp+' Please email to support@sosinclasses.com for any queries - Technical Support Team.'
            email_from = settings.EMAIL_HOST_USER
            
            recipient_list = [username.email,]

            send_mail( subject, message, email_from, recipient_list )
        except Exception as e:
            print(str(e))

    return success, username