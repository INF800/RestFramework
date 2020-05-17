#### 01. Pacages Needed

```
pip install django
pip install djangorestframework
```

#### 02. Simple Response API

**i. Create Project and App**

```
django-admin startproject fileupload
```
```
python manage.py startapp uploadapp
```

**ii. Configure your app**

In *fileupload/settings.py*:
```
INSTALLED_APPS = [
	
	...
	
	"rest_framework	",
	"fileupload",
]

	...
	...
	
# at end of file
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
```
Note that `media/` folder will be **created by itself**.

Add *media url* and *uploadapp urls* to main project urls.py

*fileupload/urls.py*:
```
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # added 2 of 3
    path('file/', include('uploadapp.urls')),
  ]

# media url
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Everything is configured!

**iii. Create Model and register**

*uploadapp/models.py*:
```
class File(models.Model):
	
  file = models.FileField(blank=False, null=False)
  remark = models.CharField(max_length=20)
  timestamp = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
  	return self.remark
```

Register to admin panel for gui actions

*uploadapp/admin.py*:
```
from . models import File
admin.site.register(File)
```

**iv. Create serializer to convt to JSON**

Create `serializers.py` in `uploadapp`

*uploadapp/serializers.py*:
```
from rest_framework import serializers
from . models import File

class FileSerializer(serializers.ModelSerializer):

  class Meta():
    model = File
    fields = ('file', 'remark', 'timestamp')
```


**iv. Add app views and urls**

*uploadapp/views.py*:
```
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from . serializers import FileSerializer

class FileList(APIView):
	
  parser_classes = (MultiPartParser, FormParser)

  def post(self, request, *args, **kwargs):

    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

*uploadapp/urls.py*: (create new if doesn't exist)
```
from django.urls import path
from . views import FileList

urlpatterns = [
    path('upload/', FileList.as_view())
]
```

**v. Create SU for admin panel and Prepare DB**
```
python manage.py createsuperuser

...

python manage.py makemigrations
python manage.py migrate
```
```
python manage.py runserver
```
All set! Now you can upload file from frontend or js or postman or forms using this api.

#### 03. Test API

Using form from ANY html file. You can do the same with terminal or postman or js
```
<form action="http://localhost:8000/file/upload/" method="post" enctype="multipart/form-data">
    <input type="text" name="remark" value="image1" />
    <input name="file" type="file" />
    <button>Submit</button>
</form>
```
Note that `enctype` is necessary.

