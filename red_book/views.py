

# Create your views here.
from django.http import HttpResponse
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


from models import Question
from django.contrib.auth.models import User
from serializer import QuestionSerializer
from serializer import UserSerializer
from permissions import IsOwnerOrReadOnly

class UserList(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    def pre_save(self, obj):
        obj.owner = self.request.user


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    def pre_save(self, obj):
        obj.owner = self.request.user

class QuestionHighlight(generics.GenericAPIView):
    queryset=Question.objects.all()
    renderer_classes=(renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        question=self.get_object()
        return Response(question.highlighted)

@api_view(('GET', ))
def api_root (request, format=None):
    return Response ({'users': reverse('user-list', request=request, format=format),
                      'questions':reverse('question-list', request=request, format=format)
    })

# class QuestionList(mixins.ListModelMixin,
#                    mixins.CreateModelMixin,
#                    generics.GenericAPIView):
#     queryset=Question.objects.all()
#     serializer_class=QuestionSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post (self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
# class QuestionDetail(mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin,
#                      generics.GenericAPIView):
#     queryset = Question.objects.all()
#     serializer_class=QuestionSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)





# class QuestionList(APIView):
#
#     def get(self, request, format=None):
#         questions = Question.objects.all()
#         serializer=QuestionSerializer(questions, many=True)
#         return Response(serializer.data)
#     def post(self, request, format=None):
#         serializer=QuestionSerializer(data=request.DATA)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
# class QuestionDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Question.objects.get(pk=pk)
#
#         except Question.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         question=self.get_object(pk)
#         serializer=QuestionSerializer(question)
#         return Response(serializer.data)
#
#     def put (self, request, pk, format=None):
#         question =self.get_object(pk)
#         serializer=QuestionSerializer(question, data=request.DATA)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response (serializer.error, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete (self, request, pk, format=None):
#         question = self.get_object(pk)
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

