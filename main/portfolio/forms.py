from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    # Meta:modelクラスをもとにfieldを自動生成してくれる
    class Meta:
        model = Post
        # 送信されるフォームのフィールドを指定
        fields = '__all__'

        #fields = ('title', 'contents', 'url')
    def __init__(self, *args, **kwargs):

        super(PostForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({'placeholder': field.label})


# モデルフォームセット
PostFormSet = forms.modelformset_factory(
    Post, form=PostForm, extra=0
)
