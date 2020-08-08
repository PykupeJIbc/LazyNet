from flask import request, render_template
from flask import current_app as app
from .models import db, Clients, Routers, Interfaces, Maps

@app.route('/', methods=['GET'])
def index():
    clients = Clients.query.all()
    for client in clients:
        print(client.name)
    return render_template('index.html')