# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Profile, Post


class PostInLine(admin.TabularInline):
	model = Post
	extra = 1

class ProfileAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 		{'fields': ['name']}),
		(None, 		{'fields': ['description']})
	]
	inlines = [PostInLine]

admin.site.register(Profile, ProfileAdmin)