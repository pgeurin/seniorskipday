# Senior Skip Day
## Notification for User churn in Transparent Classroom

Churn with a twist: Transparent Classroom makes student tracking software for teachers, and they have a problem. Sometimes teachers take vacation, and sometimes they decide to drop the software. The only catch is, they don’t change their account. The school does. So the account doesn’t churn, but it’s still at risk.

Data-wise these two conditions look similar. In the vacation case the teachers will come back and it would be very annoying for them to get an email or text asking why they left the service. In the drop case you want to intervene as soon as possible. Tricky.

Solution: make an early warning notification system and dashboard.

http://seniorskip.com/ - (Data hidden for client, sorry)

![ScreenCast](img/tc_screencast9.gif)
<img src="img/tc_screencast9.gif" width="600"/>

### Data Source:

<!-- ![slide2_meet_transparent_classroom.png](img/slide2_meet_transparent_classroom.png) -->
<img src="img/slide2_meet_transparent_classroom.png" width="600"/>

Transparent classroom’s database. Actual Data not available to the public, sorry

<!-- ![slide_3_data_layout](img/slide_3_data_layout.png) -->
<img src="img/slide_3_data_layout.png" width="600"/>
<!-- ![Example Teacher 2 Posts](img/class_852_posts.png) -->
<img src="img/class_852_posts.png" width="600"/>

![Example Teacher 3 Log(Posts)](img/class_47_log_posts.png)

Features:
![slide3_data.png](img/slide3_data.png)
<img src="img/slide3_data.png" width="600"/>


### Analytics base table conversion:

They’ve put it into a csv, with each action taken, school, classroom, teacher, ect. Client isn’t willing to give full access.


### Model:

This one is trickier. I honestly plan on comparing methods using a program I’ve already written.
I haven’t learned time series methods yet. I’m hoping to learn something quite imminently. If not I want to see current use effects use three months from now.

### How evaluate?

There are only 30 users who’ve left the company. So churn isn’t the correct measurement in this case. Schools discontinue their accounts (one year long). But teachers don’t have a direct say. Teacher decreased use is theorized to be related to decrease of use. Instead we’ll be using the their pre-set metric “health score” which is a amalgamation of five metrics (given in code)
We’ll see how many stopped meeting this score.

<!-- ![Histograms Post Since Certain Days](img/days_with_one_post_since_feb_15_2018.png) -->
<img src="img/days_with_one_post_since_feb_15_2018.png"  width="400"/>
<!-- ![Histograms Post Since Certain Days](img/log_days_with_one_post_since_feb_15_2018.png) -->
<img src="img/log_days_with_one_post_since_feb_15_2018.png"  width="400"/>
<!-- ![Histograms Post Since Certain Days](img/days_with_one_post_since_feb_15_2011.png) -->
<img src="img/days_with_one_post_since_feb_15_2011.png"  width="400"/>
<!-- ![Histograms Post Since Certain Days](img/log_days_with_one_post_since_feb_15_2011.png) -->
<img src="img/log_days_with_one_post_since_feb_15_2011.png"  width="400"/>
<!-- ![Histograms Post Since Certain Days](img/hist_post_since_jan_15_2018.png) -->
<img src="img/hist_post_since_jan_15_2018.png"  width="400"/>
<!-- ![Histograms Post Since Certain Days](img/hist_log_post_since_jan_15_2018.png) -->
<img src="img/hist_log_post_since_jan_15_2018.png"  width="400"/>
<!-- ![Histograms Post Since Certain Days](img/hist_post_since_feb_15_2011.png) -->
<img src="img/hist_post_since_feb_15_2011.png"  width="400"/>
<!-- ![Histograms Post Since Certain Days](img/hist_log_post_since_feb_15_2011.png) -->
<img src="img/hist_log_post_since_feb_15_2011.png" width="600"/>

### What is the MVP?

A python model that gives a prediction if the users will stop using the service soon (and how permanently?)

### Causal Inference:
Yes, this is a risk as we don’t have time to make a test just yet. The client is OK with this.

An assistive goal would be to compare the use dropoff with the 30 churns results to decide which method is best

## Reach out to me:

![slide5_philipgeurin.png](img/slide5_philipgeurin.png)
