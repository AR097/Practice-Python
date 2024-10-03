from flask import Flask, render_template, request, redirect, flash
import os
from enviar_email import enviar_email
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Configurações para uploads
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'xlsx', 'csv', 'pdf', 'docx', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Verifica as extensões permitidas
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        remetente = request.form['remetente']
        senha = request.form['senha']
        destinatario = request.form['destinatario']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']
        file = request.files['anexo']

        # Verifica se o arquivo foi enviado
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
        else:
            filepath = None

        # Chama a função de envio de e-mail
        try:
            enviar_email(
                remetente=remetente,
                senha=senha,
                destinatario=destinatario,
                assunto=assunto,
                mensagem=mensagem,
                arquivo=filepath
            )
            flash('E-mail enviado com sucesso!', 'success')
            return redirect('/')
        except Exception as e:
            flash(f'Falha ao enviar o e-mail: {e}', 'danger')
            return redirect('/')

    return render_template('index.html')

if __name__ == '__main__':
    # Cria a pasta de uploads se não existir
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
