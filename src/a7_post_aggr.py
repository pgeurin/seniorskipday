import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def posts_between(posts, date1, date2):
    # print('total posts in this timeframe = ' + str(sum((date1 < posts['date']) & (posts['date'] < date2))))
    last_month_posts = posts[(date1 < posts['date']) & (posts['date'] < date2)].groupby('classroom_id').count()
    num_posts_by_class = posts.groupby('classroom_id').sum()
    last_month_posts_total= num_posts_by_class.join(last_month_posts, how='left', lsuffix='_num_posts_by_class', rsuffix='_last_month_posts')
    last_month_posts_total.loc[last_month_posts_total['post_id_last_month_posts'].isnull(),'exists_last_month_posts'] = 0
    return last_month_posts_total

def log_posts_between(posts, date1, date2):
    print(sum((date1 < posts['date']) & (posts['date'] < date2)))
    last_month_posts = posts[(date1 < posts['date']) & (posts['date'] < date2)].groupby('classroom_id').count()
    num_posts_by_class = posts.groupby('classroom_id').sum()
    last_month_posts_total= num_posts_by_class.join(last_month_posts, how='left', lsuffix='_num_posts_by_class', rsuffix='_last_month_posts')
    last_month_posts_total.loc[last_month_posts_total['id_last_month_posts'].isnull(),'exists_last_month_posts'] = 0
    last_month_posts_total['exists_last_month_posts'] = np.log(last_month_posts_total['exists_last_month_posts']+1)
    return last_month_posts_total

def days_with_not_zero_posts_between(posts, date1, date2):
    print(sum((date1 < posts['date']) & (posts['date'] < date2)))
    days_one_post_in_last_month = posts[(date1 < posts['date']) & (posts['date'] < date2)].groupby(['classroom_id','date']).sum().groupby('classroom_id').count()
    num_posts_by_class = posts.groupby('classroom_id').count()
    days_one_post_in_last_month = num_posts_by_class.join(days_one_post_in_last_month, how='left', lsuffix='_num_posts_by_class', rsuffix='_days_one_post_in_last_month')
    days_one_post_in_last_month.loc[days_one_post_in_last_month['exists_days_one_post_in_last_month'].isnull(), 'exists_days_one_post_in_last_month'] = 0
    return days_one_post_in_last_month

def log_days_with_not_zero_posts_between(posts, date1, date2):
    print(sum((date1 < posts['date']) & (posts['date'] < date2)))
    days_one_post_in_last_month = posts[(date1 < posts['date']) & (posts['date'] < date2)].groupby(['classroom_id','date']).sum().groupby('classroom_id').count()
    num_posts_by_class = posts.groupby('classroom_id').count()
    days_one_post_in_last_month = num_posts_by_class.join(days_one_post_in_last_month, how='left', lsuffix='_num_posts_by_class', rsuffix='_days_one_post_in_last_month')
    days_one_post_in_last_month.loc[days_one_post_in_last_month['exists_days_one_post_in_last_month'].isnull(), 'exists_days_one_post_in_last_month'] = 0
    days_one_post_in_last_month['exists_days_one_post_in_last_month'] = np.log(days_one_post_in_last_month['exists_days_one_post_in_last_month']+1)
    return days_one_post_in_last_month

def main():
    posts = pd.read_csv('../data_january/posts.csv')
    posts['exists']=1
    posts.groupby(pd.Grouper(freq="M"), as_index=False).count()
    posts.groupby([(posts['date'].year), (posts['date'].month)]).sum()

    months = "jan, feb, mar, april, may, june, july, aug, sept, oct, nov, dec".split(',')
    for classroom_id in posts['classroom_id'].unique():
        for year in range(2011,2018):
            for i_month in range(months):
                posts_between(posts, date1=pd.datetime(str(year) + months[i_month]), date2=)
                plot_days_with_not_zero_posts_between(posts, date1, date2)

if __name__ == '__main__':
    main()
