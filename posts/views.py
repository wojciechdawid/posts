from django.http import HttpResponse, Http404
from django.shortcuts import render
from .services import PostService, PostNotFound


# Create your views here.
def list(request) -> HttpResponse:

    if request.method == 'POST':
        PostService.create(
            title=request.POST.get("post_title"),
            content=request.POST.get("post_content")
        )

    results = PostService.list()
    return render(
        request=request,
        template_name="posts.html",
        context={"list_of_posts": results}
    )

def details(request, id: int) -> HttpResponse:
    try:
        result = PostService.get(id)
    except PostNotFound:
        raise Http404("Post nie istnieje")

    return render(
        request=request,
        template_name="posts_details.html",
        context={"post": result}
    )