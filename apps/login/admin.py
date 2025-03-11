from django.contrib import admin
from .models import Campus, User
from django.contrib.auth.admin import UserAdmin

admin.site.register(Campus)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ('nome_completo', 'cpf', 'email')}),
        ('Informações Acadêmicas', {'fields': ('campus_lotacao', 'matricula', 'cargo')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'nome_completo', 'email', 'campus_lotacao', 'is_staff')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'nome_completo', 'email', 'campus_lotacao', 'matricula', 'cargo', 'is_staff', 'is_superuser'),
        }),
    )
    ordering = ('username',)