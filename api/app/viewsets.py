from rest_framework import viewsets
from api.app import serializers
from api import models
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class UsuarioViewSet(viewsets.ModelViewSet):
    permission_classes=(IsAuthenticated,)

    serializer_class = serializers.UsuarioSerializer
    queryset = models.Usuario.objects.all()
 
    @action(detail=False, methods=['post'])
    def upload_planilha(self, request):
        arquivo_planilha = request.FILES.get('planilha')
 
        import pandas as pd

        try:
            # Verifica se é um arquivo CSV ou Excel
            if arquivo_planilha.name.endswith('.csv'):
                df = pd.read_csv(arquivo_planilha)
            elif arquivo_planilha.name.endswith('.xlsx'):
                df = pd.read_excel(arquivo_planilha)
            else:
                return Response({'message': 'Formato de arquivo inválido. Apenas arquivos CSV ou Excel são suportados.'}, status=400)
            
            # Itera sobre as linhas da planilha e cria ou atualiza os usuários no banco de dados
            for index, row in df.iterrows():
                id_user = row['id_user']
                nome = row['nome']
                email = row['email']
                senha = row['senha']
                
                # Cria ou atualiza o usuário no banco de dados
                usuario, created = models.Usuario.objects.update_or_create(
                    id_user=id_user,
                    defaults={'nome': nome, 'email': email, 'senha': senha}
                )
        
            return Response({'message': 'Upload da planilha realizado com sucesso!'})
        
        except Exception as e:
            return Response({'message': f'Erro ao processar a planilha: {str(e)}'}, status=400)
        