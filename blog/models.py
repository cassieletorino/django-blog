from django.db import models

from django.contrib.auth import get_user_model 
User = get_user_model()

class Post(models.Model):
    body_text = models.TextField('Texto Principal')
    pub_date = models.DateTimeField('Data Publicação')
    categoria = models.CharField(
        'Categoria',
        max_length=15,
        choices=[
            ('noticias', 'Notícias'),
            ('como_fazer', 'Como Fazer'),
            ('review', 'Review'),
        ],
        default=None,
        null=True
    )
    autor= models.ForeignKey(
        User, # chave estrangeira vinculada ao usuário 
        editable=False, # não permite editar 
        on_delete=models.DO_NOTHING, # não exclui a pergunta se o autor for removido
        null=True # permite autor NULL para não conflitar com registros já existentes
    )