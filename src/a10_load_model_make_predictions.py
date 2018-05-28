import pandas as pd
import numpy as np
import pprint, pickle
from a1_data_load import load_posts, load_now
from a9_model import make_classrooms_merged_before, declare_now, drop_collumns
from datetime import timedelta

def unique_num(x):
    return len(np.unique(x))


def main():
    posts = load_posts()
    now = declare_now()
    # pkl_file = open('ada_boost_classifier.pkl', 'rb')
    # ada_boost_model = pickle.load(pkl_file)
    # pprint.pprint(ada_boost_model)
    # pkl_file.close()
    # y_hat = ada_boost_model.predict_proba(df_X1)
    # df1_y_hat = df_X1
    # df1_y_hat['y_hat'] = y_hat[:,0]
    # # classroom answers in order!!!!!!!!!!!!!!!!
    # danger_classrooms = df1_y_hat.iloc[y_hat[:,0].argsort()[::-1]]

    classrooms_merged = pd.read_csv('../data_january/classrooms_merged_non_leak.csv')
    classrooms_merged_before_now = make_classrooms_merged_before(classrooms_merged, now)
    classrooms_merged_before_now_dropped = drop_collumns(classrooms_merged_before_now)

    pkl_file = open('random_forrest.pkl', 'rb')
    random_forrest = pickle.load(pkl_file)
    pprint.pprint(random_forrest)
    pkl_file.close()
    df_X2 = pd.read_csv('df_X2.csv')
    print(df_X2.head(3))
    df_X2 = df_X2.drop('classroom_id', axis=1)
    y_hat = random_forrest.predict_proba(df_X2)
    df2_y_hat = df_X2
    df2_y_hat['y_hat'] = y_hat[:, 0]
    danger_classrooms = df2_y_hat.iloc[y_hat[:, 0].argsort()[::-1]]

    classroom_stats_before_now = classrooms_merged_before_now_dropped.groupby(
        'classroom_id').agg({
            'school_id': [np.unique],
            'post_per_lesson_aka_popularity': ['mean'],
            'exists': ['sum'],
            # 'date': np.mean,
            # 'picture_file_name': [lambda x: not np.isnan(x)]
        })
    classroom_stats_before_now.columns = classroom_stats_before_now.columns.map(
        '_'.join)
    classroom_stats_before_now.head()
    danger_classrooms.index = danger_classrooms.index.astype('int64')
    classroom_stats = danger_classrooms[['y_hat']
                                        ].merge(classroom_stats_before_now,
                                                how='left',
                                                left_index=True,
                                                right_index=True)
    classroom_stats = classroom_stats.rename(index=str,
                                             columns={"y_hat":
                                                      "Probabilty Zero Posts for next 6 months",
                                                      "exists_sum":
                                                      "# of posts"})
    last_months_post = posts[
        posts['classroom_id'].isin([24]) &
        (now - timedelta(days=30) < posts['date']) & (posts['date'] < now)
        ].groupby('classroom_id').count()['date']
    classroom_stats_with_danger_index = classroom_stats
    classroom_stats_with_danger_index['posts_in_last_month'] = last_months_post
    classroom_stats_with_danger_index['danger_index'] = classroom_stats_with_danger_index['posts_in_last_month'] * classroom_stats_with_danger_index['Probabilty Zero Posts for next 6 months']
    # classroom_stats_with_danger_index.to_csv('../data/classroom_stats_w_danger_index.csv')
    classroom_stats_with_danger_index.to_csv('../data_january/classroom_stats_w_danger_index2.csv')

if __name__ == "__main__":
    main()
