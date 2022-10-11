from django.db import models


class Tarefa(models.Model):

    OPCOES_STATUS = (
        ('concluído', 'Concluído'),
        ('pendente', 'Pendente'),
        ('adiado', 'Adiado'),
    )

    OPCOES_CATEGORIA = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('precisa ser feito', 'Precisa ser feito'),
    )

    descricao = models.CharField(max_length=500)
    criacao = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=50, choices=OPCOES_CATEGORIA, default='importante')
    status = models.CharField(max_length=50, choices=OPCOES_STATUS, default='pendente')
    
    def __str__(self):
        return self.descricao
    