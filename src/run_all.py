import pandas as pd
from sessions_analysis_and_plot import sessions_to_plots
from posts_analysis_and_plot import posts_to_plots


def import_all():
    teachers = pd.read_csv('../data_january/teachers.csv')
    students = pd.read_csv('../data_january/students.csv')
    schools = pd.read_csv('../data_january/schools.csv')
    posts = pd.read_csv('../data_january/posts.csv')
    posts['exists']=1
    posts=posts.rename(columns={'id':'post_id'})
    posts['date'] = pd.to_datetime(posts.date, errors='coerce')
    planning_events = pd.read_csv('../data_january/planning_events.csv')
    child_posts = pd.read_csv('../data_january/child_posts.csv')
    lesson_posts = pd.read_csv('../data_january/lesson_posts.csv')
    parents = pd.read_csv('../data_january/parents.csv')
    sessions = pd.read_csv('../data_january/sessions.csv')
    sessions['start_date'] = pd.to_datetime(sessions['start_date'])
    sessions['stop_date'] = pd.to_datetime(sessions['stop_date'])
    sessions['exists']=1
    classrooms = pd.read_csv('../data_january/classrooms.csv')
    classrooms=classrooms.rename(columns={'id':'classroom_id'})
    # posts['date'] = pd.to_datetime(posts.date, errors='coerce')
    classrooms_merged = pd.read_csv('../data_january/classrooms_merged.csv')
    return teachers, students, classrooms, sessions, schools, posts, planning_events, child_posts, lesson_posts, parents, classrooms_merged
(teachers, students, classrooms, sessions, schools, posts, planning_events,
 child_posts, lesson_posts, parents, classrooms_merged) = import_all()


def main():
    (teachers, students, classrooms, sessions, schools, posts, planning_events,
     child_posts, lesson_posts, parents, classrooms_merged) = import_all()
    sessions_to_plots(sessions)
    posts_to_plots(posts)

if __name__ == "__main__":
    main()
