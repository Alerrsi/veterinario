from django.shortcuts import render, get_object_or_404

from rest_framework import serializers
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ClienteSend
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from django.http import Http404
from .forms import *






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
        print(serializer.errors)
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



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  # Fixed
        if user is not None:
            auth_login(request, user)  # Using imported `login` to avoid name conflict
            return redirect('inicio')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def inicio(request):
    return render(request, "inicio.html")

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

@login_required
def getConsultas(request):
    consultas = Consulta.objects.all()
    return render(request, "consultas.html", {"consultas": consultas})

@login_required
def addConsulta(request):
    if request.method == "POST":
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultas')

    else: 
        form = ConsultaForm()

    return render(request, "form_consulta.html", {"form": form})

@login_required
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

@login_required
def eliminar_consultas(request, id):
    consulta = get_object_or_404(Consulta, id=id)  
    consulta.delete()  
    return redirect('consultas')

@login_required
def getMascota(request):
    mascotas = Mascota.objects.all()
    return render(request,"mascotas.html", {"mascotas": mascotas})

@login_required
def addMascota(request):
    if request.method == "POST":
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mascotas")
    else:
        form = MascotaForm()
    return render(request, "form_mascotas.html", {"form" : form})

@login_required
def upMascota(request, id):
    mascota = get_object_or_404(Mascota, pk=id)
    if request.method == "POST":
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('mascotas')

    else: 
        form = MascotaForm(instance=mascota)

    return render(request, "form_mascotas.html", {"form": form})

@login_required
def eliminar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    mascota.delete()
    return redirect('mascotas')

@login_required
def getVeterinario(request):
    veterinarios = Veterinario.objects.all()
    return render(request, "veterinario.html" , {"veterinarios" : veterinarios})

@login_required
def addVeterinario(request):
    if request.method == "POST":
        form = VeterinarioForm(request.POST)
        if form.is_valid():
            form.save
            return redirect("veterinarios")
    else:
        form = VeterinarioForm()
    return render(request, "form_veterinario.html" , {"form": form})

@login_required    
def upVeterinario(request,id):
    veterinario = get_object_or_404(Veterinario, pk=id)
    if request.method == "POST":
        form = VeterinarioForm(request.POST, instance=veterinario)
        if form.is_valid():
            form.save()
            return redirect('veterinarios')
    else:
        form = VeterinarioForm(instance=veterinario)
    return render(request, "form_veterinario.html", {"form": form})

@login_required        
def eliminar_Veterinario(request,id):
    veterinario = get_object_or_404(Veterinario, id=id)
    veterinario.delete()
    return redirect("veterinarios")

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

@api_view(['GET'])
@login_required
def json_todo(request):
    clientes = Cliente.objects.all()
    Consultas = Consulta.objects.all()
    Mascotas = Mascota.objects.all()
    Medicamentos = Medicamento.objects.all()
    Veterinarios = Veterinario.objects.all()

    serializador_clientes = ClienteSerializer(clientes, many = True)
    serializador_Consultas = ConsultaSerializer(Consultas, many = True)
    serializador_Mascotas = MascotaSerializer(Mascotas, many = True)
    serializador_Medicamentos = MedicamentoSerializer(Medicamentos, many = True)
    serializador_Veterinarios = VetrinarioSerializer(Veterinarios, many = True)

    data = {'clientes' : serializador_clientes.data, 'consultas' : serializador_Consultas.data, "mascotas": serializador_Mascotas.data, 'medicamentos' : serializador_Medicamentos.data,
            "veterinarios" : serializador_Veterinarios.data} 
    return Response(data)

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
        print(serializer.errors)
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