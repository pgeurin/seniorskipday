import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from data_load import load_posts

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


def main():
    posts = load_posts()
    posts_to_plots(posts)
    # make_sparkline(sum_post, classroom_id=77)
    # make_sparkline(sum_post, classroom_id=852)
    # sum_post, sum_post_date_indexed = make_sum_post(posts)
    # plot_all_posts(posts)


if __name__ == "__main__":
    main()
