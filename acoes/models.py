from django.db import models
import json

class Acoes(models.Model):
    acao = models.CharField(max_length=15,blank=False,null=False)
    dispositivo = models.IntegerField(blank=False, null=False)
    def __str__(obj):
        tmp = {
            "id": obj.id,
            "acao": obj.acao,
            "dispositivo": obj.dispositivo,
        }
        
        return json.dumps(tmp)