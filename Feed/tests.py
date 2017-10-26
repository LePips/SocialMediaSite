# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.utils import timezone
from Feed.models import Profile, Post

class PostTests(TestCase):
	def test_post_content_is_blank(self):
		fake_profile = Profile()
		fake_profile.name = "Test Name"
		fake_profile.save()

		fake_post = Post()
		fake_post.profile = Profile.objects.get(name='Test Name')
		fake_post.content = ''
		
		self.assertIs(bool(fake_post.content), False)

	def test_post_content_is_only_spaces(self):
		fake_profile = Profile()
		fake_profile.name = "Test Name"
		fake_profile.save()

		fake_post = Post()
		fake_post.profile = Profile.objects.get(name='Test Name')
		fake_post.content = '    '
		
		self.assertIs(bool(fake_post.content.strip()), False)