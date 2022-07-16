from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    
    path('personas/', views.persona_list, name='personas'),
    path('personas/<str:pk>/', views.persona_detail, name='persona_detail'),
    
    path('ninjas/', views.ninja_list, name='ninjas'),
    path('ninjas/<str:pk>/', views.ninja_detail, name='ninja_detail'),
    
    path('genins/', views.genin_list, name='genins'),
    path('genins/<str:pk>/', views.genin_detail, name='genin_detail'),
    
    path('chunins/', views.chunin_list, name='chunins'),
    path('chunins/<str:pk>/', views.chunin_detail, name='chunin_detail'),
    
    path('jounins/', views.jounin_list, name='jounins'),
    path('jounins/<str:pk>/', views.jounin_detail, name='jounin_detail'),
    
    path('tecnicas/', views.tecnica_list, name='tecnicas'),
    path('tecnicas/<str:pk>/', views.tecnica_detail, name='tecnica_detail'),
    
    path('tecnicas-ataque/', views.tecnica_ataque_list, name='tecnicas-ataque'),
    path('tecnicas-ataque/<str:pk>/', views.tecnica_ataque_detail, name='tecnica-ataque_detail'),

    path('ninjas-medicos/', views.ninja_medico_list, name='ninjas-medicos'),
    path('ninjas-medicos/<str:pk>/', views.ninja_medico_detail, name='ninja-medico_detail'),
    
    path('tecnicas-curativas/', views.tecnica_curativa_list, name='tecnicas-curativas'),
    path('tecnicas-curativas/<str:pk>/', views.tecnica_curativa_detail, name='tecnica-curativa_detail'),
    
    path('ninjas-tecnicas/', views.ninja_tecnica_list, name='ninjas-tecnicas'),
    path('ninjas-tecnicas/<str:pk>/', views.ninja_tecnica_detail, name='ninja-tecnica_detail'),
    
    path('bestias-miticas/', views.bestia_mitica_list, name='bestias-miticas'),
    path('bestias-miticas/<str:pk>/', views.bestia_mitica_detail, name='bestia-mitica_detail'),
    
    path('equipos/', views.equipo_list, name='equipos'),
    path('equipos/<str:pk>/', views.equipo_detail, name='equipo_detail'),
    
    path('misiones/', views.mision_list, name='misiones'),
    path('misiones/<str:pk>/', views.mision_detail, name='mision_detail'),
    
    path('equipos-en-misiones/', views.equipo_en_mision_list, name='equipos-en-misiones'),
    path('equipos-en-misiones/<str:pk>/', views.equipo_en_mision_detail, name='equipo-en-mision_detail'),
    
    path('pergaminos/', views.pergamino_list, name='pergaminos'),
    path('pergaminos/<str:pk>/', views.pergamino_detail, name='pergamino_detail'),
    
    path('equipos-en-misiones-pergaminos/', views.equipo_en_mision_pergamino_list, name='equipos-en-misiones-pergaminos'),
    path('equipos-en-misiones-pergaminos/<str:pk>/', views.equipo_en_mision_pergamino_detail, name='equipo-en-mision-pergamino_detail'),
    
    path('bestias-misiones-pergaminos/', views.bestia_mision_pergamino_list, name='bestias-misiones-pergaminos'),
    path('bestias-misiones-pergaminos/<str:pk>/', views.bestia_mision_pergamino_detail, name='bestia-mision-pergamino_detail'),
]
