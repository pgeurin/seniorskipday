from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)
classroom_stats = pd.read_csv('../data_january/classroom_stats.csv')
classroom_stats['Probabilty Zero Posts for next 6 months'] = classroom_stats[
    'Probabilty Zero Posts for next 6 months'].apply(
        lambda x: round(x, 2))
classroom_stats = classroom_stats.rename(columns={
    'Probabilty Zero Posts for next 6 months': 'Prob 0 posts 6 months',
    'post_per_lesson_aka_popularity_mean': 'Lesson Popularity',
    'classroom_id': "Classroom ID",
    'school_id_unique': 'School ID'})
classroom_stats = classroom_stats.drop('school_id_mean', axis=1)
lists_classroom_stats = [
    list(classroom_stats[i].values) for i in classroom_stats]


@app.route('/', methods=['GET'])
def index():
    return render_template('index_classrooms_in_danger.html', data=zip(*lists_classroom_stats), columns=list(classroom_stats.columns))


@app.route('/search', methods=['POST'])
def get_search():
    user_data = request.json
    classroom_id = user_data['classroom_id']
    classroom_stat = classroom_stats.loc[classroom_id].tolist()
    stat_labels = list(classroom_stats.columns)
    return jsonify({'classroom_stat': classroom_stat,
                    'stat_labels': stat_labels})


def main():
    app.run(host='0.0.0.0', port=8080, debug=True)


if __name__ == '__main__':
    main()
