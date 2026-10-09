from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
# Necesario para usar mensajes flash (alertas de error)
app.secret_key = 'clave_secreta_revolucionaria'

# Contraseña definida por vos
CONTRASEÑA_CORRECTA = "Promo26Antigroup"

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/verificar-acceso', methods=['POST'])
def verificar_acceso():
    contraseña_ingresada = request.form.get('password')
    
    if contraseña_ingresada == CONTRASEÑA_CORRECTA:
        # Si es correcta, lo enviamos a la lista secreta
        return redirect(url_for('prohibidos'))
    else:
        # Si es incorrecta, avisa del error y recarga la página principal
        flash('Contraseña incorrecta. Acceso denegado.', 'error')
        return redirect(url_for('inicio'))

@app.route('/prohibidos')
def prohibidos():
    return render_template('prohibidos.html')

if __name__ == '__main__':
    app.run(debug=True)
