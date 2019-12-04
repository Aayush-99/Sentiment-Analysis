# SENTIMENT ANALYSIS
An application that extracts emotions of a given text - whether it is positive, negative or neutral and return a sentiment score.

## Table of Contents
* [General Info](#generalinfo)
* [Technology Used](#technology)
* [Obtaining Data](#webscraping)
* [Extracting Emotions](#SentimentAnalysis)

## General Info
Guest reviews are becoming a prominent factor affecting people’s bookings/purchases. Reviews can tell you if you are keeping up with your customers’ expectations, which is crucial for developing marketing strategies based on the personas of your customers.
For this project the data was gathered using a self designed web scraping tool based on Beautiful Soup. Hotel Giraffe, New York was considered for this project.
Following the collection of data a sentiment analysis program was designed which calculated the percentage of postive, negative or neutral reviews.

## Technology Used
* Python 3.7

## Obtaining Data
Libraries Used:
* bs4
* urllib
* requests

A web scraper was designed using the libraries urllib and BeautifulSoup. A csv file was created to store the data. The number of contributions of the reviewer, the title and review were extracted.

## Extracting Emotions
Libraries Used:
* pandas
* nltk

The data was read using pandas which is an open-source library providing data structures and analysis functions in Python. NLTK stands for Natural Language Toolkit, which is a commonly used NLP library with a lot of corpus, models and algorithm.
A polarity function was created to generate the polarity scores. There are four types of scores: negative, positive, neutral and compound.
