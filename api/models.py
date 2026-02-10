from django.db import models

class ErrorReport(models.Model): # registrar errores en base datos
    code = models.IntegerField() # codigo del error
    description = models.TextField() #campo de texto para describir error
    date = models.DateTimeField() #para guardar fecha y hora del error

    def __str__(self):
        return f"Error {self.code}"