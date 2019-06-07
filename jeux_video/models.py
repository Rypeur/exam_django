from django.db import models

# Create your models here.
class Genres(models.Model):
    nom = models.CharField(max_length=100,verbose_name="Nom  du Genre")
    description = models.CharField(null=True,max_length=1000)
    image = models.ImageField()

    def __str__(self):
        return self.nom

class Plateformes(models.Model):
    nom = models.CharField(max_length=30,verbose_name="Nom de la Plateforme")
    image = models.ImageField()

    def __str__(self):
        return self.nom

class Editeurs(models.Model):
    nom = models.CharField(max_length=30,verbose_name="Nom de l'Editeur")
    description = models.CharField(null=True,max_length=1000)
    image = models.ImageField()

    def __str__(self):
        return self.nom

class Developpeurs(models.Model):
    nom = models.CharField(max_length=30,verbose_name="Nom de l'Equipe")
    description = models.CharField(null=True,max_length=1000)
    image = models.ImageField()

    def __str__(self):
        return self.nom


class Jeuxvideos(models.Model):
    titre = models.CharField(max_length=100,verbose_name="Titre du Jeu")
    description = models.TextField(null=True,max_length=1000)
    date = models.DateTimeField(verbose_name="Date de sortie")
    image = models.ImageField()

    genre = models.ManyToManyField(Genres,related_name="jeux_videos")
    plateforme = models.ManyToManyField(Plateformes,related_name="jeux_videos")
    editeur = models.ManyToManyField(Editeurs,related_name="jeux_videos")
    developpeur = models.ManyToManyField(Developpeurs,related_name="jeux_videos")
    
    class Meta:
        verbose_name = "jeux_videos"    
        ordering = ['date']
    
    def __str__(self):
        return self.titre