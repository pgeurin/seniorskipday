from flask import Flask, render_template, request, jsonify
# import psycopg2
from math import sqrt
# from load_data import process_data
# from build_rf import FraudDetector
import pickle
import pandas as pd
from random import random
import matplotlib.pyplot as plt
from io import BytesIO

app = Flask(__name__)

classroom_stats = pd.read_csv('../data/classroom_stats.csv')
lists_classroom_stats = [list(classroom_stats[i].values) for i in classroom_stats]
# load the model
# model = pickle.load(open("../static/fd.pkl", "rb"))


@app.route('/', methods=['GET'])
def index():
    return render_template('index_classrooms_in_danger.html', data=zip(*lists_classroom_stats), columns=list(classroom_stats.columns))


@app.route('/search', methods=['POST'])
def get_search():
    user_data = request.json
    classroom_id = user_data['classroom_id']
    return jsonify({'root_1': classroom_id, 'root_2': classroom_id})


@app.route('/solve', methods=['POST'])
def solve():
    user_data = request.json
    a, b, c = user_data['a'], user_data['b'], user_data['c']
    root_1, root_2 = _solve_quadratic(a, b, c)
    return jsonify({'root_1': root_1, 'root_2': root_2})


def _solve_quadratic(a, b, c):
    disc = b*b - 4*a*c
    root_1 = (-b + sqrt(disc))/(2*a)
    root_2 = (-b - sqrt(disc))/(2*a)
    return root_1, root_2


def main():
    app.run(host='0.0.0.0', port=8080, debug=True)


if __name__ == '__main__':
    main()
