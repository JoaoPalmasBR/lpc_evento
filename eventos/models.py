from django.db import models
from django.contrib.auth.models import User

class Endereco(models.Model):
    logradouro = models.CharField(max_length=128)
    complemento = models.CharField(max_length=256, null=True)
    uf = models.CharField(max_length=2, null=True)
    cidade = models.CharField(max_length=64, null=True)
    cep = models.CharField(max_length=10)
    def __str__(self):
        return '{} - {}, {}'.format(self.logradouro, self.cidade, self.uf)
class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.ForeignKey(Endereco, related_name='pessoas', null=True, blank=False)
    usuario = models.OneToOneField(User)

    def __str__(self):
        return self.nome
class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=128)
    mae = models.CharField(max_length=128, null=True)
    pai = models.CharField(max_length=128, null=True)

    def __str__(self):
        return '{} - {}'.format(self.nome, self.cpf)
class Evento(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.CharField(max_length=256)
    sigla = models.CharField(max_length=4)
    numero = models.CharField(max_length=10)
    ano = models.CharField(max_length=4)
    realizador = models.ForeignKey(PessoaFisica, related_name='pessoasfisicas', null=True, blank=False)
    endereco = models.ForeignKey(Endereco, null=True, blank=False)
    logo = models.CharField(max_length=128)
    data_de_inicio = models.DateField(blank=True, null=True)
    data_de_fim = models.DateField(blank=True, null=True)
    def __str__(self):
        return '{} - {}'.format(self.nome, self.data_de_inicio)
class Inscricao(models.Model):
    evento = models.ForeignKey(Evento,  null=True, blank=False)
    pessoa = models.ForeignKey(PessoaFisica, null=True, blank=False)
    data_de_inscricao = models.DateTimeField(blank=True, null=True)
    preco = models.FloatField()
    def __str__(self):
        return '{} - {}'.format(self.evento, self.pessoa)
