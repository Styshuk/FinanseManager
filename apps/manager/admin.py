from django.contrib import admin

# Register your models here.
from apps.manager.models import OperationType, Operation, Currency, Category

admin.site.register(OperationType)
admin.site.register(Currency)
admin.site.register(Category)


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "date", "category_id", "type_id", "value", "currency_id")
    list_filter = ("user_id__username", "category_id__name")
    search_fields = ("value", )
