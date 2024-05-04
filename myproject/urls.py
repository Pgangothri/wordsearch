from django.urls import path
from myapp.views import ParagraphListCreateView,search_paragraphs,ParagraphRetrieveUpdateDestroyView,register_user,LoginAPIView

urlpatterns = [
    path('paragraphs/', ParagraphListCreateView.as_view(), name='paragraph-list-create'),

    # URL pattern for retrieving, updating, and deleting a specific paragraph
    path('paragraphs/<int:pk>/', ParagraphRetrieveUpdateDestroyView.as_view(), name='paragraph-retrieve-update-destroy'),

    # URL pattern for searching paragraphs containing a specific word
    path('search/<str:word>', search_paragraphs, name='search-paragraphs'),
    path('register/',register_user, name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    
]