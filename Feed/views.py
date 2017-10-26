# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from serializers import ProfileSerializer, PostSerializer

from .models import Profile, Post

from datetime import datetime


def feed(request):
	all_profiles = Profile.objects.all()
	all_posts = Post.objects.all().order_by('-pub_date')
	template = 'Feed/home.html'
	context = {'all_profiles': all_profiles, 'all_posts': all_posts}
	return render(request, template, context)

def profile(request, profile_id):
	if request.method == 'GET':
		# Needs work; try to delete a post that wasn't deleted
		if Profile.objects.get(pk=profile_id):
			profile = Profile.objects.get(pk=profile_id)
			all_posts = profile.children.all()
			template = 'Feed/profile.html'
			context = {'profile': profile, 'all_posts': all_posts}
			return render(request, template, context)
		else:
			print("No profile with that ID")
			return redirect('/')
	else:
		return HttpResponse("<p>It's broken</p>")

	# Eventually make a POST for making/deleting profiles

def post(request):
	if request.method == 'POST':
		content = request.POST['content']

		if not bool(content):
			print("Text is empty")
			return redirect('/')
		elif not bool(content.strip()):
			print("Text is empty")
			return redirect('/')
		else:
			# Gets and associates the post with the Ethan profile
			profile = Profile.objects.get(pk=2)
			post = Post()
			post.profile = profile
			post.content = content
			post.pub_date = timezone.now()

			post.save()

			print(post.content)
			return redirect('/')
	else:
		return HttpResponse("<p>It's broken</p>")

def delete(request, post_id):
	if request.method == 'POST':
		# Needs work; try to delete a post that wasn't deleted
		if Post.objects.get(pk=post_id):
			post_to_delete = Post.objects.get(pk=post_id)
			post_to_delete.delete()
			return redirect('/')
		else:
			return redirect('/')
	else:
		return HttpResponse("<p>It's broken</p>")

def api(request):
	template = template = 'Feed/api.html'
	return render(request, template)

class PostList(APIView):
	authentication_classes = (SessionAuthentication, TokenAuthentication)
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		posts = Post.objects.all()
		serializer = PostSerializer(posts, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class ProfileList(APIView):
	authentication_classes = (SessionAuthentication, TokenAuthentication)
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		profiles = Profile.objects.all()
		serializer = ProfileSerializer(profiles, many=True)
		return Response(serializer.data)

	def post(self):
		pass
		