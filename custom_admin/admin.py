from django.contrib import admin
from .models import TV, Notebook, Dishwasher, Brand, Category, VacuumCleaner, Item, Promo

# 1 способ (простой)
# for model in [TV, Notebook, Dishwasher, Brand, Category, VacuumCleaner, Promo]:
#     admin.site.register(model)


# реализация вложенных полей, например, для изменения нескольких записей для одной модели
# class DishwasherInstanceInline(admin.TabularInline):
#     model = Dishwasher
#
#
# @admin.register(Brand)
# class BrandAdmin(admin.ModelAdmin):
#     inlines = [DishwasherInstanceInline]
# конец реализации вложенных полей


# 2 способ (продвинутый): используя класс ModelAdmin и декоратор @admin.register()
# декоратор @admin.register() регистрирует декорируемый класс – наследник ModelAdmin
@admin.register(Dishwasher)                 # модели созданы в models.py
class DishwasherAdmin(admin.ModelAdmin):
    # class Media:
    #     css = {}

    # поля модели для отображения на странице списка;
    # test_show_promo - функция (см.ниже), colored_name - функция класса Dishwasher
    list_display = ('model', 'brand_name', 'price', 'color', 'test_show_promo', 'colored_name')

    # для блока фильтрации списка, который фильтрует по перечисленным полям (будет справа на странице)
    list_filter = ('price', 'brand_name', 'color',)

    # fields = [('model', 'brand_name'), ('price', 'color')]
    fieldsets = (
        ('General info', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('brand_name', 'model', 'count'),
        }),
        ('Advanced options', {
            'classes': ('wide', 'extrapretty'),
            'description': ('Описание полей'),
            'fields': ('price', 'color', 'warranty'),
        }),)
    # сортировка по цене
    sortable_by = 'price'
    # строка. поиска, добавляется для моделей, у которых определен атрибут search_fields
    search_fields = ['model']
    # поиск в поле brand_name по укзанному pk
    # search_fields = ['brand_name__pk']
    # исключаемое поле
    # exclude = ('price',)
    # дефолтный параметр для пустых полей
    empty_value_display = '-Без бренда-'
    # неизменяемое поле
    readonly_fields = ['price']

    def test_show_promo(self, obj):
        return obj.promo

    # можно переопределить стандартные функции
    def delete_model(self, request, obj):
        pass    # отключаем удаление по нажатию кнопки "Delete"

