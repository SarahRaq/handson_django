from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
#from .services import EditalService, VagaService
from django.contrib import admin


router = DefaultRouter()
#router.register('edital', EditalService)
#router.register('vaga', VagaService)

app_name = 'cadastro_edital'
urlpatterns = [

    path('admin/', admin.site.urls),


]