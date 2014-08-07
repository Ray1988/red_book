__author__ = 'lucky'
from django.forms import widgets
from rest_framework import serializers
from models import Question, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    highlight=serializers.HyperlinkedIdentityField(view_name='question-highlight', format='html')
    class Meta:
        model=Question
        fields=('url','highlight', 'title', 'code', 'linenos', 'language', 'style', 'owner')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    questions = serializers.HyperlinkedRelatedField(view_name='question-detail', many=True)
    class Meta:
        model=User
        fields=('id', 'username', 'questions')


# class QuestionSerializer(serializers.ModelSerializer):
#     owner = serializers.Field(source='owner.username')
#     class Meta:
#         model=Question
#         fields=('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')
#
# class UserSerializer(serializers.ModelSerializer):
#     questions = serializers.PrimaryKeyRelatedField(many=True)
#     class Meta:
#         model=User
#         fields=('id', 'username', 'questions')


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






