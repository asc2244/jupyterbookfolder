# Project 2: Comparing SHSAT Participation Rates in 2018-19 and 2020-21

In this project, I compare SHSAT participation rates in NYC schools from 2018-19 and 2020-21.

## Introduction

As a native New Yorker (proudly born and raised in Queens), I was interested in creating a data visualization that focused on a unique aspect of growing up in the city: the SHSAT. The SHSAT (Specialized High School Admissions Test) is a high school entrance exam that's required to attend 8 out of 9 academically specialized high schools in NYC. The only one that doesn't require the test for admissions is LaGuardia High School (which I attended for piano!). Studying for the SHSAT was a big part of my (and many other NYC kids') childhood - therefore, I wanted to focus my project on this! Specifically, I was curious to understand whether or not SHSAT participation rates changed during the pandemic. Did schools see more or less people take the test after COVID? Or did the pandemic not affect participation rates at all?

I used two datasets to conduct my analysis: [2018-2019 SHSAT Admissions Test Offers By Sending School](https://data.cityofnewyork.us/Education/2018-2019-SHSAT-Admissions-Test-Offers-By-Sending-/uf53-ree9/about_data) and [2020-2021 SHSAT Admissions Test Offers By Sending School](https://data.cityofnewyork.us/Education/2020-2021-SHSAT-Admissions-Test-Offers-By-Sending-/k8ah-28f4/about_data). Both datasets record the number of people who take the SHSAT in each NYC school, using a DBN code as the school identifier. However, the only difference between them is that one captures data from the 2018-19 academic year and the other from the 2020-21 academic year. Since this data is longitudinal, meaning that the two datasets record data from the same schools over time, I realized that I could focus my data visualization project on understanding if SHSAT participation rates changed in each school on an individual level before and after COVID.

## Results
The plot shows that there is a strong, positive correlation the number of testers in 2018-19 and 2020-21. Specifically, schools that had high amounts of students taking the SHSAT in 2018-19 also had high numbers of students take the exam in 2020-21. Vice versa, schools that had low numbers of students taking the SHSAT in 2018-19 continued to have low numbers of students take the SHSAT in 2020-21.

Thus, the pandemic did not worsen the rates at which these students participated in the SHSAT, nor did it improve them. Basically, it did not have an effect on them at all!

It's interesting how there's a cluster of data points in the lower numbers. It surprised me that overall there are more schools with only 0-50 students taking the SHSAT per year than schools with 100+ students taking the exam. This make sense though since the SHSAT is an exam that skews towards wealthier, more privileged students who can afford test prep and tutors, and the majority of NYC schools do not have a very high-income population. 

### Data Visualization

[2018-19 vs 2020-21 SHSAT Participation Rates Scatterplot](project_2.png)