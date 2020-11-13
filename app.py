from flask import Flask, request, Response, render_template , redirect, url_for
from src.model_db import (select_all_taxpayers, select_taxpayer_by_rnc, select_taxpayer_by_name, select_taxpayer_by_state)
import json
from datetime import date

app = Flask(__name__)
api_v = '/api/v1'


@app.route('/')
def home():
    return redirect(url_for('doc'))


@app.route('/doc/api')
def doc():
    
    data = request.args.get('email')
    print(data)
    return render_template("index.html")


@app.route(f'{api_v}/taxpayers', methods=['GET'])
def fetch_taxpayers():
    limit = request.args.get('limit')
    if limit:
        data = select_all_taxpayers(limit)
    else:
        data = select_all_taxpayers()
    response = json.dumps(data)
    return Response(response, mimetype='application/json')


@app.route(f'{api_v}/taxpayers/by-rnc', methods=['GET'])
def fetch_taxpayer_by_rnc():
    search = request.args.get('search')
    limit = request.args.get('limit')
    if search:

        if limit:
            data = select_taxpayer_by_rnc(search, limit)
        else:
            data = select_taxpayer_by_rnc(search)
        
        response = json.dumps(data)
        return Response(response, mimetype='application/json')
    
    return {'message': 'you must pass rnc as argument. See the Documentation'}, 400


@app.route(f'{api_v}/taxpayers/by-name', methods=['GET'])
def fetch_taxpayer_by_name():
    search = request.args.get('search')
    limit = request.args.get('limit')
    if search:

        if limit:
            data = select_taxpayer_by_name(search, limit)
        else:
            data = select_taxpayer_by_name(search)

        response = json.dumps(data)
        return Response(response, mimetype='application/json')
    
    return {'message': 'you must pass name as argument. See the Documentation'}, 400


@app.route(f'{api_v}/taxpayers/active-state', methods=['GET'])
def fetch_active_taxpayers():
    limit = request.args.get('limit')
    state = 'ACTIVO'
    if limit:
        data = select_taxpayer_by_state(state, limit)
    else:
        data = select_taxpayer_by_state(state)
    
    response = json.dumps(data)
    return Response(response, mimetype='application/json')


@app.route(f'{api_v}/taxpayers/inactive-state', methods=['GET'])
def fetch_inactive_taxpayers():
    limit = request.args.get('limit')
    state = 'NO ACTIVO'
    if limit:
        data = select_taxpayer_by_state(state, limit)
    else:
        data = select_taxpayer_by_state(state)
    
    response = json.dumps(data)
    return Response(response, mimetype='application/json')


@app.route(f'{api_v}/taxpayers/discharged-state', methods=['GET'])
def fetch_discharged_taxpayers():
    limit = request.args.get('limit')
    state = 'DADO DE BAJA'
    if limit:
        data = select_taxpayer_by_state(state, limit)
    else:
        data = select_taxpayer_by_state(state)
    
    response = json.dumps(data)
    return Response(response, mimetype='application/json')



if __name__ == "__main__":
    app.run(debug=True)








