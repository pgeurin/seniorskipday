import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import six.moves
import itertools
from statsmodels.tsa.arima_model import ARIMA, ARIMAResults
from statsmodels.tsa.arima_process import ArmaProcess
import statsmodels.api as sm
from statsmodels.stats.diagnostic import acorr_ljungbox
from scipy import signal
from statsmodels.tsa.statespace.sarimax import SARIMAX
from autoregression import timeseries
from autoregression.timeseries import plot_series_and_first_differences_over_bound_time, fill_and_float_timeseries, make_arema_prediction

def main():
    posts_df = pd.read_csv('../data/posts.csv')
    posts_df['date'] = pd.to_datetime(posts_df['date'], errors='coerce')
    # plot_series_and_first_differences_over_bound_time(posts_df, event_col_name='classroom_id', time_col_name='date', other_col_name='id', num=10, start=pd.to_datetime("2012"), stop=pd.to_datetime("2018"))
    count_posts_per_day_df = posts_df.groupby(['classroom_id', 'date']).count()
    class_1_count_posts_per_day = count_posts_per_day_df.loc[1]
    timeseries = pd.Series(class_1_count_posts_per_day['id'].values,
                           class_1_count_posts_per_day.index)
    timeseries = fill_and_float_timeseries(timeseries, freq='D')
    # timeseries = timestamp_events_to_timeseries(event_timestamp_df, event_col_name='classroom_id', time_col_name='date', other_col_na
    make_arema_prediction(timeseries)


if __name__ == "__main__":
    main()
