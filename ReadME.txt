Twitter Sentiment Analysis — Emotion-Aware AI


 Project Overview

This project is a Twitter Sentiment Analysis system that analyzes tweets to determine their sentiment and can be extended to detect emotions behind user opinions.

The project is designed as a beginner-friendly AI/ML internship project, focusing on Natural Language Processing (NLP) and Machine Learning using Python.



 Objective

To classify tweets into sentiment categories such as:

Positive

Negative

Neutral

To prepare a foundation for emotion detection (Happy 😄, Angry 😡, Sad 😢)

To analyze public opinion using Twitter data


Technologies Used

Python

Pandas

Scikit-learn

NLTK

VS Code



📂 Dataset

Source: Kaggle (Twitter Sentiment Dataset)

Files Used:

twitter_training.csv

twitter_validation.csv

Columns:

Tweet ID

Entity

Sentiment

Tweet Text

 Project Structure


Sentiment Analyzer/
│
├── twitter_training.csv
├── twitter_validation.csv
├── sentiment_analysis.py
└── README.md

 Methodology


Load Twitter training and validation datasets

Rename and select required columns

Clean and preprocess tweet text

Prepare data for sentiment classification

(Future) Train machine learning models

(Future) Add emotion detection and hashtag-wise analysis




Output

Displays sample rows from training and validation datasets

Confirms successful dataset loading and preprocessing



Future Enhancements

Add machine learning model for sentiment prediction

Implement emotion detection (Happy , Angry , Sad )

Perform hashtag-wise sentiment analysis

Build a Streamlit web dashboard

Add real-time Twitter sentiment analysis