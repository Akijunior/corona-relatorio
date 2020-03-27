from django.db import models

# Create your models here.
class SuperClass(models.Model):
    STATUS = (
        ('A', 'Ativo(a)'),
        ('I', 'Inativo(a)'),
    )

    created_at = models.DateTimeField('Cadastrado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    status = models.CharField('Status', blank=True, default='I', choices=STATUS, max_length=1)

    class Meta:
        abstract = True
        ordering = ('created_at',)