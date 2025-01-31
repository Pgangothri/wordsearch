from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework import status,generics
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.views import APIView
from .models import Paragraph, Word, CustomUser
from .serializer import ParagraphSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from collections import defaultdict
from django.utils.html import escape
from django.db.models import Count
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
class ParagraphListCreateView(generics.ListCreateAPIView):
    serializer_class = ParagraphSerializer
    authentication_classes = [TokenAuthentication]  # Require Token authentication
    permission_classes = [IsAuthenticated]  # Require user to be authenticated

    def get_queryset(self):
        return Paragraph.objects.all()

    def create(self, request, *args, **kwargs):
        # Extract text from request data
        text = request.data.get("text", "")

        if not text:
            # Return an error response if no text is provided
            return Response({'error': 'Please provide text to create paragraphs'}, status=status.HTTP_400_BAD_REQUEST)

        # Split text into paragraphs based on two newline characters
        paragraphs_text = text.split('\n\n')

        # Create paragraphs and store in the database
        created_paragraphs = []
        for paragraph_text in paragraphs_text:
            paragraph = Paragraph(content=paragraph_text)
            paragraph.save()
            created_paragraphs.append({'id': paragraph.id, 'content': paragraph.content})

        # Serialize and return the created paragraphs
        serializer = self.get_serializer(Paragraph.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# View for retrieving, updating, and deleting a specific paragraph
class ParagraphRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer
    authentication_classes = [TokenAuthentication]  # Require Token authentication
    permission_classes = [IsAuthenticated]  # Require user to be authenticated

# API view for searching paragraphs containing a specific word
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def search_paragraphs(request, word):
    if not word:
        # Return an error response if no word is provided
        return Response({'error': 'Please provide a word to search'}, status=status.HTTP_400_BAD_REQUEST)

    # Use Q objects to perform case-insensitive search
    matching_paragraphs = Paragraph.objects.filter(Q(content__icontains=word))

    if not matching_paragraphs:
        # Return a message if no matching paragraphs are found
        return Response({'message': f'The word "{word}" was not found in any paragraph.'}, status=status.HTTP_404_NOT_FOUND)

    # Annotate each paragraph with the count of occurrences of the word
    annotated_paragraphs = matching_paragraphs.annotate(word_count=Count('content', filter=Q(content__icontains=word)))

    # Order the paragraphs by word_count in descending order
    ordered_paragraphs = annotated_paragraphs.order_by('-word_count')[:10]

    # Highlight the word in each paragraph
    highlighted_paragraphs = []
    for paragraph in ordered_paragraphs:
        highlighted_content = paragraph.content.replace(word, f'<strong>{escape(word)}</strong>')
        highlighted_paragraphs.append({'id': paragraph.id, 'content': highlighted_content})

    # Return the results with highlighted paragraphs
    return Response({'results': highlighted_paragraphs})

class ParagraphRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer
    authentication_classes = [TokenAuthentication]  # Require Token authentication
    permission_classes = [IsAuthenticated]