import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot_posts_since(posts, date):
    last_month_posts = posts[posts['date']>date].groupby('classroom_id').count()
    num_posts_by_class = posts.groupby('classroom_id').sum()
    last_month_posts_total= num_posts_by_class.join(last_month_posts, how='left', lsuffix='_num_posts_by_class', rsuffix='_last_month_posts')
    last_month_posts_total.loc[last_month_posts_total['id_last_month_posts'].isnull(),'exists_last_month_posts'] =0
    fig, ax = plt.subplots(1,1)
    ax.set_title(f'class posts since {date.date()}')
    ax.hist(last_month_posts_total['exists_last_month_posts'],bins=40)
    ax.set_ylabel("# of classes")
    ax.set_xlabel("# of posts")
    plt.show()

def plot_log_posts_since(posts, date):
    last_month_posts = posts[posts['date']>date].groupby('classroom_id').count()
    num_posts_by_class = posts.groupby('classroom_id').sum()
    last_month_posts_total= num_posts_by_class.join(last_month_posts, how='left', lsuffix='_num_posts_by_class', rsuffix='_last_month_posts')
    last_month_posts_total.loc[last_month_posts_total['id_last_month_posts'].isnull(),'exists_last_month_posts'] =0
    fig, ax = plt.subplots(1,1)
    ax.set_title(f'class log(posts) since {date.date()}')
    ax.hist(np.log(last_month_posts_total['exists_last_month_posts']+1), bins=40)
    ax.set_ylabel("# of classes")
    ax.set_xlabel("log(#) of posts")
    plt.show()

def plot_posts_between(posts, date1, date2):
    print(sum((date1 < posts['date']) & (posts['date'] < date2)))
    last_month_posts = posts[(date1 < posts['date']) & (posts['date'] < date2)].groupby('classroom_id').count()
    num_posts_by_class = posts.groupby('classroom_id').sum()
    last_month_posts_total= num_posts_by_class.join(last_month_posts, how='left', lsuffix='_num_posts_by_class', rsuffix='_last_month_posts')
    last_month_posts_total.loc[last_month_posts_total['id_last_month_posts'].isnull(),'exists_last_month_posts'] =0
    fig, ax = plt.subplots(1,1)
    ax.set_title(f'class posts between {date1.date()} and {date2.date()}')
    ax.hist(last_month_posts_total['exists_last_month_posts'], bins=40)
    ax.set_ylabel("# of classes")
    ax.set_xlabel("# of posts")
    plt.show()

def plot_log_posts_between(posts, date1, date2):
    print(sum((date1 < posts['date']) & (posts['date'] < date2)))
    last_month_posts = posts[(date1 < posts['date']) & (posts['date'] < date2)].groupby('classroom_id').count()
    num_posts_by_class = posts.groupby('classroom_id').sum()
    last_month_posts_total= num_posts_by_class.join(last_month_posts, how='left', lsuffix='_num_posts_by_class', rsuffix='_last_month_posts')
    last_month_posts_total.loc[last_month_posts_total['id_last_month_posts'].isnull(),'exists_last_month_posts'] =0
    fig, ax = plt.subplots(1,1)
    ax.set_title(f'class log(posts) between {date1.date()} and {date2.date()}')
    ax.hist(np.log(last_month_posts_total['exists_last_month_posts']+1), bins=40)
    ax.set_ylabel("# of classes")
    ax.set_xlabel("log(#) of posts")
    plt.show()

def plot_all_posts_between(posts):
    plot_posts_since(posts, pd.to_datetime("Feb 15 2018"))
    plot_posts_since(posts, pd.to_datetime("Feb 15 2011"))
    plot_posts_since(posts, pd.to_datetime("Jan 15 2018"))
    plot_log_posts_since(posts, pd.to_datetime("jan 15 2018"))
    plot_log_posts_since(posts, pd.to_datetime("feb 15 2018"))
    plot_posts_between(posts, pd.to_datetime("Jan 15 2018"), pd.to_datetime("Feb 15 2018"))
    plot_log_posts_between(posts, pd.to_datetime("Dec 15 2017"), pd.to_datetime("Jan 15 2018"))
    plot_log_posts_between(posts, pd.to_datetime("Jan 15 2018"), pd.to_datetime("Feb 15 2018"))
    plot_log_posts_between(posts, pd.to_datetime("FEB 15 2018"), pd.to_datetime("March 15 2018"))

def main():
    posts = pd.read_csv('../data/posts.csv')
    posts['date'] = pd.to_datetime(posts.date, errors='coerce')
    plot_all_posts_between(posts)

    # testing a uniform distribution
    import random
    plt.hist(np.log([random.random()*500 for x in range(1015)]), bins=40);
    date1, date2 = pd.to_datetime("Dec 15 2010"), pd.to_datetime("Jan 15 2011")
    sum((date1 < posts['date']) & (posts['date'] < date2))

if __name__ == '__main__':
    main()
