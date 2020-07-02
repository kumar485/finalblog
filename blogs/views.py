from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.


# def home(request):
# 	data=Post.objects.all()
# 	return render(request,'blogs/blogs.html',{'posts':data})

class PostListView(ListView):
	model=Post
	template_name='blogs/blogs.html'
	context_object_name='posts'
	ordering=['date_post']
	paginate_by=1


class PostDetailView(DetailView):
	model=Post
	template_name='blogs/post_detail.html'
	context_object_name='o'



class PostCreateView(LoginRequiredMixin,CreateView):
	model=Post
	template_name='blogs/post_form.html'
	context_object_name='form'
	fields=['title','content']

	def form_valid(self, form):
		form.instance.author= self.request.user
		return super().form_valid(form)


class PostUpdaeView(LoginRequiredMixin,UpdateView):
	model=Post
	template_name='blogs/post_form.html'
	context_object_name='form'
	fields=['title','content']

	def test_func(self):
		post=self.get_object()
		if self.request==post.author:
			return True
		return False

	def form_valid(self, form):
		form.instance.author= self.request.user
		return super().form_valid(form)



class PostDeleteView(LoginRequiredMixin,DeleteView):
	model=Post
	# template_name='blogs/delete.html'
	# context_object_name='o'
	success_url='/posts'

	
	def test_func(self):
		post=self.get_object()
		if self.request==post.author:
			return True
		return False



