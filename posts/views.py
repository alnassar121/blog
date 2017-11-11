from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404, redirect
from .forms import PostForm
from django.contrib import messages


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

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, "wooow nice")
		return redirect("list")
	context= {
		"form": form

	}
	return render(request, 'post_create.html', context)

def post_update(request, post_id):
	item = Post.objects.get(id=post_id)
	form = PostForm(request.POST or None, instance=item)
	if form.is_valid():
		form.save()
		messages.success(request, "you just update")
		return redirect("list")
	context= {
		"form": form,
		"item": item,

	}
	return render(request, 'post_update.html', context)

def post_delete(request, Post_id):
	Post.objects.get(id=post_id).delete()
	messages.success(request, "you just delete")
	return redirect("list")


	return render(request, 'post_create.html', context)



