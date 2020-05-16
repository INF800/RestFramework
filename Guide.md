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