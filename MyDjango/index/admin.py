from django.contrib import admin

from user.models import MyUser
from . models import *
# Register your models here.
admin.site.site_title = 'MyDjango后台管理'
admin.site.site_title = 'MyDjango'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'weight', 'size', 'type',]
    search_fields = ['id', 'name', 'type__type_name']
    list_filter = ['name', 'type__type_name']
    ordering = ['id']
    fields = ['name', 'weight', 'size', 'type']
    readonly_fields = ['name']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            self.readonly_fields = []
        return self.readonly_fields
    list_display.append('colored_type')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'type':
            if not request.user.is_superuser:
                kwargs["queryset"] = Type.objects.filter(id__lt=4)
        return super(admin.ModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(id__lt=6)

    def save_model(self, request, obj, form, change):
        if change:
            user = request.user
            name = self.model.objects.get(pk=obj.pk).name
            weight = form.cleaned_data['weight']
            f = open('e://MyDjango_log.txt', 'a')
            f.write('产品：' + str(name) + '，被用户：' + str(user) + '修改' + '\r\n')
        else:
            pass
        super(ProductAdmin, self).save_model(request, obj, form, change)

