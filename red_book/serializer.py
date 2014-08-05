__author__ = 'lucky'
from django.forms import widgets
from rest_framework import serializers
from models import Question, LANGUAGE_CHOICES, STYLE_CHOICES

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields=('id', 'title', 'code', 'linenos', 'language', 'style')
    # pk=serializers.Field()# fiedl is an untyped read-only field
    #
    # title=serializers.CharField(required=False,
    #                             max_length=100)
    # code=serializers.CharField(widget=widgets.Textarea,
    #                            max_length=100000)
    # linenos=serializers.BooleanField(required=False)
    #
    # language=serializers.ChoiceField(choices=LANGUAGE_CHOICES,
    #                                  default='python')
    #
    # style= serializers.ChoiceField(choices=STYLE_CHOICES,
    #                                default='friendly')
    #
    # def restore_object(self, attrs, instance=None):
    #     """
    #
    #     """
    #     if instance:
    #         instance.title=attrs.get('title', instance.title)
    #         instance.code=attrs.get('code', instance.code)
    #         instance.linenos=attrs.get('linenos', instance.linenos)
    #         instance.language=attrs.get('language', instance.language)
    #         instance.style=attrs.get('style', instance.style)
    #
    #         return instance
    #
    #     return Question(**attrs)






