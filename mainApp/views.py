# -*- coding : utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.context import Context, RequestContext
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def main(request):
	a = 'Mentoring Project Start!'
	variables = RequestContext(request, {
		'status' : a,
	})

	return render_to_response('main.html', variables)
