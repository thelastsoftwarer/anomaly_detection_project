# Efficient Data Stream Anomaly Detection

This project is part of the application process for the Graduate Software Engineer role at Cobblestone Energy. The task was to develop a Python script capable of detecting anomalies in a continuous data stream. The script focuses on identifying unusual patterns such as exceptionally high values or deviations from the norm.

## Project Description

This project simulates a continuous data stream and detects anomalies using the **Z-score** algorithm. The data stream consists of trend, seasonal (sinusoidal), and random noise components to emulate real-world scenarios such as financial transactions or system metrics. The script identifies anomalies based on the Z-score, which measures how far a data point deviates from the mean.

### Key Features:
- **Data Stream Simulation**: Generates a stream of data that includes a growing trend, seasonal changes (sinus wave), and random noise.
- **Anomaly Detection**: Uses a sliding window to compute the moving average and standard deviation, then applies the Z-score to detect outliers.
- **Real-time Visualization**: The script visualizes both the data stream and the detected anomalies in real-time using `matplotlib`.

## Algorithm Explanation

The Z-score algorithm is used for anomaly detection. The Z-score of a data point indicates how many standard deviations it is from the mean of the data within a specified window. If the absolute value of the Z-score exceeds a predefined threshold, the data point is flagged as an anomaly.

- **Z-score Formula**: 
  \[
  Z = \frac{{(x - \mu)}}{\sigma}
  \]
  Where:
  - \( x \) is the current data point,
  - \( \mu \) is the moving average of the data points in the sliding window,
  - \( \sigma \) is the standard deviation of the data points in the sliding window.

### Parameters:
- **Window Size**: The number of recent data points considered for moving average and standard deviation (e.g., 20 data points).
- **Z-score Threshold**: A threshold of 2 is used for detecting anomalies, meaning any data point more than 2 standard deviations away from the mean is flagged as an anomaly.
- **Noise Scale**: Random noise is added to the data stream to simulate real-world fluctuations.

## Requirements

To run this project, you'll need Python 3.x installed along with the following libraries:

```bash
pip install numpy matplotlib
