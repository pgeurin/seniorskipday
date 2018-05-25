# [Senior Skip Day](http://seniorskip.com)

## TOC

1. [About](#about)
2. [Procedure](#procedure)
3. [Tech Stack](#tech-stack)
4. [Web Application](#web-application)
5. [Data Source](#Data-Source)
6. [Features](#Features)
7. [How Evaluate?](#How-Evaluate?)
8. [Contact](Questions?-Reach-out!)
## About
***NLP and knowledge graphs for AEC using spaCy***

Seniorskip.com is a early warning notification system built for the client Transparent Classroom. A dashboard to prioritize the time of customer service representatives.

Seniorskip.com is churn with a twist. Transparent Classroom makes student tracking software for teachers, and they have a problem. Sometimes teachers take vacation, and sometimes they decide to drop the software. The only catch is, they don’t change their account. The school does. So the account doesn’t churn, but it’s still at risk.

Data-wise these two conditions look similar. In the vacation case the teachers will come back and it would be very annoying for them to get an email or text asking why they left the service. In the drop case you want to intervene as soon as possible. Tricky.

Solution: make an early warning notification system and dashboard.

http://seniorskip.com/ - (Data hidden for client, sorry)

<img src="img/tc_screencast9.gif" width="400"/>

## Procedure
1. EDA to assess proper prediction methodology
2. Feature extraction from Transparent Classroom data.
3. Train/Test split and model.
4. Create dashboard on Flask web application at (seniorskip.com)[http://seniorskip.com/]

## Tools

![slide_technology](img/slide_technology.png)
 - autoregression
 - Scikit Learn
 - Pandas
 - Jupyter Notebook
 - NumPy
 - EC2
 - Flask
 - Bootstrap
 - Javascript


## Web Application
![Screenshot](img/skipday_screenshot.png)

The application returns:
  * table sortable by any column (including probability of making zero posts in three months)
  * extracts components and provisions related to the components


## Data Source

<img src="img/slide2_meet_transparent_classroom.png" width="600"/>

Transparent classroom’s database. Actual Data not available to the public, sorry. It's a series of tables, detailing posts, teachers, classrooms, lessons, and their relationship.

<img src="img/slide_3_data_layout.png" width="400"/>

## Features

I extracted these features from the table relationships:
<img src="img/slide3_data.png" width="400"/>


## How evaluate?

There are only 30 users who’ve left the company. So churn isn’t the correct measurement in this case. Schools discontinue their accounts at the one year mark. Teachers don’t have a direct say. The product owner theorized that non-use is related to discontinuing accounts.

Upon EDA, the data looks continuously distributed. But looking at the log(posts) number, we can see that there is two distinct classes. This allows for binary classification for a first pass.

<img src="img/days_with_one_post_since_feb_15_2018.png"  width="300"/>
<img src="img/log_days_with_one_post_since_feb_15_2018.png"  width="300"/>
<img src="img/days_with_one_post_since_feb_15_2011.png"  width="300"/>
<img src="img/log_days_with_one_post_since_feb_15_2011.png"  width="300"/>
<img src="img/hist_post_since_jan_15_2018.png"  width="300"/>
<img src="img/hist_log_post_since_jan_15_2018.png"  width="300"/>
<img src="img/hist_post_since_feb_15_2011.png"  width="300"/>
<img src="img/hist_log_post_since_feb_15_2011.png" width="300"/>


## Questions? Reach out!

![slide5_philipgeurin.png](img/slide5_philipgeurin.png)
