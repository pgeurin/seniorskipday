import pandas as pd

def load_sessions():
    sessions = pd.read_csv('../data_january/sessions.csv')
    sessions['start_date'] = pd.to_datetime(sessions['start_date'])
    sessions['stop_date'] = pd.to_datetime(sessions['stop_date'])
    sessions['exists']=1
    return sessions


def load_posts():
    posts = pd.read_csv('../data_january/posts.csv')
    posts['exists']=1
    posts = posts.rename(columns={'id':'post_id'})
    posts['date'] = pd.to_datetime(posts.date, errors='coerce')
    return posts


def load_teachers():
    teachers = pd.read_csv('../data_january/teachers.csv')
    return teachers


def load_students():
    students = pd.read_csv('../data_january/students.csv')
    return students


def load_schools():
    schools = pd.read_csv('../data_january/schools.csv')
    return schools


def load_planning_events():
    planning_events = pd.read_csv('../data_january/planning_events.csv')
    return planning_events


def load_child_posts():
    child_posts = pd.read_csv('../data_january/child_posts.csv')
    return child_posts


def load_lesson_posts():
    lesson_posts = pd.read_csv('../data_january/lesson_posts.csv')
    return lesson_posts


def load_parents():
    parents = pd.read_csv('../data_january/parents.csv')
    return parents


def load_classrooms():
    classrooms = pd.read_csv('../data_january/classrooms.csv')
    classrooms = classrooms.rename(columns={'id':'classroom_id'})
    return classrooms


def load_classrooms_merged():
    classrooms_merged = pd.read_csv('../data_january/classrooms_merged.csv')
    return classrooms_merged


def load_all():
    sessions = load_sessions()
    posts = load_posts()
    teachers = load_teachers()
    students = load_students()
    schools = load_schools()
    planning_events = load_planning_events()
    child_posts = load_child_posts()
    lesson_posts = load_lesson_posts()
    parents = load_parents()
    classrooms = load_classrooms()
    classrooms_merged = load_classrooms_merged()
    return (teachers, students, classrooms, sessions, schools, posts,
            planning_events, child_posts, lesson_posts, parents,
            classrooms_merged)


def load_now():
    now = pd.to_datetime('January 24, 2018')
    return now

def main():
    (teachers, students, classrooms, sessions, schools, posts, planning_events,
    child_posts, lesson_posts, parents, classrooms_merged) = load_all()


if __name__ == "__main__":
    main()
