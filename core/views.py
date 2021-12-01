from django.shortcuts import render

# Create your views here.

# --------------------------------------------------------------
# https://djoser.readthedocs.io/en/latest/settings.html?highlight=serializer#serializers
# Available endpoints
# /users/
# /users/me/
# /users/confirm/
# /users/resend_activation/
# /users/set_password/
# /users/reset_password/
# /users/reset_password_confirm/
# /users/set_username/
# /users/reset_username/
# /users/reset_username_confirm/
# /token/login/ (Token Based Authentication)
# /token/logout/ (Token Based Authentication)
# /jwt/create/ (JSON Web Token Authentication)
# /jwt/refresh/ (JSON Web Token Authentication)
# /jwt/verify/ (JSON Web Token Authentication)


# {
#     'activation': 'djoser.serializers.ActivationSerializer',
#     'password_reset': 'djoser.serializers.SendEmailResetSerializer',
#     'password_reset_confirm': 'djoser.serializers.PasswordResetConfirmSerializer',
#     'password_reset_confirm_retype': 'djoser.serializers.PasswordResetConfirmRetypeSerializer',
#     'set_password': 'djoser.serializers.SetPasswordSerializer',
#     'set_password_retype': 'djoser.serializers.SetPasswordRetypeSerializer',
#     'set_username': 'djoser.serializers.SetUsernameSerializer',
#     'set_username_retype': 'djoser.serializers.SetUsernameRetypeSerializer',
#     'username_reset': 'djoser.serializers.SendEmailResetSerializer',
#     'username_reset_confirm': 'djoser.serializers.UsernameResetConfirmSerializer',
#     'username_reset_confirm_retype': 'djoser.serializers.UsernameResetConfirmRetypeSerializer',
#     'user_create': 'djoser.serializers.UserCreateSerializer',
#     'user_create_password_retype': 'djoser.serializers.UserCreatePasswordRetypeSerializer',
#     'user_delete': 'djoser.serializers.UserDeleteSerializer',
#     'user': 'djoser.serializers.UserSerializer',
#     'current_user': 'djoser.serializers.UserSerializer',
#     'token': 'djoser.serializers.TokenSerializer',
#     'token_create': 'djoser.serializers.TokenCreateSerializer',
# }

# --------------------------------------------------------------
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
#     'ROTATE_REFRESH_TOKENS': False,
#     'BLACKLIST_AFTER_ROTATION': False,
#     'UPDATE_LAST_LOGIN': False,

#     'ALGORITHM': 'HS256',
#     'SIGNING_KEY': settings.SECRET_KEY,
#     'VERIFYING_KEY': None,
#     'AUDIENCE': None,
#     'ISSUER': None,
#     'JWK_URL': None,
#     'LEEWAY': 0,

#     'AUTH_HEADER_TYPES': ('Bearer',),
#     'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
#     'USER_ID_FIELD': 'id',
#     'USER_ID_CLAIM': 'user_id',
#     'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

#     'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
#     'TOKEN_TYPE_CLAIM': 'token_type',

#     'JTI_CLAIM': 'jti',

#     'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
#     'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
#     'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
# }



#  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzODMzODcyMywiaWF0IjoxNjM4MjUyMzIzLCJqdGkiOiI4NjlmMjM5NjFkZTk0Nzg3YTNhNjAyODYzNTU2NDVjNCIsInVzZXJfaWQiOjJ9.gDNpln7Xtx9I1Acn0FLDoRW7FlBWpyuUlLDT86QDSWc",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM4MjU1OTIzLCJpYXQiOjE2MzgyNTIzMjMsImp0aSI6ImJmOTAyOTg5YzAzZDQ2YWM5YTA2YWJmNjg2MWJkZDkzIiwidXNlcl9pZCI6Mn0.TSupEqU5Z8Jfc-TJY5EZUVb_MBT0EzGSDb2X4CltJUg"
