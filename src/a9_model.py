import pandas as pd
import datetime
from datetime import timedelta
from a1_data_load import load_posts, load_classrooms
from a7_post_aggr import posts_between
import autoregression
import pickle

def get_posts_total_between_with_zeros(posts, now, six_months):
    # posts_next_semester = posts_between(posts, now+six_months, now+one_year)
    # date1, date2 = now+six_months, now+one_year
    date1, date2 = now, now + six_months
    last_month_posts = posts[(date1 < posts['date']) & (posts['date'] < date2)].groupby('classroom_id').count()
    num_posts_by_class = posts.groupby('classroom_id').sum()
    last_month_posts_total= num_posts_by_class.join(last_month_posts, how='left', lsuffix='_num_posts_by_class', rsuffix='_last_month_posts')
    last_month_posts_total.loc[last_month_posts_total['post_id_last_month_posts'].isnull(),'exists_last_month_posts'] = 0
    return last_month_posts_total


# y = posts_between(posts, now+six_months, now+one_year)['exists_last_month_posts']
def make_y_was_any_posts_between(posts, classrooms, now, then):
    y = posts_between(posts, now, now+then)['exists_last_month_posts']
    empty_posts = pd.Series([0]*len(classrooms.classroom_id.unique()),index=classrooms.classroom_id.unique())
    full_y = empty_posts.add(y, fill_value=0)
    return full_y, y


def find_y_hearts(posts, now):
    #     the min of last three # posts/month is greater than 50
    # the min of last three # posts/month is greater than 200
    # the min of least month is greater than zero
    # the min of least WEEK is greater than zero (so one post every week)
    # the least month is more than a fourth of the greatest month. (again, over the last three months)
    #ERROR HERE: posts_between returns a SERIES of posts with classroom-id
    #    posts = posts.groupby('date').sum()
    three_months = timedelta(days=90)
    one_month = timedelta(days=30)
    one_week = timedelta(days=7)
    posts_last_three_months = posts_between(posts, now - three_months, now)['exists_last_month_posts']
    first_month = posts_between(posts, now - three_months, now - one_month - one_month)['exists_last_month_posts']
    second_month = posts_between(posts, now- one_month - one_month, now- one_month)['exists_last_month_posts']
    third_month = posts_between(posts, now - one_month, now)['exists_last_month_posts']
    last_week = posts_between(posts, now - one_week, now)['exists_last_month_posts']
    print(first_month)
    min_of_last_three_greater_fifty = (min(first_month, second_month, third_month) > 50)
    min_of_last_three_greater_two_hundred = (min(first_month, second_month, third_month) > 200)
    min_of_least_month_greater_zero = first_month > 0
    min_of_least_WEEK_is_greater_than_zero = len(last_week) > 0
    least_month_more_than_fourth_of_the_greatest = ( (4 * (min(first_month, second_month, third_month)) > (max(first_month, second_month, third_month))))
    stars = min_of_last_three_greater_fifty + min_of_last_three_greater_two_hundred + min_of_least_month_greater_zero + min_of_least_WEEK_is_greater_than_zero + least_month_more_than_fourth_of_the_greatest
    return (min_of_last_three_greater_fifty, min_of_last_three_greater_two_hundred, min_of_least_month_greater_zero, min_of_least_WEEK_is_greater_than_zero, least_month_more_than_fourth_of_the_greatest)


def get_all_y_hearts(posts, now):
    y_hearts=np.ones(len(posts['classroom_id'].unique()))
    for i, classroom_id in enumerate(posts['classroom_id'].unique()):
        y_hearts[i] = sum(find_y_hearts(posts[posts['classroom_id']==classroom_id], now))
    y_hearts = pd.Series(y_hearts, index=posts['classroom_id'].unique())
    return y_hearts


def make_classrooms_merged_before(classrooms_merged, now):
    classrooms_merged['date'] = pd.to_datetime(classrooms_merged['date'])
    classrooms_merged_before_now = classrooms_merged[classrooms_merged['date']<now]
    return classrooms_merged_before_now


def drop_collumns(classrooms_merged_before):
    classrooms_merged_before_dropped = classrooms_merged_before.drop('inactive', axis=1).drop('post_id_y', axis=1).drop('Unnamed: 0', axis=1)
    return classrooms_merged_before_dropped



def make_classrooms_sum_(classrooms_merged, full_y):
    classrooms_sum_ = classrooms_merged.groupby('classroom_id').sum()
    print(len(full_y))
    print(len(classrooms_sum_))
    classrooms_sum_['will_post_next_semester'] = (full_y>0)
    return classrooms_sum_


