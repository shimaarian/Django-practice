from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Post
from base64 import b64decode


def index(request):
    # return HttpResponse("index")
    return render(request,"base.html")


def posts_list(request):
    post = Post.published.all()
    context = {"post": post, }
    return render(request, "blog/list.html", context)


# approach1
def posts_detail(request, pk):
    detail = get_object_or_404(Post, id=pk, status=Post.Status.PUBLISHED)
    context = {"detail": detail}
    return render(request, "blog/detail.html", context)


# approach2
# def posts_detail(request, pk):
#     try:
#         detail = Post.published.get(id=pk)
#     except:
#         raise Http404("no post fined!")
#
#     context = {"detail": detail}
#     return render(request, "blog/detail.html", context)


def get_visit_session(request):
    visit = request.session.get('visit', 0) + 1
    request.session['visit'] = visit
    data = b64decode('eyJ2aXNpdCI6MTF9:1ov84c:qngX5Woil1EDwGGylot0OrQtche6734UOApKJ4yp-BA')
    print(data)
    return HttpResponse(f"Visit count:{request.session['visit']}")
