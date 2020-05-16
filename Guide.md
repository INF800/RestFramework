#### 01. Packages Needed

```
pip install django
pip install djangorestframework
```

#### 02. Simple Response API

**i. Create Project**

```
django-admin startproject responseapi
```

Creates folder named `responseapi` in cur dir. This is the  main project folder.

**ii. Create your app to send information**

```
python manage.py startapp senddata
```

**iii. Configure your project settings**

*responseapi/responseapi/settings.py*:
```
INSTALLED_APPS = {

	...
	
	"rest_framework",
	"senddata"
}
```

**iv. Add data to models that will be transmitted**

In your app,

*senddata/models.py*:
```
class Data(models.Model):
	data1 = models.CharField(max_length=10)
	data2 = models.IntegerField()
	
	def __str__(self):
		return self.data1
```

`__str__` summarizes our object. Gives very basic info.

Migrate your table
```
python manage.py makemigrations
```

**v. Add/delete data from admin pannel**

In app,

*senddata/admin.py*:
```
#a. import created model
from . models import Data

#b. register model
admin.site.register(Data)
```

Create superuser for admin pannel and run server
```
python manage.py createsuperuser
...
python manage.py runserver
```

Add data from admin panel `/admin` in your app `senddata`'s `Data` that will be transmitted

**vi. Convert model to JSON**

In `senddata` app dir, create `serializers.py`

*senddata/serializers.py*:
```
from rest_framework import serializers, Data

class DataSerializer(serializers.ModelSerializer):
	
	# configure Meta with fields in your model
	class Meta:
		model = Data #imported above
		fields = ('data1', 'data2') # not necessary to mention all avl. fields
		"""
		# you can give all avl. fields using
		fields = '__all__'
		"""
```

**vii. What you need to display**

In app's view, Request API and get json back

*senddata/views.py*:
```
#custom imports
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import response
from rest_framework import status
from . models import Data
from . serializers import DataSerializer

class DataList(APIView):
	"""
	# GET returns all data in model, Data
	# POST creates new data in model, Data
	"""
	
	def get(self, request):
		Data1 = Data.objects.all()  # store all instances or objects
		serializer = DataSerializer(Data1, many=True) # convt to many JSON objects
		return Response(serializer.data) # return JSON
	
	def post(self):
		pass
```

Link everything

*responseapi/urls.py*:
```
...

#custom imports
from rest_framework.urlpatterns import format_suffix_patterns
from senddata import views

urlpatterns = [
	...
	
	url(r'^getdata/', views.DataList.as_view()),
]
```

**All Set!**

goto: `/getdata/`. 

You can try with GET request in postman as well