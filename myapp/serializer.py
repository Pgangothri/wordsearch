from rest_framework import serializers
from .models import Paragraph,CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [ 'id','email', 'name', 'dob', 'password','created_at','modified_at']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
        email=validated_data['email'],
        name=validated_data.get('name', ''),  # Set name field if provided
        dob=validated_data.get('dob', None)   # Set dob field if provid
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



class ParagraphSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Paragraph
        fields = '__all__'

