from django import forms

from .models import Post
from .models import PostActivity
#from .models import User
from .models import Login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    # Meta:modelクラスをもとにfieldを自動生成してくれる
    class Meta:
        managed = True
        model = Post
        # 送信されるフォームのフィールドを指定
        fields = '__all__'

        #fields = ('title', 'contents', 'url')
    def __init__(self, *args, **kwargs):

        super(PostForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({'placeholder': field.label})

class PostActivityForm(forms.ModelForm):
    class Meta:
        model = PostActivity
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super(PostActivityForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({'placeholder': field.label})

class UserForm(UserCreationForm):
    class Meta:
        model = User
        #fields = '__all__'
        fields = ('username', 'password1')

    def __init__(self, *args, **kwargs):

        super(UserForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({'placeholder': field.label})
            field.widget.attrs['class'] = 'form-control'


from django.contrib.auth.forms import AuthenticationForm
class LoginForm(AuthenticationForm):
    class Meta:
        model = Login
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({'placeholder': field.label})

        self.fields['username'].initial = 'TestUser'
        self.fields['password'].render_value = True
        self.fields['password'].initial = 'test'

# モデルフォームセット
PostFormSet = forms.modelformset_factory(
    Post, form=PostForm, extra=0
)

PostActivityFormSet = forms.modelformset_factory(
    PostActivity, form=PostActivityForm, extra=0
)
