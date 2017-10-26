# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Profile(models.Model):
	name = models.CharField(max_length=75)
	description = models.TextField()

	def __str__(self):
		return self.name

class Post(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="children")
	content = models.TextField()
	pub_date = models.DateTimeField('date published', editable=False, auto_now_add=True)

	def __str__(self):
		return self.content