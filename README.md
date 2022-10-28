# python28oct

## despues de crear el proyecto

marcar la carpeta proj como la carpeta raiz.

## configurar el proyecto

En proj.settings, configure lo siguiente

en templates, agregue la direccion

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

y además cree una carpeta dentro de "proj"

En el mismo archivo, agregar la aplicación

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app1'
]
```

## Cree el modelo

Dentro de la carpeta app1, modifique el archivo models.py y agregue una clase con los campos que quiero que tenga la base de datos
Si necesito mas tablas, agrego mas clases.

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    edad = models.IntegerField(default=0)
```

## Crear la migracion

Necesitamos crear los archivos de migracion. En el terminal, ejecutar lo siguiente

```shell
python .\manage.py makemigrations
```

Eso va a crear (en carpeta app1.migrations), el archivo de migracion.

> Para poder correr python manage.py, tengo que estar dentro de la carpeta de proj

## Ejecutar la migracion

```shell
python.exe .\manage.py migrate 
```

## Ejecutar un ejemplo

Instalar la siguiente herramienta:

https://sqlitebrowser.org/dl/

Una vez que instale la herramienta, ir a la tabla y agregar dato.  Y no olvidar guardar la base de datos (file->save)

### crear views

en app1.views.py agregar una function que lee los datos. Y se los envio al template.

```python
def listar_person(request):
    personas=Person.objects.all()  # estoy trayendo todas las filas de la tabla persona
    return render(request,'listar_person.html',{"personas":personas})
```

### crear template
En la carpeta templates/listar_person.html, agregue lo siguiente:

```html
<ul>
    {% for person in personas %}
    <li>{{person.first_name}}, {{person.last_name}} {{person.edad}}</li>

    {% endfor %}
</ul>
```

### editar el url
En proj.urls agregar la ruta de la funcion de la vista que se creo:

```python
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('person/listar',views.listar_person)
]
```

### ejecutar el proyecto

```shell
python .\manage.py runserver 
```

E ir a la ruta indica en urls http://localhost:8000/person/listar para probar el ejemplo



