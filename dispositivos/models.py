from django.db import models
import json
class Dispositivos(models.Model):
    nome = models.CharField(max_length=50, blank=False,null=False)
    endereco = models.CharField(max_length=15,blank=False,null=False)
    chave = models.CharField(max_length=50, blank=False,null=False)
    def __str__(obj):
        tmp = {
            "id": obj.id,
            "nome": obj.nome,
            "endereco": obj.endereco,
            "chave": obj.chave,
        }
        
        return json.dumps(tmp)