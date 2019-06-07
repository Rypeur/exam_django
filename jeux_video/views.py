from django.shortcuts import redirect,render,get_object_or_404
from django.http import HttpResponse, Http404
from django.template.defaultfilters import slugify
from datetime import datetime
from jeux_video.models import Jeuxvideos,Genres,Editeurs,Developpeurs,Plateformes
from jeux_video.forms import ContactForm,DeveloppeursForm,EditeursForm,GenresForm,PlateformesForm,JeuxvideosForm

def home(request):
    return render(request, 'jeux_video/home.html', locals())

def jeuxvideos(request) :
    jeux_videos = Jeuxvideos.objects.all() 
    return render(request, 'jeux_video/jeux_videos.html', {'jeux_videos': jeux_videos})

def view_jeu_video(request, id):
    jeu_video = get_object_or_404(Jeuxvideos, id=id)
    editeurs = jeu_video.editeur.all
    developpeurs = jeu_video.developpeur.all
    genres = jeu_video.genre.all
    plateformes = jeu_video.plateforme.all
    return render(request, 'jeux_video/view_jeu_video.html', locals())

def add_jeu_video(request) :
    form = JeuxvideosForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        envoi = True    
    return render(request, 'jeux_video/add_jeu_video.html', locals())

def modify_jeu_video(request,id):
    jeu_video=get_object_or_404(Jeuxvideos, id=id)
    form = JeuxvideosForm(request.POST or None,request.FILES or None,instance=jeu_video)
    if form.is_valid():
        form.save()
        envoi = True  
    return render(request, 'jeux_video/modify_jeu_video.html', locals())

def delete_jeu_video(request,id):
    jeu_video=get_object_or_404(Jeuxvideos, id=id)
    jeu_video.delete()
    return redirect('jeux_videos')
    
def genres(request) : 
    genres = Genres.objects.all() 
    return render(request, 'jeux_video/genres.html', {'genres': genres})

def view_genre(request, id):
    genre = get_object_or_404(Genres, id=id)
    return render(request, 'jeux_video/view_genre.html', locals())

def add_genre(request) :
    form = GenresForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        envoi = True    
    return render(request, 'jeux_video/add_genre.html', locals())

def modify_genre(request,id):
    genre=get_object_or_404(Genres, id=id)
    form = GenresForm(request.POST or None,request.FILES or None,instance=genre)
    if form.is_valid():
        form.save()
        envoi = True  
    return render(request, 'jeux_video/modify_genre.html', locals())

def delete_genre(request,id):
    genre=get_object_or_404(Genres, id=id)
    genre.delete()
    return redirect('genre')

def editeurs(request) :
    editeurs = Editeurs.objects.all() 
    return render(request, 'jeux_video/editeurs.html', {'editeurs': editeurs})

def view_editeur(request, id):
    editeur = get_object_or_404(Editeurs, id=id)
    return render(request, 'jeux_video/view_editeur.html', locals())

def add_editeur(request) :
    form = EditeursForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        envoi = True    
    return render(request, 'jeux_video/add_editeur.html', locals())

def modify_editeur(request,id):
    editeur=get_object_or_404(Editeurs, id=id)
    form = EditeursForm(request.POST or None,request.FILES or None,instance=editeur)
    if form.is_valid():
        form.save()
        envoi = True  
    return render(request, 'jeux_video/modify_editeur.html', locals())

def delete_editeur(request,id):
    editeur=get_object_or_404(Editeurs, id=id)
    editeur.delete()
    return redirect('editeur')

def developpeurs(request) : 
    developpeurs = Developpeurs.objects.all() 
    return render(request, 'jeux_video/developpeurs.html', {'developpeurs': developpeurs})

def view_developpeur(request, id):
    developpeur = get_object_or_404(Developpeurs, id=id)
    return render(request, 'jeux_video/view_developpeur.html', locals())

def add_developpeur(request) :
    form = DeveloppeursForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        envoi = True    
    return render(request, 'jeux_video/add_developpeur.html', locals())

def modify_developpeur(request,id):
    developpeur=get_object_or_404(Developpeurs, id=id)
    form = DeveloppeursForm(request.POST or None,request.FILES or None,instance=developpeur)
    if form.is_valid():
        form.save()
        envoi = True  
    return render(request, 'jeux_video/modify_developpeur.html', locals())

def delete_developpeur(request,id):
    developpeur=get_object_or_404(Developpeurs, id=id)
    developpeur.delete()
    return redirect('developpeurs')

def plateformes(request) :
    plateformes = Plateformes.objects.all() 
    return render(request, 'jeux_video/plateformes.html', {'plateformes': plateformes})

def add_plateforme(request) :
    form = PlateformesForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        envoi = True    
    return render(request, 'jeux_video/add_plateforme.html', locals())

def modify_plateforme(request,id):
    plateforme=get_object_or_404(Plateformes, id=id)
    form = PlateformesForm(request.POST or None,request.FILES or None,instance=plateforme)
    if form.is_valid():
        form.save()
        envoi = True  
    return render(request, 'jeux_video/modify_plateforme.html', locals())

def delete_plateforme(request,id):
    plateforme=get_object_or_404(Plateformes, id=id)
    plateforme.delete()
    return redirect('plateformes')

def contact(request):
    
    form = ContactForm(request.POST or None)
    
    if form.is_valid(): 
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']
        envoi = True
    return render(request, 'jeux_video/contact.html', locals())    