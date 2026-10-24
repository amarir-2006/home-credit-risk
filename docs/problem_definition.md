# Problem Definition

## Business objective

Estimate the risk of payment difficulties for a loan applicant
using information available at the time of the application.

## Dataset target

The Home Credit competition uses the `TARGET` column in
`application_train.csv`.

We will verify its definition and the feature availability rules
against the dataset documentation before modeling.

## Intended use

Educational research and demonstration of ML engineering practices.

## Validation principles

- Keep training and evaluation data separate.
- Audit features for target leakage.
- Document the split strategy and evaluation metrics.
- Do not interpret competition predictions as a validated
  12-month probability of default.