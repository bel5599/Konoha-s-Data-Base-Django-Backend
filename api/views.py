from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import BestiaMisionPergaminoLlaveSerializer, BestiaMiticaSerializer, ChuninSerializer, EquipoEnMisionPergaminoSerializer, EquipoEnMisionSerializer, EquipoSerializer, GeninSerializer, JouninSerializer, MisionSerializer, NinjaSerializer, NinjaTecnicaSerializer, PergaminoSerializer, PersonaSerializer, TaskSerializer, TecnicaAtaqueSerializer, TecnicaCurativaSerializer, TecnicaSerializer

from .models import BestiaMisionPergaminoLlave, BestiaMitica, Chunin, Equipo, EquipoEnMision, EquipoEnMisionPergamino, Genin, Jounin, Mision, Ninja, NinjaTecnica, Pergamino, Persona, Task, Tecnica, TecnicaAtaque, TecnicaCurativa
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
        
        'Bestia-Mitica-List': '/bestias-miticas/',
        'Bestia-Mitica-Detail': '/bestias-miticas/<str:pk>',
        
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

#tasks
@api_view(['GET','POST'])
def task_list(request):
    return get_post(request, Task, TaskSerializer)
@api_view(['GET','PUT','DELETE'])
def task_detail(request,pk):
    return get_put_delete(request, pk, Task, TaskSerializer)

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
    return get_post(request, BestiaMisionPergaminoLlave, BestiaMisionPergaminoLlaveSerializer)
@api_view(['GET','PUT','DELETE'])
def bestia_mision_pergamino_detail(request,pk):
    return get_put_delete(request, pk, BestiaMisionPergaminoLlave, BestiaMisionPergaminoLlaveSerializer)
