from django.shortcuts import render, redirect
from .forms import PostForm, UserForm, CommentForm
from .models import Post, User, Comment
from django.http import HttpResponse


def home(req):
    return render(req, 'AppBlog/main.html')


def users(req):
    return render(req, 'AppBlog/users.html')


def posts(req):
    return render(req, 'AppBlog/posts.html')


def comments(req):
    return render(req, 'AppBlog/comments.html')

# ---------------------------------------------------------------------------- #
#                                    GET ALL                                   #
# ---------------------------------------------------------------------------- #


def get_all_posts(req):
    all_post = Post.objects.all()

    return render(req, 'AppBlog/all-post.html', {'all_post': all_post})


def get_all_users(req):
    all_user = User.objects.all()

    return render(req, 'AppBlog/all-users.html', {'all_users': all_user})


def get_all_comments(req):
    get_all_comments = Comment.objects.all()

    return render(req, 'AppBlog/all-comments.html', {'all_comments': get_all_comments})


# ---------------------------------------------------------------------------- #
#                                     FIND                                     #
# ---------------------------------------------------------------------------- #
def find_post(req):
    if req.GET['username']:
        post_to_find = req.GET['username']
        post = Post.objects.filter(username__icontains=post_to_find)

        return render(req, 'AppBlog/post-results.html', {'post': post, 'username': post_to_find})

    else:
        respuesta = "No se encontro informacion"

    return HttpResponse(respuesta)


def find_user(req):
    if req.GET['username']:
        user_to_find = req.GET['username']
        user = User.objects.filter(username__icontains=user_to_find)

        return render(req, 'AppBlog/user-results.html', {'users': user, 'username': user_to_find})

    else:
        respuesta = "No se encontro informacion"

    return HttpResponse(respuesta)


def find_comment(req):
    if req.GET['username']:
        comment_to_find = req.GET['username']
        comment = Comment.objects.filter(username__icontains=comment_to_find)

        return render(req, 'AppBlog/comment-results.html', {'comments': comment, 'username': comment_to_find})

    else:
        respuesta = "No se encontro informacion"

    return HttpResponse(respuesta)

# ---------------------------------------------------------------------------- #
#                                     FORMS                                    #
# ---------------------------------------------------------------------------- #


def post_form(request):
    if request.method == "POST":
        my_form = PostForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data
            new_post = Post(username=data['username'],
                            post_description=data['post_description'],
                            post_img=data['post_img'])

            new_post.save()
            return redirect('inicio')

    my_form = PostForm()
    return render(request, 'AppBlog/post-form.html', {'post_form': my_form})


def user_form(request):
    if request.method == "POST":
        my_form = UserForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data
            new_user = User(username=data['username'],
                            name=data['name'],
                            apellido=data['apellido'],
                            email=data['email'])

            new_user.save()
            return redirect('inicio')

    my_form = UserForm()
    return render(request, 'AppBlog/user-form.html', {'user_form': my_form})


def comment_form(request):
    if request.method == "POST":
        my_form = CommentForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data
            new_comment = Comment(username=data['username'],
                                  comment=data['comment'])

            new_comment.save()
            return redirect('inicio')

    my_form = CommentForm()
    return render(request, 'AppBlog/comment-form.html', {'comment_form': my_form})
