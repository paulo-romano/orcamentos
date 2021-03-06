from django import forms

from orcamentos.crm.validate import validate_documents
from orcamentos.utils.lists import GENDER, CUSTOMER_TYPE
from orcamentos.crm.models import Customer, Person


class CustomerForm(forms.ModelForm):
    gender = forms.ChoiceField(
        label='Sexo', choices=GENDER, initial='M', widget=forms.RadioSelect)
    customer_type = forms.ChoiceField(
        label='Tipo', choices=CUSTOMER_TYPE, initial='p', widget=forms.RadioSelect)

    class Meta:
        model = Customer
        fields = ['gender', 'treatment', 'first_name', 'last_name', 'slug',
                  'photo', 'birthday', 'company', 'department', 'email',
                  'cpf', 'rg', 'cnpj', 'ie', 'customer_type', 'address',
                  'complement', 'district', 'city', 'uf', 'cep', 'active']

    def clean_cpf(self):
        return self.cleaned_data['cpf'] or None

    def clean_cnpj(self):
        if not self.cleaned_data['cnpj']:
            return None
        else:
            validate_documents.cnpj(self.cleaned_data['cnpj'])
            return self.cleaned_data['cnpj']


class PersonForm(forms.ModelForm):
    gender = forms.ChoiceField(
        label='Sexo', choices=GENDER, initial='M', widget=forms.RadioSelect)

    class Meta:
        model = Person
        fields = '__all__'

    def clean_cpf(self):
        return self.cleaned_data['cpf'] or None
