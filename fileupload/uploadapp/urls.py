from django.urls import path
from . views import FileList

urlpatterns = [
    path('upload/', FileList.as_view())#, name='file-upload'),
]