import pandas as pd
from sessions_analysis_and_plot import sessions_to_plots
from posts_analysis_and_plot import posts_to_plots
from merge_dataframes import (make_classrooms_merged,
                              make_classrooms_merged_non_leaky)
from data_load import load_all, load_now


def main():
    (teachers, students, classrooms, sessions, schools, posts, planning_events,
     child_posts, lesson_posts, parents, classrooms_merged) = load_all()
    # sessions_to_plots(sessions)
    # posts_to_plots(posts)
<<<<<<< HEAD
    # classrooms_merged_all_leaky = make_classrooms_merged(classrooms, posts,
=======
    classrooms_merged_all_leaky = make_classrooms_merged(classrooms, posts,
>>>>>>> 9d8a99265da6530b8b9ccf8a5d6d8f60135f971f
                                                         teachers, students,
                                                         lesson_posts)
    now = load_now()
    print(now)
    classrooms_merged_non_leaky = make_classrooms_merged_non_leaky(now,
                                                                   posts,
                                                                   child_posts,
                                                                   lesson_posts
                                                                   )


if __name__ == "__main__":
    main()
