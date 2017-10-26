from models import Profile, Post
from rest_framework import serializers

# look at HyperlinkedModelSerializer
class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		#fields = ('name', 'description')
		fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		#fields = ('content', 'pub_date')
		fields = '__all__'