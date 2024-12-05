# Project 3: The Rat Project 🐀

In this project, I analyze the relationship between rat sightings and gentrification in NYC.

## Introduction

Hello everyone! Welcome to the rat project. This was a labor of love, fueled by desire to prove that I could code and do something silly.

As an NYC native, I spent my life surrounded by rats. And since I was born and raised in Queens, I obviously think it's the best borough ever. Therefore, I wanted to use my project to 1) prove that Queens is #1 and 2) learn something new about the worst animals ever.

I randomly stumbled across the [Rodent Inspection Dataset](https://data.cityofnewyork.us/Health/Rodent-Inspection/p937-wjvj/about_data) on NYC Open Data, which basically aggregates all reported rat sightings by borough in NYC.

It was perfect. Love at first sight. I knew I wanted to do my project on this.

Then I started thinking about what goes best with rats. After much deliberation, it hit me: rent. It was a perfect combination. Rats and rent. It even had the alliteration thing going for it.

I asked myself: what sort of analysis could I put together with rats and rent? After finding the [Median Asking Rent Dataset](https://streeteasy.com/blog/data-dashboard/[object%20Object]?agg=Total&metric=Inventory&type=Sales&bedrooms=Any%20Bedrooms&property=Any%20Property%20Type&minDate=2010-01-01&maxDate=2024-10-01&area=Flatiron,Brooklyn%20Heights) on Streeteasy, which aggregates the median rental-asking prices by borough on their website, I realized that I could use this data to not only figure out which borough had the most rats (using the rodent inspection data), but also find out which boroughs were the most gentrified (using the Streeteasy data).

[The Good Cause Eviction Law](https://rentguidelinesboard.cityofnewyork.us/resources/faqs/rent-increases/#:~:text=The%20Good%20Cause%20Eviction%20law%20establishes%20a%20%E2%80%9Clocal%20rent%20standard,a%20maximum%20of%2010%25%20total) establishes a “local rent standard,” which states that a reasonable rent increase in a given year is set at the rate of inflation plus 5%, with a maximum of 10% total. Therefore, I decided that I was going to use the data from Streeteasy to calculate the yearly percent change in rent from 2010-2024. If rent increased by more than 10% in a year, then I would classify it as an unfair rent increase and label it as gentrified (I understand this is an oversimplification of the definition of gentrification, but rent data was the simplest to work with for purposes of this project). I would then count how many times each borough was labelled as gentrified to determine which borough is deemed the most gentrified in NYC.

The plan was simple (although it was much harder in practice than I thought). First, I would use the Rodent Inspection data to compile the number of rats reported in each borough. Then, I would use the Streeteasy Rent data calculate the percent changes in rent and the proportion of gentrification per borough. Lastly, I would merge the two datasets together using "Borough" as the common column to show the proportion of rats and gentrification per borough. Then, I would turn this into a data visualization!

All of this would be to answer the following question: do rats like gentrification? My hypothesis was yes, they do! I think that rats will hang out in gentrified areas more than less-gentrified areas since gentrified areas typically have more tourism, construction, and late night eateries (all of which means more trash).

Ultimately, this ended up being much more complicated than I thought, mainly due to the fact that I challenged myself to do some of the steps using the Python Standard Library instead of Pandas. I say that I challenged myself, but I really just forgot that the Pandas functions existed until it was too late. Oh well. Hopefully this helps me prepare for the final.

The rat spiel is over. Please sit back and enjoy the data.

## Results
All in all, the purpose of this project was to answer the following question: do rats like gentrification? My hypothesis was that they do! Rats would probably like gentrified areas more than non gentrified areas because there's more trash in gentrified areas (due to increased tourism, foot traffic, etc.).

It seems like I was ~ mostly ~ right about that. Manhattan has the most gentrification and the most rats. Brooklyn had the second most gentrification and also a good amount of rats. Conversely, Queens had less rats and also less gentrification (same with Staten Island). Bronx was a weird outlier though. It had a lot of rats and a little gentrification. This might be due to data collection issues (i.e. how I only used rental data instead of sales data, not enough data on Bronx from the Streeteasy dataset, etc.).

Overall, I feel like I was able to show a fair correlation between rats and gentrification. The more gentrified an area, the more rats you'll see. So if your rent increases by more than 10%, you better buy some rat traps or invest in a cat!

The Rat Project almost destroyed me, but I learned a lot and feel good about how it turned out!

Thank you for reading :)

Stay ratty <3 🐀 - Alexa

### Data Visualization
[Rat Bar Graph](project_3.1.png)
[Gentrification Bar Graph](project_3.2.png)
[Rat x Gentrification Bar Graph](project_3.png)