from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Todos los serializadores
from api.serializers.PersonaSerializer import PersonaSerializer
from api.serializers.NinjaSerializer import NinjaSerializer
from api.serializers.GeninSerializer import GeninSerializer
from api.serializers.ChuninSerializer import ChuninSerializer
from api.serializers.TecnicaSerializer import TecnicaSerializer
from api.serializers.TecnicaCurativaSerializer import TecnicaCurativaSerializer
from api.serializers.TecnicaAtaqueSerializer import TecnicaAtaqueSerializer
from api.serializers.NinjaMedicoSerializer import NinjaMedicoSerializer
from api.serializers.NinjaTecnicaSerializer import NinjaTecnicaSerializer
from api.serializers.EquipoSerializer import EquipoSerializer
from api.serializers.BestiaMiticaSerializer import BestiaMiticaSerializer
from api.serializers.BestiaMisionPergaminoSerializer import BestiaMisionPergaminoSerializer
from api.serializers.EquipoEnMisionSerializer import EquipoEnMisionSerializer
from api.serializers.EquipoEnMisionPergaminoSerializer import EquipoEnMisionPergaminoSerializer
from api.serializers.JouninSerializer import JouninSerializer
from api.serializers.MisionSerializer import MisionSerializer
from api.serializers.PergaminoSerializer import PergaminoSerializer

# Todos los modelos
from api.models.Persona import Persona
from api.models.Ninja import Ninja
from api.models.Genin import Genin
from api.models.Chunin import Chunin
from api.models.Tecnica import Tecnica
from api.models.TecnicaCurativa import TecnicaCurativa
from api.models.TecnicaAtaque import TecnicaAtaque
from api.models.NinjaMedico import NinjaMedico
from api.models.NinjaTecnica import NinjaTecnica
from api.models.Equipo import Equipo
from api.models.BestiaMitica import BestiaMitica
from api.models.BestiaMisionPergamino import BestiaMisionPergamino
from api.models.EquipoEnMision import EquipoEnMision
from api.models.EquipoEnMisionPergamino import EquipoEnMisionPergamino
from api.models.Jounin import Jounin
from api.models.Mision import Mision
from api.models.Pergamino import Pergamino

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Persona-List': '/personas/',
        'Persona-Detail': '/personas/<str:pk>',

        'Ninja-List': '/ninjas/',
        'Ninja-Detail': '/ninjas/<str:pk>',
        
        'Genin-List': '/genins/',
        'Genin-Detail': '/genins/<str:pk>',
        
        'Chunin-List': '/chunins/',
        'Chunin-Detail': '/chunins/<str:pk>',
        
        'Jounin-List': '/jounins/',
        'Jounin-Detail': '/jounins/<str:pk>',
        
        'Tecnica-List': '/tecnicas/',
        'Tecnica-Detail': '/tecnicas/<str:pk>',
        
        'Tecnica-Ataque-List': '/tecnicas-ataque/',
        'Tecnica-Ataque-Detail': '/tecnicas-ataque/<str:pk>',
        
        'Tecnica-Curativa-List': '/tecnicas-curativas/',
        'Tecnica-Curativa-Detail': '/tecnicas-curativas/<str:pk>',
        
        'Ninja-Tecnica-List': '/ninjas-tecnicas/',
        'Ninja-Tecnica-Detail': '/ninjas-tecnicas/<str:pk>',
        'Bestia-Mitica-List': '/bestias-miticas/', 'Bestia-Mitica-Detail': '/bestias-miticas/<str:pk>',
        
        'Equipo-List': '/equipos/',
        'Equipo-Detail': '/equipos/<str:pk>',
        
        'Mision-List': '/misiones/',
        'Mision-Detail': '/misiones/<str:pk>',
        
        'Equipo-En-Mision-List': '/equipos-en-misiones/',
        'Equipo-En-Mision-Detail': '/equipos-en-misiones/<str:pk>',
        
        'Pergamino-List': '/pergaminos/',
        'Pergamino-Detail': '/pergaminos/<str:pk>',
        
        'Equipo-En-Mision-Pergamino-List': '/equipos-en-misiones-pergaminos/',
        'Equipo-En-Mision-Pergamino-Detail': '/equipos-en-misiones-pergaminos/<str:pk>',
        
        'Bestia-Mision-Pergamino-List': '/bestias-misiones-pergaminos/',
        'Bestia-Mision-Pergamino-Detail': '/bestias-misiones-pergaminos/<str:pk>',
    }
    return Response(api_urls)

