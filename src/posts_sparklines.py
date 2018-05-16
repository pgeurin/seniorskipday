posts.head(3)

posts.describe()

sorted_post_date = posts.date.sort_values()

# # posts.date.dtypes
# # posts.date.apply(lambda x: not isinstance(x, pd.Timestamp))
# sorted_post_date.iloc[-170:]
# # posts.date.dtypes
# posts['date'] = pd.to_datetime(posts.date, errors='coerce')
# # len(posts.date)
# # posts.date>'2018-12-12'

print(posts.date.max())
print(posts.date.min())

# posts['exists']=1
# posts.head(3)

posts[['date','classroom_id','exists']].groupby(['classroom_id', 'date']).sum().plot();

posts[['date','classroom_id','exists']].groupby(['classroom_id', 'date']).sum()

sum_post = posts[['date','classroom_id','exists']].groupby(['classroom_id', 'date']).sum()
sum_post['exists'] = np.log(sum_post['exists'])
sum_post = sum_post.reset_index()
sum_post_date_indexed = sum_post.copy()
sum_post_date_indexed.set_index('date',inplace=True)
# plt.plot(sum_post[sum_post['classroom_id']==1])
# plt.scatter(sum_post[sum_post['classroom_id']==1][date], sum_post[sum_post['classroom_id']==1]['exists'])

sum_post[sum_post['classroom_id']==3]

sum_post['classroom_id'].value_counts()[60:61]
sum_post.head()

# plt.plot(sum_post[sum_post['classroom_id']==1]);
np.exp(5)

fig, ax = plt.subplots(2,1, figsize=(20,3))
ax[0].scatter(sum_post[sum_post['classroom_id']==77]['date'].values,sum_post[sum_post['classroom_id']==77]['exists'])
ax[1].plot(sum_post[sum_post['classroom_id']==77]['date'],sum_post[sum_post['classroom_id']==77]['exists']);
ax[0].set_title("Class 77 log(posts)")

fig, ax = plt.subplots(2,1, figsize=(20,3))
ax[0].scatter(sum_post[sum_post['classroom_id']==852]['date'].values,sum_post[sum_post['classroom_id']==852]['exists'])
ax[1].plot(sum_post[sum_post['classroom_id']==852]['date'],sum_post[sum_post['classroom_id']==852]['exists']);
ax[0].set_title("Class 852 log(posts)")

for classroom_id in sum_post['classroom_id'].unique()[0:30]:
    fig, ax = plt.subplots(2,1, figsize=(20,3))
    ax[0].scatter(sum_post[sum_post['classroom_id']==classroom_id]['date'].values,sum_post[sum_post['classroom_id']==classroom_id]['exists'], s=6)
    ax[1].plot(sum_post[sum_post['classroom_id']==classroom_id]['date'],sum_post[sum_post['classroom_id']==classroom_id]['exists']);
    ax[0].set_title(f"Class {classroom_id} log(posts)")
    plt.show()
