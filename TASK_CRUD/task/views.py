from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task,Note
from .serialisers import TaskSerializer,NoteSerializer

# Create your views here.

@api_view(['GET','POST','PUT'])
def user_note(request,user):
    if request.method=='GET':
        notes=Note.objects.filter(user=user)
        notes=NoteSerializer(notes,many=True)
        return Response(notes.data)
    
    if request.method=='POST':
            try:
                data=request.data
                data['user']=user
                note_serialized=NoteSerializer(data=data)
                if note_serialized.is_valid():
                    note_serialized.save()
                    return Response(note_serialized.data,status=status.HTTP_201_CREATED)
                else:
                    return Response('Error addint note')
            except Exception as e:
                print(str(e))
                return Response(str(e))

        
@api_view(['POST'])
def add_task(request,user,note):
    if request.method=='POST':
        data=request.data
        try:
            note = Note.objects.get(user=user, id=note)
            task = Task.objects.create(content=data['content'], note=note, user=user)
            task_serialized = TaskSerializer(task)
            return Response(task_serialized.data, status=status.HTTP_201_CREATED)
        except Note.DoesNotExist:
            return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f'Error occurred: {str(e)}')
            return Response(f'Error occurred: {str(e)}', status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def modify_task(request,user,note,id):
    if request.method=='GET':
        try:
            task=Task.objects.get(note=note,id=id,user=user)
            task_serialized=TaskSerializer(task)
            return Response(task_serialized.data)
        except Exception as e:
            print(f'Error occurred: {str(e)}')
            return Response(f'Error occurred: {str(e)}', status=status.HTTP_400_BAD_REQUEST)

    if request.method=='PUT':
        try:
            data=request.data
            task=Task.objects.get(note=note,id=id,user=user)
            task_serialized=TaskSerializer(task,data=data,partial=True)
            if task_serialized.is_valid():
                task_serialized.save()
                return Response('Task Updated')
            else:
                return Response('Issue saving Task')
        except Task.DoesNotExist:
            return Response('Task does not exist')
        except Exception as e:
            print(f'Error occurred: {str(e)}')
            return Response(f'Error occurred: {str(e)}', status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='DELETE':
        try:
            data=request.data
            task=Task.objects.get(note=note,user=user,id=id)
            task.delete()
            return Response(f'Task id:{id} deleted')
        except Exception as e:
            print(f'Error occurred: {str(e)}')
            return Response(f'Error occurred: {str(e)}', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def get_note(request,user,note):
        if request.method=='GET':
            try:
                note=Note.objects.get(user=user,id=note)
                tasks=Task.objects.filter(user=user,note=note).order_by('-created_at')
                task_serialised=TaskSerializer(tasks,many=True)
                note_serialised=NoteSerializer(note)
                return Response({'title':note_serialised.data['title'],'tasks':task_serialised.data})
            except Note.DoesNotExist:
                return Response('Note does not exist')
            except Exception as e:
                print(f'Error occured:{str(e)}')
                return Response(f'Error occured:{str(e)}')
        if request.method=='PUT':
            try:
                data=request.data
                notedata=Note.objects.get(user=user,id=note)
                note_serialized=NoteSerializer(notedata,data=data,partial=True)
                if note_serialized.is_valid():
                    note_serialized.save()
                    return Response(f'Note id:{note} updated')
                else:
                    return Response('Error Updating note') 
            except Exception as e:
                print(f'error occured:{str(e)}')
                return Response(f'error occured:{str(e)}')
        if request.method=='DELETE':
            try:
                notedata=Note.objects.get(user=user,id=note)
                notedata.delete()
                return Response(f'Note id:{note} updated')
            except Exception as e:
                print(f'error occured:{str(e)}')
                return Response(f'error occured:{str(e)}')
            

    
