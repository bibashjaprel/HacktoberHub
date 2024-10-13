# Google Stock Price Prediction using LSTM

## Overview

This project implements a Long Short-Term Memory (LSTM) neural network to predict Google stock prices based on historical data. The model uses a sequence of previous stock prices to forecast future values.

## Requirements

- Python 3.x
- NumPy
- Pandas
- Matplotlib
- Keras
- TensorFlow

## Dataset

The project uses two CSV files:

- `Google_Stock_Price_Train.csv`: Training data containing historical Google stock prices.
- `Google_Stock_Price_Test.csv`: Test data for validating the model's predictions.

# Model Architecture

The LSTM model consists of:

- Input Layer: Takes in sequences of previous stock prices.
- LSTM Layers: Four LSTM layers with varying units and dropout layers to prevent overfitting.
- Output Layer: A Dense layer that predicts the stock price.