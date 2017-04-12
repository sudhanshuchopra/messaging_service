from msg.models import Message
from .serializers import MessageSerializer
from rest_framework import generics
from rest_framework import permissions
from django.db.models import Q
from .permissions import IsCreatorOrReadOnly
from rest_framework.response import Response

class MessageList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def list(self, request):
        queryset = self.get_queryset()
        queryset=queryset.filter(Q(creator=request.user)|Q(recipent=request.user)).distinct()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsCreatorOrReadOnly,)
    queryset = Message.objects.all()
    serializer_class = MessageSerializer