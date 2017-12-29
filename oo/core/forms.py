from django import forms

from oo.core.models import Topic, Comment
from oo.users.models import CryptoKeypair


class TopicForm(forms.ModelForm):

    type = forms.ChoiceField(
        choices=Topic.TOPIC_TYPES,
        initial=Topic.IDEA
    )

    blockchain = forms.ChoiceField(
        choices=CryptoKeypair.KEY_TYPES,
        initial=False
    )

    class Meta:
        model = Topic
        exclude = []


class CommentForm(forms.ModelForm):

    blockchain = forms.ChoiceField(
        choices=CryptoKeypair.KEY_TYPES,
        initial=False
    )

    class Meta:
        model = Comment
        exclude = []
