from django.contrib import admin
#from DASE.models import beca_excelencia

#from import_export import resources
#from import_export.admin import ImportExportModelAdmin

# Register your models here.

# class becas_excelenciaResource(resources.ModelResource):
#     class Meta:
#         model = beca_excelencia

# class becas_excelenciaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = ("nombre","cedula","carrera", "tipo_beneficio", "porcentaje", "aportante_fondo_becas")
#     search_fields = ("nombre","cedula","carrera", "tipo_beneficio", "porcentaje", "aportante_fondo_becas")
#     resource_class = becas_excelenciaResource

# admin.site.register(beca_excelencia, becas_excelenciaAdmin)

# Personalizacion admin site
admin.site.site_header = "Sistema de control y gestión DASE"
admin.site.site_title = "DASE"
