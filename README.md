# Home Credit Default Risk

A production-oriented machine learning project for credit default
risk prediction using the Home Credit Default Risk dataset.

## Project objectives

- Build a reproducible data validation and feature engineering pipeline.
- Establish a baseline classification model.
- Compare candidate models using leakage-safe validation.
- Evaluate discrimination, probability calibration, and stability.
- Package the model behind a validated prediction API.
- Add automated testing, experiment tracking, and monitoring.

## Dataset

Source: [Home Credit Default Risk — Kaggle](https://www.kaggle.com/competitions/home-credit-default-risk)

The initial implementation will use `application_train.csv`.
Additional relational tables will be added in later phases.

The dataset is not included in this repository. Follow the dataset
provider's terms and instructions before downloading or using it.

## Architecture

The planned pipeline is:

Data ingestion -> Data validation -> Feature engineering ->
Model training -> Evaluation -> Model artifact -> Prediction API ->
Monitoring


## Disclaimer

This is an educational machine learning project, not a validated
credit decision system. Model outputs must not be used to make
real lending decisions.