from django.shortcuts import render, get_object_or_404

from rest_framework import serializers
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ClienteSend
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from django.http import Http404
from .forms import ConsultaForm






class ClienteView(APIView):
    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404 

    def get(self, request, pk=None,format=None, *args, **kwargs):
        if pk: 
            cliente = self.get_object(pk)
            serializer = ClienteSerializer(cliente)

            return Response(serializer.data)
        else: 
            cliente = Cliente.objects.all()
            serializer = ClienteSerializer(cliente, many = True)

            return Response(serializer.data)  

    def post(self, request):
        serializer = ClienteSend(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk, format=None):
        cliente = self.get_object(pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class MascotaView(APIView):
    def get_object(self, pk):
        try:
            return Mascota.objects.get(pk=pk)
        except Mascota.DoesNotExist:
            raise Http404 
    def get(self, request, pk=None,format=None, *args, **kwargs):
        if pk: 
            mascota = self.get_object(pk)
            serializer = MascotaSerializer(mascota)

            return Response(serializer.data)
        else: 
            mascota = Mascota.objects.all()
            serializer = MascotaSerializer(mascota, many = True)

            return Response(serializer.data)

    def post(self, request):
        serializer = MascotaSend(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        mascota = self.get_object(pk)
        serializer = MascotaSerializer(mascota, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk, format=None):
        mascota = self.get_object(pk)
        mascota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class ConsultaView(APIView):

    def get_object(self, pk):
        try:
            return Consulta.objects.get(pk=pk)
        except Consulta.DoesNotExist:
            raise Http404 

    def get(self, request, pk=None,format=None, *args, **kwargs):
        if pk: 
            consulta = self.get_object(pk)
            serializer = ConsultaSerializer(consulta)

            return Response(serializer.data)
        else: 
            consulta = Consulta.objects.all()
            serializer = ConsultaSerializer(consulta, many = True)

            return Response(serializer.data)

    def post(self, request):
        serializer = ConsultaSend(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, pk, format=None):
        consulta = self.get_object(pk)
        serializer = ConsultaSerializer(consulta, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk, format=None):
        consulta = self.get_object(pk)
        consulta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def getConsultas(request):
    consultas = Consulta.objects.all()
    return render(request, "consultas.html", {"consultas": consultas})

def addConsulta(request):
    if request.method == "POST":
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultas')

    else: 
        form = ConsultaForm()

    return render(request, "form_consulta.html", {"form": form})


def upConsulta(request, id):
    consulta = get_object_or_404(Consulta, pk=id)
    if request.method == "POST":
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('consultas')

    else: 
        form = ConsultaForm(instance=consulta)

    return render(request, "form_consulta.html", {"form": form})

def eliminar_consultas(request, id):
    consulta = get_object_or_404(Consulta, id=id)  
    consulta.delete()  
    return redirect('consultas')



class VeterinarioView(APIView):

    def get_object(self, pk):
        try:
            return Veterinario.objects.get(pk=pk)
        except Veterinario.DoesNotExist:
            raise Http404 
        

    def get(self, request, pk=None,format=None, *args, **kwargs):
        if pk: 
            veterinario = self.get_object(pk)
            serializer = VetrinarioSerializer(veterinario)

            return Response(serializer.data)
        else: 
            veterinario = Veterinario.objects.all()
            serializer = VetrinarioSerializer(veterinario, many = True)

            return Response(serializer.data)
    
    def post(self, request):
        serializer = VeterinarioSend(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        veterinario = self.get_object(pk)
        serializer = VetrinarioSerializer(veterinario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        veterinario = self.get_object(pk)
        veterinario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class MedicamentoView(APIView):

    def get_object(self, pk):
        try:
            return Medicamento.objects.get(pk=pk)
        except Medicamento.DoesNotExist:
            raise Http404 

    def get(self, request, pk=None,format=None, *args, **kwargs):
        if pk: 
            medicamento = self.get_object(pk)
            serializer = MedicamentoSerializer(medicamento)

            return Response(serializer.data)
        else: 
            medicamento = Medicamento.objects.all()
            serializer = MedicamentoSerializer(medicamento, many = True)

            return Response(serializer.data)  

    def post(self, request):
        serializer = MedicamentoSend(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, pk, format=None):
        medicamento = self.get_object(pk)
        serializer = MedicamentoSerializer(medicamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk, format=None):
        medicamento = self.get_object(pk)
        medicamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)