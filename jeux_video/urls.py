from django.urls import path
from jeux_video import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('contact/',views.contact,name='contact'),
    path('jeux_videos/',views.jeuxvideos,name='jeux videos'),
    path('jeux_videos/view_jeux_video/<int:id>/', views.view_jeu_video,name='view_jeu_video'),
    path('jeux_videos/add_jeux_video/', views.add_jeu_video,name='add_jeu_video'),
    path('jeux_videos/modify_jeu_video/<int:id>/', views.modify_jeu_video,name='modify_jeu_video'),
    path('jeux_videos/delete_jeu_video/<int:id>/', views.delete_jeu_video,name='delete_jeu_video'),

    path('genres/',views.genres,name='genres'),
    path('genres/view_genre/<int:id>/', views.view_genre,name='view_genre'),
    path('genres/add_genre/', views.add_genre,name='add_genre'),
    path('genres/modify_genre/<int:id>/', views.modify_genre,name='modify_genre'),
    path('genres/delete_genre/<int:id>/', views.delete_genre,name='delete_genre'),

    path('editeurs/',views.editeurs,name='editeurs'),
    path('editeurs/view_editeur/<int:id>/', views.view_editeur,name='view_editeur'),
    path('editeurs/add_editeur/', views.add_editeur,name='add_editeur'),
    path('editeurs/modify_editeur/<int:id>/', views.modify_editeur,name='modify_editeur'),
    path('editeurs/delete_editeur/<int:id>/', views.delete_editeur,name='delete_editeur'),

    path('developpeurs/',views.developpeurs,name='developpeurs'),
    path('developpeurs/view_developpeur/<int:id>/', views.view_developpeur,name='view_developpeur'),
    path('developpeurs/add_developpeur/', views.add_developpeur,name='add_developpeur'),
    path('developpeurs/modify_developpeur/<int:id>/', views.modify_developpeur,name='modify_developpeur'),
    path('developpeurs/delete_developpeur/<int:id>/', views.delete_developpeur,name='delete_developpeur'),

    path('plateformes/',views.plateformes,name='plateformes'),  
    path('plateformes/add_plateforme/', views.add_plateforme,name='add_plateforme'),
    path('plateformes/modify_plateforme/<int:id>/', views.modify_plateforme,name='modify_plateforme'),
    path('plateformes/delete_plateforme/<int:id>/', views.delete_plateforme,name='delete_plateforme'),


]