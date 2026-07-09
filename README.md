# Tata Car Resale Price Prediction Using Machine Learning

## Project Overview

This project is a regression machine learning project that predicts the resale price of Tata cars based on vehicle features such as model, variant, fuel type, transmission, body type, engine capacity, power, mileage, year, kilometres driven, ownership count, accident history, and ex-showroom price.

The goal of this project is to practise the full Data Science and Machine Learning lifecycle from data collection to model deployment.

The project follows these stages:

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Model Building
5. Model Evaluation
6. Model Deployment

---

## Business Problem

Car buyers, sellers, and dealerships often need a reliable way to estimate the resale value of used cars.

Manual car price estimation can be inconsistent because resale price depends on several factors, including:

- Car model
- Car variant
- Fuel type
- Transmission
- Body type
- Engine capacity
- Mileage
- Manufacturing year
- Kilometres driven
- Ownership count
- Accident history
- Original ex-showroom price

The goal of this project is to build a machine learning model that can estimate Tata car resale prices more consistently using historical car data.

---

## Dataset

The dataset was collected from Kaggle.

Each row in the dataset represents one Tata car record.

The target variable is:

`resale_price_lakh`

This means the model is trained to predict the resale price of each car in lakhs.

---

## Problem Type

This is a regression machine learning problem because the target variable is a continuous numerical value.

The model predicts a price, not a category.

Example:

```text
Predicted resale price = 4.90 lakh