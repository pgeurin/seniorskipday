import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

teachers = pd.read_csv('../data/teachers.csv')
students = pd.read_csv('../data/students.csv')
sessions = pd.read_csv('../data/sessions.csv')
schools = pd.read_csv('../data/schools.csv')
posts = pd.read_csv('../data/posts.csv')
planning_events = pd.read_csv('../data/planning_events.csv')
child_posts = pd.read_csv('../data/child_posts.csv')
classrooms = pd.read_csv('../data/classrooms.csv')
lesson_posts = pd.read_csv('../data/lesson_posts.csv')
parents = pd.read_csv('../data/parents.csv')
sessions['start_date'] = pd.to_datetime(sessions['start_date'])
sessions['stop_date'] = pd.to_datetime(sessions['stop_date'])
sessions['exists']=1
posts['exists']=1
posts['date'] = pd.to_datetime(posts.date, errors='coerce')

posts = pd.read_csv('../data/posts.csv')
posts['exists']=1
posts['date'] = pd.to_datetime(posts.date, errors='coerce')

print(len(posts))
posts.head()

classrooms_merged = classrooms.merge(posts,how='outer', left_on='id', right_on='classroom_id')
classrooms_merged['classroom_id']=classrooms_merged['id_x']
classrooms_merged = classrooms_merged.drop('id_x', axis=1)
classrooms_merged['post_id']=classrooms_merged['id_y']
classrooms_merged = classrooms_merged.drop('id_y', axis=1)
print(len(classrooms_merged))
classrooms_merged.head(3)

children_per_post = child_posts.groupby('post_id').count()
children_per_post.describe()
children_per_post = children_per_post.reset_index()
children_per_post['children_per_post_aka_post_blast'] = children_per_post['child_id']
children_per_post = children_per_post.drop('child_id', axis=1)
children_per_post.head(3)

classrooms_merged = classrooms_merged.merge(children_per_post, how='left', left_on='post_id', right_on='post_id')
print(len(classrooms_merged))
classrooms_merged.head(3)

# not adding
posts_per_child = child_posts.groupby('child_id').count()
posts_per_child.describe()
posts_per_child.head(3)

posts_per_lesson = lesson_posts.groupby('lesson_id').count()
posts_per_lesson
print(len(posts_per_lesson))
posts_per_lesson = posts_per_lesson.reset_index()
posts_per_lesson['post_per_lesson_aka_popularity'] = posts_per_lesson['post_id']
posts_per_lesson = posts_per_lesson.drop('post_id', axis=1)
posts_per_lesson.head(3)


classrooms_merged = classrooms_merged.merge(posts_per_lesson, how='left', left_on='lesson_set_id', right_on='lesson_id')
print(len(classrooms_merged))
classrooms_merged.head(3)

classrooms.head(3)

len(classrooms_merged.classroom_id.unique())

len(teachers.default_classroom_id.unique())
len(teachers)

len(teachers.school_id.unique())

len(lesson_posts.lesson_id.unique())
len(lesson_posts.post_id.unique())
posts_per_lesson = lesson_posts.groupby('lesson_id').count()
print(len(posts_per_lesson))
plt.hist(np.log(posts_per_lesson.sample(100).values), bins=30);
posts_per_lesson.head(3)
posts_per_lesson.rename(index=str, columns={"post_id": "posts_per_lesson"});

classrooms_merged = classrooms_merged.merge(posts_per_lesson, left_on='lesson_set_id', right_index=True)
classrooms_merged.head(3)

# next time try merging first, then filter by time, then groupby and count
# We're going to have to merge by time soon.

classrooms_merged = classrooms_merged.merge(teachers, left_on='classroom_id', right_on='default_classroom_id')

teachers['teach_and_admin'] = (teachers['teacher']=='t') & (teachers['admin']=='t' )
teachers['is_teacher'] = teachers['teacher']=='t'
teachers['is_admin'] = teachers['admin']=='t'

teachers_per_class = teachers.groupby('default_classroom_id').sum()
teachers_per_class.head(3)

# THIS IS ALMOST DEFINITELY DATA LEAKAGE:
classrooms_merged = classrooms_merged.merge(teachers, left_on='classroom_id', right_index=True)

students.head()

len(students.child_id.unique())

len(students.classroom_id.unique())

current_students_per_class = students[students['current']=='t'].groupby('classroom_id').count()
current_students_per_class.drop('current', axis=1)
current_students_per_class.rename({'child_id': 'num_current_children'});

old_students_per_class = students[students['current']=='f'].groupby('classroom_id').count()
old_students_per_class.drop('current', axis=1)
old_students_per_class.rename({'child_id': 'num_old_children'});

classrooms_merged = classrooms_merged.merge(current_students_per_class, left_on='classroom_id', right_index=True)
classrooms_merged = classrooms_merged.merge(old_students_per_class, left_on='classroom_id', right_index=True)

classrooms_merged.head(3)

classrooms_merged.to_csv('../data/classrooms_merged2.csv')

### NOT MERGED:

# posts_merge = posts_merge.merge(planning_events, how='left', left_on)
# posts_merge.head(3)
#
# planning_events.child_id.value_counts().head(5)
#
# planning_events.head(5)