def make_classrooms_sum_hearts_before_now(classrooms_merged_before_now, y_hearts):
    classrooms_sum_before_now = classrooms_merged_before_now.groupby('classroom_id').sum()
    classrooms_sum_before_now['hearts'] = y_hearts
    return classrooms_sum_before_now


def check_merge_lengths(classrooms, classrooms_merged, posts, classrooms_merged_before_now_dropped, classrooms_sum_before_now, y, full_y):
    unique_classrooms = len(classrooms.classroom_id.unique())
    unique_classroms_merged = len(classrooms_merged.classroom_id.unique()),
    num_y = len(y)
    unique_posts = len(posts.classroom_id.unique())
    num_full_y = len(full_y)
    unique_classrooms_merged_before_now_dropped = len(classrooms_merged_before_now_dropped.classroom_id.unique())
    unique_classrooms_sum_before_now = len(classrooms_sum_before_now.index.unique())
    return unique_classrooms, unique_classroms_merged, num_y, unique_posts, num_full_y, unique_classrooms_merged_before_now_dropped, unique_classrooms_sum_before_now


def merged_to_sum_before(classrooms_merged, now, y):
    classrooms_merged_before = make_classrooms_merged_before(classrooms_merged, now)
    classrooms_merged_before_dropped = drop_collumns(classrooms_merged_before)
    classrooms_sum_before_dropped = make_classrooms_sum_(classrooms_merged_before_dropped, y)
    return classrooms_sum_before_dropped


def main():
    posts = load_posts()
    classrooms = load_classrooms()
    posts['year_month'] = pd.to_datetime(posts['date']).map(lambda dt: dt.replace(day=1))
    classrooms_merged = pd.read_csv('../data_january/classrooms_merged_non_leak.csv')
    now = pd.to_datetime('September 24, 2017')
    six_months = timedelta(days=365//2)
    # one_year = timedelta(days=365)
    last_month_posts_total = get_posts_total_between_with_zeros(posts, now, six_months)
    full_y, y = make_y_was_any_posts_between(posts, classrooms, now, six_months)
    # print(find_y_hearts(posts, now))
    # print(find_y_hearts(posts[posts['classroom_id']==1 | posts['classroom_id']==3], now))
    # y_hearts = get_all_y_hearts(posts, now)
    classrooms_merged_before_now = make_classrooms_merged_before(classrooms_merged, now)
    classrooms_merged_before_three_months_ago = make_classrooms_merged_before(classrooms_merged, now-timedelta(days=90))
    classrooms_merged_before_now_dropped = drop_collumns(classrooms_merged_before_now)
    classrooms_merged_before_three_months_ago = drop_collumns(classrooms_merged_before_three_months_ago)
    classrooms_sum_before_now = make_classrooms_merged_before(classrooms_merged, now)
    classrooms_sum_before_now_dropped = make_classrooms_merged_before(classrooms_merged_before_now_dropped, now)
    classrooms_sum_before_three_months_ago = make_classrooms_merged_before(classrooms_merged_before_three_months_ago, now)
    check_merge_lengths(classrooms, classrooms_merged, posts, classrooms_merged_before_now_dropped, classrooms_sum_before_now, y, full_y)

    classrooms_sum_before_three_months_ago = make_classrooms_sum_(classrooms_merged_before_three_months_ago, full_y)
    classrooms_sum_before_now = make_classrooms_sum_(classrooms_merged, full_y)
    # classrooms_sum_hearts_before_three_months_ago = merged_to_sum_before(classrooms_merged, now-timedelta(days=90), y_hearts)
    # classrooms_sum_hearts_before_three_months_ago = make_classrooms_sum_hearts_before_now(classrooms_merged_before_three_months_ago)
    # classrooms_sum_hearts_before_now = make_classrooms_sum_hearts_before_now(classrooms_merged)
    # names3, results3, models3, pipeline3, df_X3 = autoregression.compare_predictions(classrooms_sum_hearts_before_three_months_ago, 'will_post_next_semester')
    names2, results2, models2, pipeline2, df_X2 = autoregression.compare_predictions(classrooms_sum_before_three_months_ago, 'will_post_next_semester', corr_matrix=True,
    scatter_matrix=False, bootstrap_coefs=False,
    feature_importances=False,
    partial_dep=False, actual_vs_predicted=False,
    residuals=False, univariates=False, compare_models=False,
    ROC=False)

    output = open('random_forrest.pkl', 'wb')
    pickle.dump(models2[3], output)
    output.close()
    df_X2.to_csv('df_X2.csv')

    # PICKEL:
    # output = open('ada_boost_classifier.pkl', 'wb')
    # pickle.dump(models1[8], output)
    # output.close()

    # pickle.dump(models1[7], 'ada_boost_classifier.pkl', protocol=0)

if __name__ == "__main__":
    main()
