from django.contrib.admin import ModelAdmin, register
from .models import Candidato, Documento
from django.contrib import admin

#@register(UF)
# class UFAdmin(ModelAdmin):
#     list_display = ('sigla', 'nome', 'codigo')
#
#
# @register(Municipio)
# class MunicipioAdmin(ModelAdmin):
#     list_display = ('codigo', 'uf', 'nome')
#     list_editable = ('uf', 'nome')
#     list_filter = ('uf__nome', )
#     search_fields = ('nome', 'codigo')

admin.site.register(Candidato)
admin.site.register(Documento)