from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.





class PaginaPersonalizada(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    nome_pagina = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class CamposPersonalizados(models.Model):
    pagina = models.ForeignKey(PaginaPersonalizada, on_delete=models.CASCADE, db_index=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    nome_campo = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class ValorCampoPersonalizados(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    campo = models.ForeignKey(CamposPersonalizados, on_delete=models.CASCADE, db_index=True)
    valor = models.CharField(max_length=100)
    tipo_dado = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
