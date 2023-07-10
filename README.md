# Api_galeria

Esta é uma API desenvolvida em Django com Django Rest Framework que possui recursos para criar e verificar usuários no banco de dados, além de permitir o upload de planilhas com informações de usuários.

# Funcionalidades
Autenticação JWT: Os usuários podem se autenticar na API usando o padrão JWT (JSON Web Token).
Criação de Usuários: A API permite a criação de novos usuários, com informações como nome, email e senha.
Verificação de Usuários: É possível verificar os detalhes de um usuário existente no banco de dados.
Upload de Planilhas: Os usuários podem fazer o upload de planilhas contendo informações de usuários em formato CSV ou Excel. Os dados da planilha são processados e armazenados no banco de dados.

Siga as instruções abaixo para executar a API em seu ambiente de desenvolvimento:

1. Instale as dependências do projeto: "pip install -r requirements.txt"
2. Execute as migrações do banco de dados: "python manage.py migrate"
3. Inicie o servidor de desenvolvimento do Django: "python manage.py runserver"

# Criando usuario para Token:
1. Crie um superusuário para acessar o painel de administração: "python manage.py createsuperuser"
2. Para obter um token JWT válido, faça uma requisição POST para a rota /token/ com as credenciais do superusuário (nome de usuário e senha) no corpo da requisição. O token será retornado na resposta.
3. Para atualizar um token expirado, faça uma requisição POST para a rota /token/refresh/ com o token expirado no corpo da requisição. O novo token será retornado na resposta.

# Observações
1. Certifique-se de configurar corretamente as variáveis de ambiente, como a chave secreta (SECRET_KEY) e as configurações do banco de dados, antes de executar a API em um ambiente de produção.
2. Para autenticação JWT, as rotas /token/ e /token/refresh/ estão disponíveis para obtenção e atualização do token JWT.
3. Para fazer o upload de uma planilha, use a rota /usuarios/upload-planilha/ e envie o arquivo de planilha com a chave planilha no corpo da requisição POST.

# Public
No diretorio Public tem uma Planilha para testes e Imagens do funcionamento e testes da Api.
   



