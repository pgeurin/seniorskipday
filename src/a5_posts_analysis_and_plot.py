import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from a1_data_load import load_posts

def plot_all_posts(posts):
    posts[['date', 'classroom_id', 'exists']].groupby(['classroom_id',
                                                       'date']).sum().plot()
    return None


def make_sum_post(posts):
    sum_post = posts[['date', 'classroom_id',
                      'exists']].groupby(['classroom_id', 'date']).sum()
    sum_post['exists'] = np.log(sum_post['exists'])
    sum_post = sum_post.reset_index()
    sum_post_date_indexed = sum_post.copy()
    sum_post_date_indexed.set_index('date', inplace=True)
    return sum_post, sum_post_date_indexed


def make_sparkline(sum_post, classroom_id=77):
    fig, ax = plt.subplots(2, 1, figsize=(20, 3))
    ax[0].scatter(
        sum_post[sum_post['classroom_id'] == classroom_id]['date'].values,
        sum_post[sum_post['classroom_id'] == classroom_id]['exists'])
    ax[1].plot(
        sum_post[sum_post['classroom_id'] == classroom_id]['date'],
        sum_post[sum_post['classroom_id'] == classroom_id]['exists'])
    ax[0].set_title(f"Class {classroom_id} log(posts)")
    # plt.savefig(f'../img/sparklines/sparkline_{classroom_id}.png')
    # plt.savefig(f'../img/sparklines/sparkline_{classroom_id}_thumb.png',
    #             dpi=30)
    # plt.close(fig)
    plt.show()
    return None


def make_all_sparklines(sum_post):
    for classroom_id in sum_post['classroom_id'].unique()[0:3]:
        make_sparkline(sum_post, classroom_id=classroom_id)
        # plt.show()
    return None


def save_all_sparklines(sum_post):
    for classroom_id in sum_post['classroom_id'].unique()[0:30]:
        make_sparkline(sum_post, classroom_id=classroom_id)
        plt.show()
    return None


def posts_to_plots(posts):
    plot_all_posts(posts)
    make_sum_post(posts)
    sum_post, sum_post_date_indexed = make_sum_post(posts)
    make_sparkline(sum_post, classroom_id=77)
    make_sparkline(sum_post, classroom_id=852)
    make_all_sparklines(sum_post)
    return sum_post


def make_binary_graph(posts):
    posts['year_month'] = pd.to_datetime(posts['date']).map(lambda dt: dt.replace(day=1))
    posts.groupby(['classroom_id','year_month']).count().head(3)

    # pretty good so far, but I want those zeros
    class_month_posts = posts.pivot_table(index='year_month',
                         columns='classroom_id',
                         values='exists',
                         fill_value=0,
                         aggfunc='count').unstack()
    class_month_posts.head(3)

    for classroom_id in list(
            class_month_posts.index.get_level_values(0).unique())[0:10]:
        fig, ax = plt.subplots(2, 1, figsize=(20, 3))
        ax.flatten()
        dates = np.array(class_month_posts[classroom_id].index)
        current_monthly_posts = class_month_posts[classroom_id].values
        ax[0].scatter(dates, current_monthly_posts > 0, s=1)
        ax[1].plot(dates, current_monthly_posts > 0)
        ax[1].plot(class_month_posts[
            class_month_posts['classroom_id'] == classroom_id
            ].sort_values('date')['date'], class_month_posts[class_month_posts[
                'classroom_id'] == classroom_id].sort_values('date'))
        ax[0].set_title(f"Class {classroom_id} score")
        ax[0].set_xlim("2011", "2018")
        ax[1].set_xlim("2011", "2018")
        plt.show()


def main():
    posts = load_posts()
    posts_to_plots(posts)
    make_binary_graph(posts)
    # make_sparkline(sum_post, classroom_id=77)
    # make_sparkline(sum_post, classroom_id=852)
    # sum_post, sum_post_date_indexed = make_sum_post(posts)
    # plot_all_posts(posts)


if __name__ == "__main__":
    main()
