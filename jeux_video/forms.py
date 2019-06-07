from django import forms
import datetime
from jeux_video.models import Jeuxvideos,Editeurs,Developpeurs,Genres,Plateformes

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    envoyeur = forms.EmailField(label="Votre adresse e-mail", widget=forms.TextInput(attrs={'class': "form-control"}))
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)
    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        sujet = cleaned_data.get('sujet')
        message = cleaned_data.get('message')

        if sujet and message:  # Est-ce que sujet et message sont valides ?
            if "pizza" in sujet and "pizza" in message:
                self.add_error("message", 
                "Vous parlez déjà de pizzas dans le sujet, "
                "n'en parlez plus dans le message !"
            )

        return cleaned_data  # N'oublions pas de renvoyer les données si tout est OK

class JeuxvideosForm(forms.ModelForm):
    class Meta:
        model = Jeuxvideos
        fields= '__all__'
        widgets = {
            'titre': forms.TextInput(attrs={'class': "form-control"}),
            'description' : forms.Textarea(attrs={'class': "form-control"}),
            'date' : forms.DateInput(attrs={'class': "form-control"}),
            'genre' : forms.CheckboxSelectMultiple(),
            'plateforme' : forms.CheckboxSelectMultiple(),
            'editeur' : forms.CheckboxSelectMultiple(),
            'developpeur' : forms.CheckboxSelectMultiple(),
        }

class EditeursForm(forms.ModelForm):
    class Meta:
        model = Editeurs
        fields= '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': "form-control"}),
            'description': forms.Textarea(attrs={'class': "form-control"}),
            
        }

class DeveloppeursForm(forms.ModelForm):
    class Meta:
        model = Developpeurs
        fields= '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': "form-control"}),
            'description': forms.Textarea(attrs={'class': "form-control"}),
        
        }

class PlateformesForm(forms.ModelForm):
    class Meta:
        model = Plateformes
        fields= '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': "form-control"}),
            
        }

class GenresForm(forms.ModelForm):
    class Meta:
        model = Genres
        fields= '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': "form-control"}),
            'description': forms.Textarea(attrs={'class': "form-control"}),
         
        }