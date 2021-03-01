from cat_client import call_cat
from dog_client import call_dog

from cat_analysis_client import analyze_cat
from flask import Flask, jsonify
from google.protobuf.json_format import MessageToDict


app = Flask(__name__)


@app.route('/cat/<string:cat_name>')
def get_cat_meaw(cat_name):
    response = call_cat(cat_name)
    return jsonify(MessageToDict(response))


@app.route('/dog/<string:dog_name>')
def get_dog_barking(dog_name):
    response = call_dog(dog_name)
    return jsonify(MessageToDict(response))

@app.route('/analyze/<string:cat_name>')
def get_cat_analysis(cat_name):
    response = analyze_cat(cat_name)
    return jsonify(MessageToDict(response))

app.run()
