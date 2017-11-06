from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404


def post_home(request):
	context = {
	"greeting": "HEllow yaman",
	"ending": "GoodBye yaman",
	"number": "random.randint(1.20)",
	"me": request.user

	}
	return render(request, 'yaman.html', context)


def post_list(request):
	objects = Post.objects.all()
	context = {
		"post_items": objects,
	}
	return render(request, "list.html", context)

def post_detail(request, post_id):

	"""
	item = Post.objects.get(id=3) 
	for more handelling the error
	Item = get_object_or_404.get(post, id=1000)

	"""

	Item = get_object_or_404(Post, id=post_id)

	context = {
		"item": Item,
	}
	return render(request, "detail.html", context)