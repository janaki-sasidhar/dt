from rest_framework import serializers
from .models import Notes
# from django.contrib.auth.models import User
from users.models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id','title','description']



class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ( 'password', 'password2', 'email', 'first_name', 'last_name','realm')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'realm':{'required':True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        request = self.context.get('request')
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            realm = validated_data['realm']
        )


        user.set_password(validated_data['password'])
        user.save()

        return user





class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['realm'] = user.realm
        if user.id:
            customuser = CustomUser.objects.get(id=user.id)
            if not customuser.logged_in_firsttime:
                customuser.logged_in_firsttime = True
                customuser.save()
                print('user has logged in firsttime')

        return token