from flask import Flask, render_template
import psycopg2

# from load_data import process_data
# from build_rf import FraudDetector
import pickle
import pandas as pd
from random import random
import matplotlib.pyplot as plt
from io import BytesIO

app = Flask(__name__)
# conn = psycopg2.connect(dbname='meetglow', user='macbookpro', password='consulting', host='localhost')
# conn = psycopg2.connect(dbname='meetglow', user='cds', password='consulting', host='localhost')
# cursor = conn.cursor()

classroom_stats = pd.read_csv('../data/classroom_stats.csv')

lists_classroom_stats = [list(classroom_stats[i].values) for i in classroom_stats]
def insert_livedata(event_data):
	cols = []
	vals = []
	for k, v in event_data.items():
		if (k != 'description' and k != 'event_published' and k != 'has_header'):
			cols.append(k)
			if (type(v) == str):
				v = ''.join(['\'',v,'\''])
			elif ((type(v) == list) or (v == 'None')):
				v = '\'NA\''
			else:

				v = str(v)
			vals.append(v)

	columns =  ','.join(cols)
	values = ','.join(vals)

	sql =  f''' INSERT INTO live_data ({columns}) VALUES ({values}); '''
	cursor.execute (sql)
	conn.commit()

def get_data():
        predicted_events = []
        cursor.execute (''' select object_id, name, org_name, org_desc, event_start, event_created, payee_name, venue_address, venue_name, predict_proba  from live_data; ''')
        results = cursor.fetchall()
        for row in results:
	        event = {}
	        event['object_id'] = row[0]
	        event['name'] = row[1]
	        event['org_name'] = row[2]
	        event['org_desc'] = row[3]
	        event['event_start'] = row[4]
	        event['event_created'] = row[5]
	        event['payee_name'] = row[6]
	        event['venue_address'] = row[7]
	        event['venue_name'] = row[8]
	        event['predict_proba'] = row[9]
	        predicted_events.append(event)

        return predicted_events

# load the model
# model = pickle.load(open("../static/fd.pkl", "rb"))


@app.route('/')
def index():
    n = 100
    x = range(n)
    y = [random() for i in x]
    # return render_template('index_classrooms_in_danger.html', data=zip(x,y))
    return render_template('index_classrooms_in_danger.html', data=zip(*lists_classroom_stats), columns=list(classroom_stats.columns))

@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/score/{event_data}')
def score(event_data):
    # transform the data (including vectorizing)
    process_data = process_data(event_data)
    return f'<h1> {predict_proba} </h1>'

    # get a prediction and add it to event_data
    predict_proba = model.predict_proba(process_data)
    event_data['predict_proba'] = predict_proba
    # store this event in the db
    insert_livedata(event_data)


@app.route('/plot.png')
def get_graph():
    plt.figure()
    n = 10
    plt.plot(range(n), [random() for i in range(n)])
    image = BytesIO()
    plt.savefig(image)
    return image.getvalue(), 200, {'Content-Type': 'image/png'}


def main():
    # load model
    # connect to db
    app.run(host='0.0.0.0', port=8080, debug=True)
    # app.run()


if __name__ == '__main__':
    main()
