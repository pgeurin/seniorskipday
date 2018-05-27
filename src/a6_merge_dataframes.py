import pandas as pd
import matplotlib.pyplot as plt
from data_load import (load_posts, load_classrooms, load_teachers,
                       load_students, load_lesson_posts, load_now)

def make_posts_per_lesson(lesson_posts):
    posts_per_lesson = lesson_posts.groupby('lesson_id').count()
    posts_per_lesson.rename(index=str, columns={"post_id": "posts_per_lesson"});
    return posts_per_lesson


def plot_hist_posts_per_lesson_hist(posts_per_lesson):
    plt.hist(np.log(posts_per_lesson.sample(100).values), bins=30);
    return None


def merge_classrooms_to_posts(classrooms_merged, posts_per_lesson):
    return classrooms_merged.merge(posts_per_lesson, how='left', left_on='lesson_set_id', right_index=True)
# classrooms_merged_posts = merge_classrooms_to_posts(classrooms_merged, posts_per_lesson)


def one_hot_teacher_admin(teachers):
    teachers['teach_and_admin'] = (teachers['teacher']=='t') & (teachers['admin']=='t' )
    teachers['is_teacher'] = teachers['teacher']=='t'
    teachers['is_admin'] = teachers['admin']=='t'
    return teachers


def make_teachers_per_class(teachers):
    teachers_one_hot = one_hot_teacher_admin(teachers)
    return teachers_one_hot.groupby('default_classroom_id').sum()
# teachers_per_class = teachers_per_class(teachers)


# THIS IS ALMOST DEFINITELY DATA LEAKAGE:
def merge_classrooms_to_posts_teachers(classrooms_merged_posts, teachers_per_class):
    return classrooms_merged_posts.merge(teachers_per_class,
                                         how='left',
                                         left_on='classroom_id',
                                         right_index=True)
# classrooms_merged_posts_teachers = merge_classrooms_to_posts_teachers(classrooms_merged_posts, teachers_per_class)


def compare_num_classrooms(classrooms_merged_posts_teacher,students):
    print(len(classrooms_merged.classroom_id.unique()))
    print(len(students.child_id.unique()))
    print(len(students.classroom_id.unique()))
    return None


def make_current_students_per_class(students):
    current_students_per_class = students[
        students['current'] == 't'].groupby('classroom_id').count()
    current_students_per_class = current_students_per_class.drop('current', axis=1)
    current_students_per_class.rename({'child_id': 'num_current_children'})
    return current_students_per_class


def make_old_students_per_class(students):
    old_students_per_class = students[students['current']=='f'].groupby('classroom_id').count()
    old_students_per_class = old_students_per_class.drop('current', axis=1)
    old_students_per_class.rename({'child_id': 'num_old_children'});
    return old_students_per_class


def merge_classrooms_to_posts_teachers_current_old_students(classrooms,
                                                            posts_per_lesson,
                                                            teachers_per_class,
                                                            current_students_per_class,
                                                            old_students_per_class):
    classrooms_merged = classrooms.merge(posts_per_lesson,
                                         how='left',
                                        left_on='lesson_set_id',
                                        right_index=True)
    classrooms_merged = merge_classrooms_to_posts_teachers(classrooms_merged,
                                                           teachers_per_class)
    classrooms_merged = classrooms_merged.merge(current_students_per_class,
                                                how='left',
                                                left_on='classroom_id',
                                                right_index=True)
    classrooms_merged = classrooms_merged.merge(old_students_per_class,
                                                how='left',
                                                left_on='classroom_id',
                                                right_index=True)
    return classrooms_merged


def make_classrooms_merged(classrooms, posts, teachers, students, lesson_posts):
    posts_per_lesson = make_posts_per_lesson(lesson_posts)
    teachers_per_class = make_teachers_per_class(teachers)
    current_students_per_class = make_current_students_per_class(students)
    old_students_per_class = make_old_students_per_class(students)
    classrooms_merged_all = merge_classrooms_to_posts_teachers_current_old_students(
        classrooms, posts_per_lesson, teachers_per_class,
        current_students_per_class, old_students_per_class)
    return classrooms_merged_all

def make_classrooms_merged_non_leaky(now, posts, child_posts, lesson_posts):
    posts_before = posts[posts['date'] < now]
    classrooms_merged = classrooms.merge(posts,
                                         how='outer',
                                         left_on='classroom_id',
                                         right_on='classroom_id')
    children_per_post = child_posts.groupby('post_id').count()
    children_per_post = children_per_post.reset_index()
    children_per_post[
        'children_per_post_aka_post_blast'] = children_per_post['child_id']
    children_per_post = children_per_post.drop('child_id', axis=1)
    classrooms_merged = classrooms_merged.merge(children_per_post,
                                                how='left',
                                                left_on='post_id',
                                                right_on='post_id')
    posts_per_child = child_posts.groupby('child_id').count()
    posts_per_lesson = lesson_posts.groupby('lesson_id').count()
    posts_per_lesson = posts_per_lesson.reset_index()
    posts_per_lesson['post_per_lesson_aka_popularity'] = posts_per_lesson['post_id']
    posts_per_lesson = posts_per_lesson.drop('post_id', axis=1)
    classrooms_merged = classrooms_merged.merge(posts_per_lesson,
                                                how='left',
                                                left_on='lesson_set_id',
                                                right_on='lesson_id')
    posts_per_lesson = lesson_posts.groupby('lesson_id').count()
    plt.hist(np.log(posts_per_lesson.sample(100).values), bins=30)
    posts_per_lesson.rename(index=str, columns={"post_id": "posts_per_lesson"})
    classrooms_merged = classrooms_merged.merge(posts_per_lesson,
                                                how='left',
                                                left_on='lesson_set_id',
                                                right_index=True)
    return classrooms_merged

def main():
    # posts_per_lesson = make_posts_per_lesson(lesson_posts)
    # current_students_per_class = make_current_students_per_class(students)
    # old_students_per_class = make_old_students_per_class(students)
    # classrooms_merged = merge_classrooms_to_posts_teachers_current_old_students(classrooms, teachers_per_class, current_students_per_class, old_students_per_class)
    posts = load_posts()
    classrooms = load_classrooms()
    teachers = load_teachers()
    students = load_students()
    lesson_posts = load_lesson_posts()
    now = load_now()
    classrooms_merged_all_leaky = make_classrooms_merged(classrooms, posts, teachers, students, lesson_posts)
    make_classrooms_merged_non_leaky = make_classrooms_merged_non_leaky(now, posts, child_posts)

if __name__ == "__main__":
    main()
