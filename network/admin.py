from django.contrib import admin

from network.models import Network, Product


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'supplier', 'city', 'created_at')
    search_fields = ['name', 'city']
    list_filter = ['country', 'city']
    readonly_fields = ['created_at']
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        rows_updated = queryset.update(debt_to_supplier=0.00)
        if rows_updated == 1:
            message_bit = '1 запись была обновлена.'
        else:
            message_bit = '%s записей были обновлены.' % rows_updated
        self.message_user(request, '%s Задолженности обнулены.' % message_bit)

    clear_debt.short_description = 'Очистить задолженности перед поставщиками.'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('products', 'name', 'model', 'release_date')

