import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from a1_data_load import load_posts

def plot_days_with_not_zero_posts_since(posts, date):
    days_one_post_in_last_month = posts[
        posts['date']> date
        ].groupby(['classroom_id','date']).sum(
        ).groupby('classroom_id').count()
    num_posts_by_class = posts.groupby('classroom_id').count()
    days_one_post_in_last_month = num_posts_by_class.join(
        days_one_post_in_last_month,
        how='left',
        lsuffix='_num_posts_by_class',
        rsuffix='_days_one_post_in_last_month')
    days_one_post_in_last_month.loc[
        days_one_post_in_last_month[
            'exists_days_one_post_in_last_month'].isnull(
            ), 'exists_days_one_post_in_last_month'] = 0
    fig, ax = plt.subplots(1,1)
    ax.set_title(f'Days with not zero posts since {date.date()}')
    ax.hist(days_one_post_in_last_month['exists_days_one_post_in_last_month'],
            bins=30)
    ax.set_ylabel("# of classes")
    ax.set_xlabel("# of days")
    plt.show()
    return None


def plot_log_days_with_not_zero_posts_since(posts, date):
    days_one_post_in_last_month = posts[posts['date']> date].groupby(['classroom_id','date']).sum().groupby('classroom_id').count()
    num_posts_by_class = posts.groupby('classroom_id').count()
    days_one_post_in_last_month = num_posts_by_class.join(days_one_post_in_last_month, how='left', lsuffix='_num_posts_by_class', rsuffix='_days_one_post_in_last_month')
    days_one_post_in_last_month.loc[days_one_post_in_last_month['exists_days_one_post_in_last_month'].isnull(), 'exists_days_one_post_in_last_month'] = 0
    fig, ax = plt.subplots(1,1)
    ax.set_title(f'Days with not zero posts since {date.date()}')
    ax.hist(np.log(days_one_post_in_last_month['exists_days_one_post_in_last_month']+1),bins=30);
    ax.set_ylabel("# of classes")
    ax.set_xlabel("log(#) of days")
    plt.show()
    return None

def plot_days_with_not_zero_posts_between(posts, date1, date2):
    print(sum((date1 < posts['date']) & (posts['date'] < date2)))
    days_one_post_in_last_month = posts[
        (date1 < posts['date']) & (posts['date'] < date2)
        ].groupby(['classroom_id', 'date']).sum(
        ).groupby('classroom_id').count()
    num_posts_by_class = posts.groupby('classroom_id').count()
    days_one_post_in_last_month = num_posts_by_class.join(
        days_one_post_in_last_month,
        how='left',
        lsuffix='_num_posts_by_class',
        rsuffix='_days_one_post_in_last_month')
    days_one_post_in_last_month.loc[
        days_one_post_in_last_month[
            'exists_days_one_post_in_last_month'].isnull(),
        'exists_days_one_post_in_last_month'] = 0
    fig, ax = plt.subplots(1,1)
    ax.set_title(f"""Days with not zero posts between
                 {date1.date()} and {date2.date()}""")
    ax.hist(days_one_post_in_last_month['exists_days_one_post_in_last_month'],
            bins=30)
    ax.set_ylabel("# of classes")
    ax.set_xlabel("# of days")
    plt.show()
    return None


def plot_log_days_with_not_zero_posts_between(posts, date1, date2):
    print(sum((date1 < posts['date']) & (posts['date'] < date2)))
    days_one_post_in_last_month = posts[
        (date1 < posts['date']) &
        (posts['date'] < date2)
        ].groupby(['classroom_id','date']).sum(
        ).groupby('classroom_id').count()
    num_posts_by_class = posts.groupby('classroom_id').count()
    days_one_post_in_last_month = num_posts_by_class.join(
        days_one_post_in_last_month,
        how='left',
        lsuffix='_num_posts_by_class',
        rsuffix='_days_one_post_in_last_month')
    days_one_post_in_last_month.loc[days_one_post_in_last_month[
        'exists_days_one_post_in_last_month'].isnull(),
                                    'exists_days_one_post_in_last_month'] = 0
    fig, ax = plt.subplots(1,1)
    ax.set_title(f"""Days with not zero posts between
                 {date1.date()} and {date2.date()}""")
    ax.hist(np.log(days_one_post_in_last_month[
        'exists_days_one_post_in_last_month']+1), bins=30)
    ax.set_ylabel("# of classes")
    ax.set_xlabel("# of days")
    plt.show()
    return None

def all_posts_since(posts):
    plot_days_with_not_zero_posts_since(posts,
                                        pd.to_datetime("feb 15 2018"))
    plot_log_days_with_not_zero_posts_since(posts,
                                            pd.to_datetime("feb 15 2018"))
    plot_days_with_not_zero_posts_since(posts,
                                        pd.to_datetime("feb 15 2011"))
    plot_log_days_with_not_zero_posts_since(posts,
                                            pd.to_datetime("feb 15 2011"))
    plot_days_with_not_zero_posts_between(posts,
                                         pd.to_datetime("Feb 15 2018"),
                                         pd.to_datetime("Feb 16 2018"))
    plot_days_with_not_zero_posts_between(posts,
                                          pd.to_datetime("Jan 15 2018"),
                                          pd.to_datetime("Feb 15 2018"))
    plot_log_days_with_not_zero_posts_between(posts,
                                              pd.to_datetime("Dec 15 2017"),
                                              pd.to_datetime("Jan 15 2018"))
    plot_days_with_not_zero_posts_between(posts, pd.to_datetime("Jan 15 2018"),
                                          pd.to_datetime("Feb 15 2018"))
    plot_log_days_with_not_zero_posts_between(posts,
                                              pd.to_datetime("FEB 15 2018"),
                                              pd.to_datetime("March 15 2018"))

def main():
    posts = load_posts()
    plot_days_with_not_zero_posts_since(posts,
                                        pd.to_datetime("feb 15 2018"))
    plot_log_days_with_not_zero_posts_since(posts,
                                            pd.to_datetime("feb 15 2018"))
    plot_days_with_not_zero_posts_since(posts,
                                        pd.to_datetime("feb 15 2011"))
    plot_log_days_with_not_zero_posts_since(posts,
                                            pd.to_datetime("feb 15 2011"))
    plot_days_with_not_zero_posts_between(posts,
                                         pd.to_datetime("Feb 15 2018"),
                                         pd.to_datetime("Feb 16 2018"))
    plot_days_with_not_zero_posts_between(posts,
                                          pd.to_datetime("Jan 15 2018"),
                                          pd.to_datetime("Feb 15 2018"))
    plot_log_days_with_not_zero_posts_between(posts,
                                              pd.to_datetime("Dec 15 2017"),
                                              pd.to_datetime("Jan 15 2018"))
    plot_days_with_not_zero_posts_between(posts, pd.to_datetime("Jan 15 2018"),
                                          pd.to_datetime("Feb 15 2018"))
    plot_log_days_with_not_zero_posts_between(posts,
                                              pd.to_datetime("FEB 15 2018"),
                                              pd.to_datetime("March 15 2018"))
    return None

if __name__ == '__main__':
      main()
