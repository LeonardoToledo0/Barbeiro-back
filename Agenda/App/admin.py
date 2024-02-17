from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Reserva,Cliente,Galeria,Banner


class ClienteAdmin(UserAdmin):
    list_display = ('email', 'nome', 'telefone', 'is_active', 'is_staff')
    search_fields = ('email', 'nome', 'telefone')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'senha')}),
        ('Informações Pessoais', {'fields': ('nome', 'telefone')}),
        ('Permissões', {'fields': ('is_active', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome', 'telefone', 'senha'),
        }),
    )

    filter_horizontal = ()
    list_filter = ('is_active', 'is_staff')

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'horario', 'confirmado')
    list_filter = ('confirmado',)
    search_fields = ('cliente__nome', 'horario')


class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'valor', 'imagem1_tag', 'imagem2_tag', 'imagem3_tag')

    def imagem1_tag(self, obj):
        return '<img src="{}" height="50"/>'.format(obj.imagem1.url) if obj.imagem1 else ''
    
    def imagem2_tag(self, obj):
        return '<img src="{}" height="50"/>'.format(obj.imagem2.url) if obj.imagem2 else ''

    def imagem3_tag(self, obj):
        return '<img src="{}" height="50"/>'.format(obj.imagem3.url) if obj.imagem3 else ''

    imagem1_tag.allow_tags = True
    imagem2_tag.allow_tags = True
    imagem3_tag.allow_tags = True

class BannerAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'imagem_tag')

    def imagem_tag(self, obj):
        return '<img src="{}" height="50"/>'.format(obj.imagem.url) if obj.imagem else ''

    imagem_tag.allow_tags = True


admin.site.register(Banner, BannerAdmin)
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Cliente, ClienteAdmin)
