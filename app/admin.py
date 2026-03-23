from django.contrib import admin
from .models import Cidade, Autor, Editora, Leitor, Livro, Genero


# 1. Definição dos Inlines (deve vir antes de quem os usa)
class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1


# 2. Definição das classes Admin customizadas
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [LivroInline]


# 3. Registro dos modelos (APENAS UMA VEZ PARA CADA)
admin.site.register(Cidade)
admin.site.register(Editora)
admin.site.register(Leitor)
admin.site.register(Genero)
admin.site.register(Livro)  # Registra o Livro sozinho
admin.site.register(Autor, AutorAdmin)  # Registra o Autor com a configuração especial