# 폼즈를 가져옴
from dataclasses import field
from django import forms
# movies/models.py에 있는 모델인 Movie랑 Comment를 가져옴
from .models import Movie, Comment

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('title', 'description',)
        # 외래키 아닌 것만 가져왔음

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)
        # 여기도 FKey아닌 것만 가져옴