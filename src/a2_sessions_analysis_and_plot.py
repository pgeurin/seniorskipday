import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def make_session_plot(sessions):
    fig, ax = plt.subplots(1,1, figsize=(20,40))
    point_pairs = [((sessions.start_date[i], sessions.stop_date[i]), (sessions.school_id[i], sessions.school_id[i])) for i in range(len(sessions))]
    # point_pairs = [((sessions.start_date[i],sessions.stop_date[i]),(sessions.school_id[i],sessions.school_id[i])) for i in range(100)]
    for x in point_pairs:
        ax.plot(x[0], x[1], alpha=.5)
    ax.set_xlabel('start/stop date')
    ax.set_ylabel('school_id')
    ax.set_title('school_id start/stop dates')
    return None

def make_sum_sessions(sessions):
    sessions.groupby('start_date').sum().head(5)
    sum_sessions_date_indexed = sessions.groupby('start_date').sum()
    sum_sessions_date_indexed['exists'] = np.log(sum_sessions_date_indexed['exists'])
    sum_sessions_date_indexed[sum_sessions_date_indexed['school_id'] == 465]['exists']
    sum_sessions = sum_sessions_date_indexed.reset_index()
    return sum_sessions

def plot_one_session(sessions, sum_sessions, school_id=24):
    fig, ax = plt.subplots(1, 1, figsize=(20,3))
    ax.plot(sum_sessions[sum_sessions['school_id']==school_id]['start_date'], sum_sessions[sum_sessions['school_id']==school_id]['exists'])
    plt.show()
    print('max stop = ' + str(sessions.stop_date.max()))
    print('max start = ' + str(sessions.start_date.max()))
    print('min stop = ' + str(sessions.stop_date.min()))
    print('min start = ' + str(sessions.start_date.min()))
    return None


def plot_session_starts(sessions):
    fig, ax = plt.subplots(1, 1, figsize=(20,20))
    ax.plot(sessions[['exists', 'start_date']].groupby('start_date').sum());
    plt.show()
    return None


def sessions_to_plots(sessions):
    make_session_plot(sessions)
    sum_sessions = make_sum_sessions(sessions)
    plot_one_session(sessions, sum_sessions, school_id=24)
    plot_session_starts(sessions)
    return sum_sessions


def find_cont_account(sessions):
    continued_accounts = (sessions.groupby('school_id').agg(
        {'stop_date' : [np.max]}) > pd.to_datetime("march 2018")).sum()
    return continued_accounts


def find_all_account(sessions):
    total_accounts = len(sessions.groupby('school_id').agg(
        {'stop_date' : [np.max]}) > pd.to_datetime("march 2018"))
    return total_accounts


def find_ended_sessions(sessions):
    ended_accounts = sessions.groupby('school_id').agg(
        {'stop_date' : [np.max]}) > pd.to_datetime("march 2018")
    return ended_accounts

def main():
    sessions = pd.read_csv('../data_january/sessions.csv')
    sessions['start_date'] = pd.to_datetime(sessions['start_date'])
    sessions['stop_date'] = pd.to_datetime(sessions['stop_date'])
    sessions['exists'] = 1
    sessions_to_plots(sessions)
    find_ended_sessions(sessions)
    # make_session_plot(sessions)
    # sum_sessions = make_sum_sessions(sessions)
    # plot_one_session(sum_sessions, school_id=24)
    # plot_session_starts(sessions)


if __name__ == "__main__":
    main()
