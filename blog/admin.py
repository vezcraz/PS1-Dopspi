from django.contrib import admin
from .models import *

# from django.contrib import admin
# from django.apps import apps

# app = apps.get_app_config('blog')

# for model_name, model in app.models.items():
#     admin.site.register(model)

class admin_chapterdata(admin.ModelAdmin):
	list_display = ('Year_Published', 'Chapter_Number', 'Table_Number')

	def get_queryset(self, request):
		queryset = super(admin_chapterdata, self).get_queryset(request)
		queryset = queryset.order_by('-Year_Published', '-Chapter_Number', '-Table_Number')
		return queryset

admin.site.register(Chapter_Data, admin_chapterdata)
admin.site.register(Index_Data)
admin.site.register(Year_Data)
admin.site.register(Ext_Link)
admin.site.register(Navbar)