def get_post(request, clase, serializador):
    if request.method == 'GET':
        objects = clase.objects.all()
        serializer = serializador(objects, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializador(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def get_put_delete(request, pk, clase, serializador):
    try:
        objeto = clase.objects.get(id=pk)
    except Exception as e:
        raise e
    if request.method == 'GET':
        serializer = serializador(objeto, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        #instance=task
        serializer = serializador(objeto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        objeto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def female_medical_ninjas(request,class_,serializador):
    female_medical_ninjas=NinjaMedico.objects.filter(sexo='F')
    medical_ninjas=NinjaMedico.objects.all()
    percent=(len(female_medical_ninjas) * 100) / len(medical_ninjas)
    
def captain_in_C_rank_missions(request, class_, serializador):
    team_on_mission=EquipoEnMision.objects.all()
    captain_missions=[(item.capitan,item.mision) for item in team_on_mission
                     if item.mision.rango== 'B' or item.mision.rango=='A' or item.mision.rango=='S']
    dicc=dict()
    for item in captain_missions:
        if dicc.has_key(item[0]):
            dicc[item[0]]=dicc[item[0]]+1
        else:
            dicc.setdefault(item[0],1)
    captain_list={captain for (captain,missions) in dicc.items() if missions>3}
    
def ninja_invocation_in_S_rank_missions(request, class_,serializador):
    team_on_mission=EquipoEnMision.objects.all()
    ninjas_S_rank_missions=[(item.equipo,item.capitan) for item in team_on_mission if item.mision.rango==S]
    dicc=dict()
    for item in ninjas_S_rank_missions:
        if dicc.has_key(item[0].ninja1):
            dicc[item[0].ninja1]=dicc[item[0].ninja1]+1
        else:
            dicc.setdefault(item[0].ninja1,1)
        if dicc.has_key(item[0].ninja2):
            dicc[item[0].ninja2]=dicc[item[0].ninja2]+1
        else:
            dicc.setdefault(item[0].ninja2,1)
        if dicc.has_key(item[0].ninjamedico):
            dicc[item[0].ninjamedico]=dicc[item[0].ninjamedico]+1
        else:
            dicc.setdefault(item[0].ninjamedico,1)
        if dicc.has_key(item[1]):
            dicc[item[1]]=dicc[item[1]]+1
        else:
            dicc.setdefault(item[1],1)
    ninjas=[ninja for (ninja,missions) in dicc.items() if missions>6]
    ninjas_invocation=[(item.invocador.nombre,item.invocador.clan,item.nombre) for item in BestiaMitica if ninjas.__contains__(item.invocador)]

def hidden_techniques(request,class_,serializador):
    foreign_missions=EquipoEnMision.objects.filter(mision_in=[mision.id for mision in Mision.objects.filter(~Q(pais_cliente="Konoa"))])
    ocult_technique=NinjaTecnica.objects.filter(tecnica_in=[tecnica.id for tecnica in Tecnica.objects.filter(es_oculta=True)])
    dicc=dict()
    for (ninja,tecnica) in ocult_technique:
        for item in foreign_missions:
            if item.capitan==ninja:
                if dicc.has_key(item.capitan):
                    dicc[item.capitan].add(tecnica)
                else:
                    dicc.setdefault(item.capitan,tecnica)
            elif item.equipo.ninja1==ninja:
                if dicc.has_key(item.equipo.ninja1):
                    dicc[item.equipo.ninja1].add(tecnica)
                else:
                    dicc.setdefault(item.equipo.ninja1,tecnica)
            elif item.equipo.ninja2==ninja:
                if dicc.has_key(item.equipo.ninja2):
                    dicc[item.equipo.ninja2].add(tecnica)
                else:
                    dicc.setdefault(item.equipo.ninja2,tecnica)
            elif item.equipo.ninjamedico==ninja:
                if dicc.has_key(item.equipo.ninjamedico):
                    dicc[item.equipo.ninjamedico].add(tecnica)
                else:
                    dicc.setdefault(item.equipo.ninjamedico,tecnica)
    hidden_techn=dicc.values()
            
def medical_ninja_captains(request,class_,serializador):
    medical_ninja=NinjaMedico.objects.all()
    team_on_mission=EquipoEnMision.objects.all()
    medical_captain=[item.capitan for item in team_on_mission if medical_ninja.__contains__(item.capitan)]

def highest_reward_missions(request, class_, serializador):
    satisfactory_mission=EquipoEnMision.objects.filter(resultado='S').order_by(mision.recompensa)
    missions=satisfactory_mission.values_list('mision',flat=True).order_by('recompensa')


#personas
@api_view(['GET','POST'])
def persona_list(request):
    return get_post(request, Persona, PersonaSerializer)
@api_view(['GET','PUT','DELETE'])
def persona_detail(request,pk):
    return get_put_delete(request, pk, Persona, PersonaSerializer)

#ninjas
@api_view(['GET','POST'])
def ninja_list(request):
    return get_post(request, Ninja, NinjaSerializer)
@api_view(['GET','PUT','DELETE'])
def ninja_detail(request,pk):
    return get_put_delete(request, pk, Ninja, NinjaSerializer)

#genins
@api_view(['GET','POST'])
def genin_list(request):
    return get_post(request, Genin, GeninSerializer)
@api_view(['GET','PUT','DELETE'])
def genin_detail(request,pk):
    return get_put_delete(request, pk, Genin, GeninSerializer)

#chunins
@api_view(['GET','POST'])
def chunin_list(request):
    return get_post(request, Chunin, ChuninSerializer)
@api_view(['GET','PUT','DELETE'])
def chunin_detail(request,pk):
    return get_put_delete(request, pk, Chunin, ChuninSerializer)

#jounins
@api_view(['GET','POST'])
def jounin_list(request):
    return get_post(request, Jounin, JouninSerializer)
@api_view(['GET','PUT','DELETE'])
def jounin_detail(request,pk):
    return get_put_delete(request, pk, Jounin, JouninSerializer)

#tecnicas
@api_view(['GET','POST'])
def tecnica_list(request):
    return get_post(request, Tecnica, TecnicaSerializer)
@api_view(['GET','PUT','DELETE'])
def tecnica_detail(request,pk):
    return get_put_delete(request, pk, Tecnica, TecnicaSerializer)

#tecnicas ataque
@api_view(['GET','POST'])
def tecnica_ataque_list(request):
    return get_post(request, TecnicaAtaque, TecnicaAtaqueSerializer)
@api_view(['GET','PUT','DELETE'])
def tecnica_ataque_detail(request,pk):
    return get_put_delete(request, pk, TecnicaAtaque, TecnicaAtaqueSerializer)

#tecnicas ataque
@api_view(['GET','POST'])
def ninja_medico_list(request):
    return get_post(request, NinjaMedico, NinjaMedicoSerializer)
@api_view(['GET','PUT','DELETE'])
def ninja_medico_detail(request,pk):
    return get_put_delete(request, pk, NinjaMedico, NinjaMedicoSerializer)

#tecnicas curativas
@api_view(['GET','POST'])
def tecnica_curativa_list(request):
    return get_post(request, TecnicaCurativa, TecnicaCurativaSerializer)
@api_view(['GET','PUT','DELETE'])
def tecnica_curativa_detail(request,pk):
    return get_put_delete(request, pk, TecnicaCurativa, TecnicaCurativaSerializer)

#ninja tecnicas
@api_view(['GET','POST'])
def ninja_tecnica_list(request):
    return get_post(request, NinjaTecnica, NinjaTecnicaSerializer)
@api_view(['GET','PUT','DELETE'])
def ninja_tecnica_detail(request,pk):
    return get_put_delete(request, pk, NinjaTecnica, NinjaTecnicaSerializer)

#bestias miticas
@api_view(['GET','POST'])
def bestia_mitica_list(request):
    return get_post(request, BestiaMitica, BestiaMiticaSerializer)
@api_view(['GET','PUT','DELETE'])
def bestia_mitica_detail(request,pk):
    return get_put_delete(request, pk, BestiaMitica, BestiaMiticaSerializer)

#equipos
@api_view(['GET','POST'])
def equipo_list(request):
    return get_post(request, Equipo, EquipoSerializer)
@api_view(['GET','PUT','DELETE'])
def equipo_detail(request,pk):
    return get_put_delete(request, pk, Equipo, EquipoSerializer)

#misiones
@api_view(['GET','POST'])
def mision_list(request):
    return get_post(request, Mision, MisionSerializer)
@api_view(['GET','PUT','DELETE'])
def mision_detail(request,pk):
    return get_put_delete(request, pk, Mision, MisionSerializer)

#equipos en misiones
@api_view(['GET','POST'])
def equipo_en_mision_list(request):
    return get_post(request, EquipoEnMision, EquipoEnMisionSerializer)
@api_view(['GET','PUT','DELETE'])
def equipo_en_mision_detail(request,pk):
    return get_put_delete(request, pk, EquipoEnMision, EquipoEnMisionSerializer)

#pergaminos
@api_view(['GET','POST'])
def pergamino_list(request):
    return get_post(request, Pergamino, PergaminoSerializer)
@api_view(['GET','PUT','DELETE'])
def pergamino_detail(request,pk):
    return get_put_delete(request, pk, Pergamino, PergaminoSerializer)

#Equipos en mision pergaminos
@api_view(['GET','POST'])
def equipo_en_mision_pergamino_list(request):
    return get_post(request, EquipoEnMisionPergamino, EquipoEnMisionPergaminoSerializer)
@api_view(['GET','PUT','DELETE'])
def equipo_en_mision_pergamino_detail(request,pk):
    return get_put_delete(request, pk, EquipoEnMisionPergamino, EquipoEnMisionPergaminoSerializer)

#bestias misiones pergamino
@api_view(['GET','POST'])
def bestia_mision_pergamino_list(request):
    return get_post(request, BestiaMisionPergamino, BestiaMisionPergaminoSerializer)
@api_view(['GET','PUT','DELETE'])
def bestia_mision_pergamino_detail(request,pk):
    return get_put_delete(request, pk, BestiaMisionPergamino, BestiaMisionPergaminoSerializer)
