import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from autoregression. cleandata import clean_df_respect_to_y

# from autoregression import cleandata

def import_hearts():
    hearts = pd.read_csv('../data_june/health_checks.csv')
    hearts['date'] = pd.to_datetime(hearts['date'], errors='coerce')
    return hearts


def make_sum_post(posts):
    sum_post = posts[['date', 'classroom_id', 'exists']
                     ].groupby(['classroom_id', 'date']).sum()
    sum_post['exists'] = np.log(sum_post['exists'])
    sum_post = sum_post.reset_index()
    sum_post_date_indexed = sum_post.copy()
    sum_post_date_indexed.set_index('date', inplace=True)
    return sum_post

def make_hearts_merged(hearts, classrooms_merged):
    hearts_merged = classrooms_merged.merge(hearts, how='left', left_on=['school_id','date'], right_on=['school_id','date'])
    hearts_merged['classroom_id'] = hearts_merged['classroom_id_x']
    hearts_merged = hearts_merged.drop('classroom_id_y', axis=1)
    hearts_merged = hearts_merged.drop('classroom_id_x', axis=1)
    hearts_merged_cleaned_date = clean_df_respect_to_y(hearts_merged, 'date')
# sum(pd.isna(hearts_merged['date']))
# sum(pd.isna(hearts_merged_cleaned_date['date']))
    return hearts_merged, hearts_merged_cleaned_date

def plot_hearts(hearts_merged, sum_post):
    for classroom_id in sum_post['classroom_id'].unique()[20:30]:
        fig, ax = plt.subplots(2,1, figsize=(20,3))
        ax.flatten()
        x = hearts_merged[
            hearts_merged['classroom_id'] == classroom_id]['date'].values
        y = hearts_merged[
            hearts_merged['classroom_id'] == classroom_id]['score']
        ax[0].scatter(x, y, s=1)
        x_sorted = hearts_merged[hearts_merged['classroom_id'] == classroom_id].sort_values('date')['date']
        y_sorted = hearts_merged[hearts_merged['classroom_id']==classroom_id].sort_values('date')['score']
        ax[1].plot(x_sorted, y_sorted);
        ax[0].set_title(f"Class {classroom_id} score")

    #     ax[0].get_xaxis().set_label_coords(2011,2019)
    #     ax[1].get_xaxis().set_label_coords(2011,2019)
    #     x0, x1 = ax[0].xaxis.label.get_position()
    #     print(x0, x1)
    # #     ax[1].xaxis.label.set_position([x0, x1])
    # #     ax[1].xaxis._autolabelpos=False
    #     ax[0].set_xticks([pd.to_datetime(x0),pd.to_datetime(x1)])
    #     ax[1].set_xticks([pd.to_datetime(x0),pd.to_datetime(x1)])
        plt.show()


def merge_hearts(classrooms_merged_school, hearts):
    hearts_merged = classrooms_merged.merge(hearts, how='inner', left_on=['classroom_id','date'], right_on=['classroom_id','date'])
#     hearts_merged['classroom_id'] = hearts_merged['classroom_id_x']
#     hearts_merged = hearts_merged.drop('classroom_id_y', axis=1)
#     hearts_merged = hearts_merged.drop('classroom_id_x', axis=1)
    return hearts_merged
hearts_merged = merge_hearts(classrooms_merged, hearts)
hearts_merged.head()


def show_heart_merge_deets(hearts_merged, classrooms_merged):
    print(len(hearts_merged))
    print(len(hearts))
    print(len(classrooms_merged))
    print(hearts_merged.columns)
    return None
show_heart_merge_deets(hearts_merged, classrooms_merged)


def main():
    posts = pd.read_csv('../data_january/posts.csv')
    posts['exists'] = 1
    sum_post = make_sum_post(posts)
    classrooms_merged = pd.read_csv('../data_january/classrooms_merged.csv')
    classrooms_merged = classrooms_merged.rename({'school_id_x': 'school_id'},
                                                 axis='columns')
    hearts = import_hearts()
    hearts_merged, hearts_merged_cleaned_date = make_hearts_merged(
        hearts,
        classrooms_merged)
    plot_hearts(hearts_merged_cleaned_date, sum_post)


if __name__ == "__main__":
    main()
