from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Livro

class LivroForm(forms.ModelForm):

    class Meta:
        model = Livro
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(LivroForm, self).__init__(*args, **kwargs)

            self.helper = FormHelper()
            self.helper.layout = Layout(
                'titulo',
                'autor',
                'editora',
                'genero',
                'preco',
                'data_pub',
                'status',
                Submit('submit', 'Salvar')
                )

    class EditarLivroView(View):
        template_name = 'editar_livro.html'
    def get(self, request, id, *args, **kwargs):
        livro = get_object_or_404(Livro, id=id)
        form = LivroForm(instance=livro)
        return render(request, self.template_name, {'livro': livro,'form': form})
    def post(self, request, id, *args, **kwargs):
        livro = get_object_or_404(Livro, id=id)
