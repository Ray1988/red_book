

# Create your views here.
from django.http import HttpResponse
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics


from models import Question
from serializer import QuestionSerializer


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

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

