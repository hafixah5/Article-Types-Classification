# Classification of Text Articles

## Table of Contents

* [Project Description](#project-description)
* [Project Files](#project-files)
* [Project Usage](#project-usage)
* [Credit](#credit)

##  :scroll:  Project Description

This project aims to create a Natural Language Processing (NLP) model, to classify more than 2000 articles into 5 categories.
The categories are Sport, Tech, Business, Entertainment and Politics. 
In this project, the model is able to classify the articles with a 90% accuracy.

A sneak peek of the model developed and model report are as below:

![Model Architecture.png](https://github.com/hafixah5/Article-Types-Classification/blob/main/Images/Model%20Architecture.png)

![Confusion Matrix.png](https://github.com/hafixah5/Article-Types-Classification/blob/main/Images/Confusion%20Matrix.png)

##  :card_index_dividers:  Project Files
:point_right: classification_of_articles.py (model development file)

:point_right: Folder saved_models
- model.h5
- ohe.pkl
- tokenizer.json

:point_right: photos folder which contains the following images:
- confusion matrix
- epoch accuracy and epoch loss (from tensorboard)
- model accuracy
- model architecture
- model architecture
- model parameter

##  :rocket:  Project Usage
1) This project is done using Python 3.8 on Google Colab.
This project used the following modules:

![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)

2) The dataset can be loaded from [here](https://raw.githubusercontent.com/susanli2016/PyCon-Canada-2019-NLP-Tutorial/master/bbc-text.csv)

3) You may download all the necessary files (dataset & python files) to run the project on your device.

## :technologist:  Credit

This dataset is taken from: [Link](https://raw.githubusercontent.com/susanli2016/PyCon-Canada-2019-NLP-Tutorial/master/bbc-text.csv)
