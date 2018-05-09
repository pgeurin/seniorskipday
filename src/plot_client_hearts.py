import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

hearts = pd.read_csv('../data2/health_checks.csv')
hearts['date'] = pd.to_datetime(hearts['date'], errors='coerce')
hearts.head(3)

classrooms_merged.head(10)

hearts_merged = classrooms_merged.merge(hearts, how='left', left_on=['school_id','date'], right_on=['school_id','date'])

len(hearts_merged)

len(hearts)

len(classrooms_merged)

hearts_merged.columns

hearts_merged['classroom_id'] = hearts_merged['classroom_id_x']
hearts_merged = hearts_merged.drop('classroom_id_y', axis=1)
hearts_merged = hearts_merged.drop('classroom_id_x', axis=1)
hearts_merged.head(3)


sum(pd.isna(hearts_merged['date']))

# sum(pd.isna(hearts_merged_cleaned_date['date']))

from autoregression import cleandata
hearts_merged_cleaned_date = cleandata.clean_df_respect_to_y(hearts_merged, 'date')

def plot_hearts(hearts_merged):
    for classroom_id in sum_post['classroom_id'].unique()[20:30]:
        fig, ax = plt.subplots(2,1, figsize=(20,3))
        ax.flatten()
        ax[0].scatter(hearts_merged[hearts_merged['classroom_id']==classroom_id]['date'].values,hearts_merged[hearts_merged['classroom_id']==classroom_id]['score'], s=1)
        ax[1].plot(hearts_merged[hearts_merged['classroom_id']==classroom_id].sort_values('date')['date'],hearts_merged[hearts_merged['classroom_id']==classroom_id].sort_values('date')['score']);
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
plot_hearts(hearts_merged_cleaned_date)
