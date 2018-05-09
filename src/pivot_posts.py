import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

posts['year_month'] = pd.to_datetime(posts['date']).map(lambda dt: dt.replace(day=1))
posts.groupby(['classroom_id','year_month']).count().head(3)

class_month_posts = posts.pivot_table(index='classroom_id',
                     columns='year_month',
                     values='exists',
                     fill_value=0,
                     aggfunc='count').unstack()
class_month_posts.head(3)

# pretty good so far, but I want those zeros
class_month_posts = posts.pivot_table(index='year_month',
                     columns='classroom_id',
                     values='exists',
                     fill_value=0,
                     aggfunc='count').unstack()
class_month_posts.head(3)

for classroom_id in class_month_posts['classroom_id'].unique()[0:10]:
    fig, ax = plt.subplots(2,1, figsize=(20,3))
    ax.flatten()
    ax[0].scatter(class_month_posts[class_month_posts['classroom_id']==classroom_id]['date'].values,class_month_posts[class_month_posts['classroom_id']==classroom_id]['exists'], s=1)
    ax[1].plot(class_month_posts[class_month_posts['classroom_id']==classroom_id].sort_values('date')['date'],class_month_posts[class_month_posts['classroom_id']==classroom_id].sort_values('date')['exists']);
    ax[0].set_title(f"Class {classroom_id} score")

for classroom_id in list(class_month_posts.index.get_level_values(0).unique())[0:10]:
    fig, ax = plt.subplots(2,1, figsize=(20,3))
    ax.flatten()
    dates = np.array(class_month_posts[classroom_id].index)
    current_monthly_posts = class_month_posts[classroom_id].values
    ax[0].scatter(dates, current_monthly_posts>0, s=1)
    ax[1].plot(dates, current_monthly_posts>0)
#     ax[1].plot(class_month_posts[class_month_posts['classroom_id']==classroom_id].sort_values('date')['date'],class_month_posts[class_month_posts['classroom_id']==classroom_id].sort_values('date'));
    ax[0].set_title(f"Class {classroom_id} score")
    ax[0].set_xlim("2011","2018")
    ax[1].set_xlim("2011","2018")
    plt.show()
