from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import get_object_or_404
from django.views import View
from django.contrib import messages

from .models import (
    Livro,
    Emprestimo,
    Cidade,
    Autor,
    Editora,
    Leitor,
    Genero
)

from .forms import LivroForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class LivrosView(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()
        return render(request, 'Livros.html', {'livros': livros})


class EmprestimoView(View):
    def get(self, request, *args, **kwargs):
        reservas = Emprestimo.objects.all()
        return render(request, 'reserva.html', {'reservas': reservas})


class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})


class AutoresView(View):
    def get(self, request, *args, **kwargs):
        autores = Autor.objects.all()
        return render(request, 'autor.html', {'autores': autores})


class EditorasView(View):
    def get(self, request, *args, **kwargs):
        editoras = Editora.objects.all()
        return render(request, 'editora.html', {'editoras': editoras})


class LeitoresView(View):
    def get(self, request, *args, **kwargs):
        leitores = Leitor.objects.all()
        return render(request, 'leitor.html', {'leitores': leitores})


class GenerosView(View):
    def get(self, request, *args, **kwargs):
        generos = Genero.objects.all()
        return render(request, 'genero.html', {'generos': generos})


class EditarLivroView(View):

    template_name = 'editar_livro.html'

    def get(self, request, id, *args, **kwargs):

        livro = get_object_or_404(
            Livro,
            id=id
        )

        form = LivroForm(
            instance=livro
        )

        return render(
            request,
            self.template_name,
            {
                'livro': livro,
                'form': form
            }
        )

    def post(self, request, id, *args, **kwargs):

        livro = get_object_or_404(
            Livro,
            id=id
        )

        form = LivroForm(
            request.POST,
            instance=livro
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'As edições foram salvas com sucesso.'
            )

            return redirect(
                'editar',
                id=id
            )

        else:

            messages.error(
                request,
                'Corrija os erros no formulário antes de enviar novamente.'
            )

            return render(
                request,
                self.template_name,
                {
                    'livro': livro,
                    'form': form
                }
            )

class DeleteLivroView(View):
    def get(self, request, id):

        livro = Livro.objects.filter(id=id).first()

        if livro:
            livro.delete()

        return redirect('livros')