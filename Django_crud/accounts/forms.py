from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationFrom(UserCreationForm):

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields
        # fields = UerCreationForm.Meta.fileds
        # 이렇게는 왜 하는지 잘 모르겠음 