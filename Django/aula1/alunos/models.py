from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length = 200)
    data_nascimento = models.DateField('date published')

class Curso(models.Model):
    nome = models.CharField(max_length = 200)

class Disciplina(models.Model):
    # Chave estrangeira p/ Curso.
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    nome = models.CharField(max_length = 200)
    codigo = models.CharField(max_length = 6, null = True)