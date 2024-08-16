from flask import Flask, render_template
from routes.home import home_route
from routes.moedas import moeda_route

#Inicialização
app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(moeda_route, url_prefix='/moeda')


#execução
app.run(debug=True)