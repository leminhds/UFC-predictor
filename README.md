# UFC-predictor
project goes from scraping the data to EDA to prediction


## What is included
The project is composed of 3 main parts:
- Data collection by scraping http://www.ufcstats.com/ with Scrapy
- Data preprocessing
- Predictive model with XGBoost

You can find the 2 scrapers for fightcards and fighters in their respective folders. More details about what information do we scrape are presented in the README file of these folders

The 2 csv raw file are what we obtain from the scrapers

The preprocessing notebook details all the steps that was used to arrive to the cleaned_dataset.csv

The EDA and predictor notebooks relies on the cleaned_dataset.csv that was produced by the preprocessing notebook

## Drawback and room for improvement
Admittedly, the predictor utilized the information that would only be available during the fight itself (such as the accuracy of punches, number of takedown attempts, etc.) therefore, in the context of predicting for an upcoming fight, the accuracy will be lower than the result previously mentioned.
One way to overcome this challenge would be to have a 3rd scraper that would focus on scraping the fight statistic of a fighter in the 3 previous fight prior to the match we want to predict.
