import pandas as pd
from a1_data_load import load_all, load_now
from a2_sessions_analysis_and_plot import sessions_to_plots
import a3_plot_days_where_posts
import a4_plot_post_last_x_days
from a5_posts_analysis_and_plot import posts_to_plots
from a6_merge_dataframes import (make_classrooms_merged,
                                 make_classrooms_merged_non_leaky)
from a7_post_aggr import plot_posts_between
import a8_plot_client_hearts
import a9_model
import a10_load_model_make_predictions


def main():
    (teachers, students, classrooms, sessions, schools, posts, planning_events,
     child_posts, lesson_posts, parents, classrooms_merged) = load_all()
    sessions_to_plots(sessions)
    a3_plot_days_where_posts.main()
    a4_plot_post_last_x_days.main()

    posts_to_plots(posts)
    classrooms_merged_all_leaky = make_classrooms_merged(classrooms, posts,
                                                         teachers, students,
                                                         lesson_posts)
    now = load_now()
    print(now)
    classrooms_merged_non_leaky = make_classrooms_merged_non_leaky(now,
                                                                   posts,
                                                                   child_posts,
                                                                   lesson_posts,
                                                                   classrooms)
    plot_posts_between(posts)
    a8_plot_client_hearts.main()
    a9_model.main()
    a10_load_model_make_predictions.main()

if __name__ == "__main__":
    main()
