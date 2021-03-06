# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-13 15:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='endereço')),
                ('complement', models.CharField(blank=True, max_length=100, verbose_name='complemento')),
                ('district', models.CharField(blank=True, max_length=100, verbose_name='bairro')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='cidade')),
                ('uf', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Brasília'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], max_length=2, verbose_name='UF')),
                ('cep', models.CharField(blank=True, max_length=9, verbose_name='CEP')),
                ('gender', models.CharField(blank=True, choices=[('M', 'masculino'), ('F', 'feminino')], max_length=1, null=True, verbose_name='gênero')),
                ('treatment', models.CharField(blank=True, choices=[('a', 'Arq.'), ('aa', 'Arqa.'), ('d', 'Dona'), ('dr', 'Dr.'), ('dra', 'Dra.'), ('e', 'Eng.'), ('ea', 'Engª.'), ('p', 'Prof.'), ('pa', 'Profa.'), ('sr', 'Sr.'), ('sra', 'Sra.'), ('srta', 'Srta.')], max_length=4, null=True, verbose_name='tratamento')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('photo', models.URLField(blank=True, null=True, verbose_name='foto')),
                ('birthday', models.DateTimeField(blank=True, null=True, verbose_name='nascimento')),
                ('company', models.CharField(blank=True, max_length=50, null=True, verbose_name='empresa')),
                ('department', models.CharField(blank=True, max_length=50, null=True, verbose_name='departamento')),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='CPF')),
                ('rg', models.CharField(blank=True, max_length=11, null=True, verbose_name='RG')),
                ('active', models.BooleanField(default=True, verbose_name='ativo')),
                ('blocked', models.BooleanField(default=False, verbose_name='bloqueado')),
                ('first_name', models.CharField(max_length=50, verbose_name='nome')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='sobrenome')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('cnpj', models.CharField(blank=True, max_length=14, null=True, unique=True, verbose_name='CNPJ')),
                ('ie', models.CharField(blank=True, max_length=12, null=True, verbose_name='inscrição estadual')),
                ('customer_type', models.CharField(choices=[('c', 'construtora'), ('a', 'arquitetura'), ('p', 'particular')], max_length=1, verbose_name='tipo')),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='endereço')),
                ('complement', models.CharField(blank=True, max_length=100, verbose_name='complemento')),
                ('district', models.CharField(blank=True, max_length=100, verbose_name='bairro')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='cidade')),
                ('uf', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Brasília'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], max_length=2, verbose_name='UF')),
                ('cep', models.CharField(blank=True, max_length=9, verbose_name='CEP')),
                ('gender', models.CharField(blank=True, choices=[('M', 'masculino'), ('F', 'feminino')], max_length=1, null=True, verbose_name='gênero')),
                ('treatment', models.CharField(blank=True, choices=[('a', 'Arq.'), ('aa', 'Arqa.'), ('d', 'Dona'), ('dr', 'Dr.'), ('dra', 'Dra.'), ('e', 'Eng.'), ('ea', 'Engª.'), ('p', 'Prof.'), ('pa', 'Profa.'), ('sr', 'Sr.'), ('sra', 'Sra.'), ('srta', 'Srta.')], max_length=4, null=True, verbose_name='tratamento')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('photo', models.URLField(blank=True, null=True, verbose_name='foto')),
                ('birthday', models.DateTimeField(blank=True, null=True, verbose_name='nascimento')),
                ('company', models.CharField(blank=True, max_length=50, null=True, verbose_name='empresa')),
                ('department', models.CharField(blank=True, max_length=50, null=True, verbose_name='departamento')),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='CPF')),
                ('rg', models.CharField(blank=True, max_length=11, null=True, verbose_name='RG')),
                ('active', models.BooleanField(default=True, verbose_name='ativo')),
                ('blocked', models.BooleanField(default=False, verbose_name='bloqueado')),
                ('date_entry', models.DateTimeField(blank=True, null=True, verbose_name='data de entrada')),
                ('date_release', models.DateTimeField(blank=True, null=True, verbose_name='data de saída')),
            ],
            options={
                'verbose_name': 'funcionário',
                'verbose_name_plural': 'funcionários',
                'ordering': ['user__first_name'],
            },
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.CharField(max_length=50, unique=True, verbose_name='cargo')),
            ],
            options={
                'verbose_name': 'cargo',
                'verbose_name_plural': 'cargos',
                'ordering': ['occupation'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='endereço')),
                ('complement', models.CharField(blank=True, max_length=100, verbose_name='complemento')),
                ('district', models.CharField(blank=True, max_length=100, verbose_name='bairro')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='cidade')),
                ('uf', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Brasília'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], max_length=2, verbose_name='UF')),
                ('cep', models.CharField(blank=True, max_length=9, verbose_name='CEP')),
                ('gender', models.CharField(blank=True, choices=[('M', 'masculino'), ('F', 'feminino')], max_length=1, null=True, verbose_name='gênero')),
                ('treatment', models.CharField(blank=True, choices=[('a', 'Arq.'), ('aa', 'Arqa.'), ('d', 'Dona'), ('dr', 'Dr.'), ('dra', 'Dra.'), ('e', 'Eng.'), ('ea', 'Engª.'), ('p', 'Prof.'), ('pa', 'Profa.'), ('sr', 'Sr.'), ('sra', 'Sra.'), ('srta', 'Srta.')], max_length=4, null=True, verbose_name='tratamento')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('photo', models.URLField(blank=True, null=True, verbose_name='foto')),
                ('birthday', models.DateTimeField(blank=True, null=True, verbose_name='nascimento')),
                ('company', models.CharField(blank=True, max_length=50, null=True, verbose_name='empresa')),
                ('department', models.CharField(blank=True, max_length=50, null=True, verbose_name='departamento')),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='CPF')),
                ('rg', models.CharField(blank=True, max_length=11, null=True, verbose_name='RG')),
                ('active', models.BooleanField(default=True, verbose_name='ativo')),
                ('blocked', models.BooleanField(default=False, verbose_name='bloqueado')),
                ('first_name', models.CharField(max_length=50, verbose_name='nome')),
                ('last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='sobrenome')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('occupation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_occupation', to='crm.Occupation', verbose_name='cargo')),
            ],
            options={
                'verbose_name': 'contato',
                'verbose_name_plural': 'contatos',
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='telefone')),
                ('phone_type', models.CharField(choices=[('pri', 'principal'), ('com', 'comercial'), ('res', 'residencial'), ('cel', 'celular'), ('cl', 'Claro'), ('oi', 'Oi'), ('t', 'Tim'), ('v', 'Vivo'), ('n', 'Nextel'), ('fax', 'fax'), ('o', 'outros')], default='pri', max_length=3, verbose_name='tipo')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal', models.BooleanField(default=True, verbose_name='interno')),
                ('commissioned', models.BooleanField(default=True, verbose_name='comissionado')),
                ('commission', models.DecimalField(decimal_places=2, default=0.01, max_digits=6, verbose_name='comissão')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seller_employee', to='crm.Employee', verbose_name='funcionário')),
            ],
            options={
                'verbose_name': 'vendedor',
                'verbose_name_plural': 'vendedores',
                'ordering': ['employee__user__first_name'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='occupation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_occupation', to='crm.Occupation', verbose_name='cargo'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
