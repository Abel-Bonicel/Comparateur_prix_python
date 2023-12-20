import requests
from flask import Flask, render_template, request
import search

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST' :
        if request.form['search_product'] != '':
            request_search = request.form['search_product']
            return render_template('product.html', search_product = search.search_Product(request_search))
        else:
                return render_template('index.html')
    else:
        return render_template('index.html')