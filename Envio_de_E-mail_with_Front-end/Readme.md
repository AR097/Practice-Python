# Aplicação de Envio de E-mail com Anexo
Este projeto é uma aplicação web simples desenvolvida com o framework Flask em Python. Ele permite que o usuário envie e-mails com um ou mais anexos através de uma interface web. O envio é feito utilizando o servidor SMTP do Gmail, sendo possível configurar remetente, destinatário, assunto, mensagem e anexar arquivos de diversos tipos.

<img src="https://github.com/user-attachments/assets/f173c75e-54e4-4c15-82f3-35a0a2936379" width="auto" height="300">
<img src="https://github.com/user-attachments/assets/7e5c31bf-c9fe-476a-bb7f-d5a481e3592f" width="auto" height="300">

# Funcionalidades
- Interface web para envio de e-mails.
- Suporte para anexar arquivos (como PDF, CSV, DOCX, imagens, etc.).
- Validação de tipos de arquivos permitidos.
- Feedback visual para o usuário após o envio do e-mail (sucesso ou erro).
- Exclui automaticamente o arquivo anexo após o envio, para não ocupar espaço no servidor.

# Tecnologias Utilizadas
- Python 3.x
- Flask - Framework web usado para construir a interface e gerenciar as rotas.
- smtplib - Biblioteca padrão do Python para envio de e-mails via SMTP.
- Bootstrap 4 - Para estilização simples e responsiva da interface.
- dotenv - Para carregamento de variáveis de ambiente (como as credenciais de e-mail).
- Werkzeug - Para manipulação segura de uploads de arquivos.

# Pré-requisitos
- Python 3.x
- pip - Gerenciador de pacotes do Python

# Instalação e Execução
Clone este repositório:
```
git clone https://github.com/AR097/Practice-Python/tree/main/Envio_de_E-mail_with_Front-end.git
```
Navegue até a pasta do arquivo:
```
cd Envio_de_E-mail_with_Front-end
```
Criar e ativar o ambiente Virtual
```
python3 -m venv venv
```
```
source venv/bin/activate
```
Instale as dependências do projeto
```
pip install -r requirements.txt
```
## Configuração do Gmail
Crie uma senha de aplicativo para usar a sua conta de gmail.

Crie na pasta principal do projeto o arquivo .env
Nele voce devera incluir as seguintes informações: 
```
EMAIL_REMETENTE=seuemail@gmail.com
EMAIL_SENHA=Chaveapp(mais-seguro)ouSenha
```
No arquivo .env adicione suas credenciais de e-mail no formato que conta no arquivo, (ATENÇÂO, Cuidado para nao compartilhar suas informação, Note que ao compartilhar meu projeto, retirei as informações pessoais e senciveis. *Nunca compartilhe o arquivo .env com suas informações*)

Execute a aplicação:
```
python app.py
``` 
# Uso
Acesse a página principal no navegador.
Preencha o formulário com as seguintes informações:
E-mail Remetente: Seu endereço de e-mail.
Senha ou Chave de Aplicativo: A senha ou chave de aplicativo do Gmail.
E-mail Destinatário: O destinatário do e-mail.
Assunto: Assunto do e-mail.
Mensagem: Corpo da mensagem.
Anexo: Selecione o arquivo que deseja anexar.
Clique no botão "Enviar E-mail".
Verifique a mensagem de sucesso ou erro exibida no topo da página.

# Tipos de Arquivos Permitidos
Os seguintes tipos de arquivos podem ser anexados:
- xlsx
- csv
- pdf
- docx
- png
- jpg
- jpeg
- gif
