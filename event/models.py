class Compagnie(models.Model):

    nom_compagnie = models.CharField(max_length=255)
    addresse = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nom_compagnie

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Compagnie'
        verbose_name_plural = 'Compagnies'
        
class Commune(models.Model):

    nom = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nom

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Commune'
        verbose_name_plural = 'Communes'