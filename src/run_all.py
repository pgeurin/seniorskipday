import pandas as pd
from sessions_analysis_and_plot import sessions_to_plots
from posts_analysis_and_plot import posts_to_plots
from merge_dataframe_leaky import make_classrooms_merged
from data_load import load_all

def main():
    (teachers, students, classrooms, sessions, schools, posts, planning_events,
     child_posts, lesson_posts, parents, classrooms_merged) = load_all()
    sessions_to_plots(sessions)
    posts_to_plots(posts)
    classrooms_merged_all_leaky = make_classrooms_merged(classrooms, posts,
                                                         teachers, students,
                                                         lesson_posts)


if __name__ == "__main__":
    main()
