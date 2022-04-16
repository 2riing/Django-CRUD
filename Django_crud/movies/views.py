from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_safe
from django.contrib.auth.decorators import login_required

# modles.py 에 있는 Movie클래스랑 comment클래스를 가져온다
from .models import Movie, Comment
# forms.py에 있는 MovieForm이랑 CommentForm을 가져옴
from .froms import MovieForm, CommentForm


@require_GET
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {'movies' : movies,}
    return render(request, 'movies/index.html', context)
    

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():  
            movie = form.save(commit=False) 
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = { 'form': form,}
    return render(request, 'movies/create.html', context)

@require_GET
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    form = CommentForm()
    context = {
        'movie' : movie,
        'form' : form,
    }
    return render(request, 'movies/detail.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, movie_pk):
    movie = get_object_or_404(Movie, pk= movie_pk)
    if request.user == movie.user:
        if request.method == 'POST':
            form = MovieForm(request.POST, instance = movie)
            if form.is_valid():
                movie = form.save(commit=False)
                movie.save()
                return redirect('movies:detail', movie.pk)
        else:
            form = MovieForm(instance=movie)
        context = {'form':form,}
        return render(request, 'movies/update.html', context)
    else:
        return redirect('movies:detail', movie.pk)

@login_required
@require_POST
def delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user == movie.user:
        movie.delete()
    return redirect('movies:index')
    
@login_required
@require_POST
def comments_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.movie = movie
        comment.save()
    return redirect('movies:detail', movie.pk)

@login_required
@require_POST
def comments_delete(request, movie_pk, comment_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('movies:detail', movie.pk)