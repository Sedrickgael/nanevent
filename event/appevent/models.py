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

class Events(models.Model):

    nom_event = models.CharField(max_length=50)
    date_debut = models.DateField(, auto_now=False, auto_now_add=False)
    date_fin = models.DateField(, auto_now=False, auto_now_add=False)
    id_commune = models.ForeignKey('Commune', on_delete=models.CASCADE)
    compagnie_id = models.ForeignKey('Compagnie', on_delete=models.CASCADE)
    id_categorie = models.ForeignKey('Categorie_event', on_delete=models.CASCADE)
    statut = models.BooleanField(default=False)
    description  = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_event

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Events'
        verbose_name_plural = 'Eventss'


class Users(models.Model):
    
    id_commune = models.ForeignKey('Commune', on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    date_udapte = models.DateField(auto_now=False,)
    dat_add = models.DateField(auto_now=False, auto_now_add=False)
    statut = models.BooleanField()

    def __str__(self):
        return self.nom + self.prenom

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Users'
        verbose_name_plural = 'Userss'
        
class Categorie_event(models.Model):
    
    nom = models.CharField(max_length=255)
    date_udapte = models.DateField(auto_now=False,)
    dat_add = models.DateField(auto_now=False, auto_now_add=False)
    statut = models.BooleanField()

    def __str__(self):
        return self.nom

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'categorie_event'
        verbose_name_plural = 'categorie_events'

class Participants(models.Model):
    
    id_user = models.ForeignKey('Users', on_delete=models.CASCADE, related_name='participant_user')
    id_event = models.ForeignKey('Events', on_delete=models.CASCADE, related_name='participant_event')
    date_udapte = models.DateField(auto_now=False,)
    dat_add = models.DateField(auto_now=False, auto_now_add=False)
    statut = models.BooleanField()

    # def __str__(self):
    #     return self.id_user

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Participants'
        verbose_name_plural = 'Participantss'
        verbose_name_plural = 'Eventss'