from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
def list(request) -> HttpResponse:

    if request.method == 'POST':
        pass
    results = Post.objects.all()
    return render(
        request=request,
        template_name="posts.html",
        context={"list_of_posts": results}
    )

def details():
    pass