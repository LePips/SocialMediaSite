from models import Profile, Post
from rest_framework import serializers

# look at HyperlinkedModelSerializer
class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		children = serializers.StringRelatedField(many=True, read_only=True)

		fields = ('name', 'description', 'children')

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		#fields = ('content', 'pub_date')
		fields = '__all__'
