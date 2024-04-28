---

# Network Traffic Anomaly Detection using One-Class SVM

## Overview

This repository contains Python code for performing anomaly detection on network traffic data using the One-Class Support Vector Machines (One-Class SVM) algorithm. Anomaly detection is a critical task in network security for identifying suspicious or malicious activities within network traffic.

## Requirements

- Python 3.x
- pandas
- scikit-learn

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/e-tabidze/ML-presentation
   ```

## Usage

1. Place your network traffic data in a CSV file named `network_traffic_data.csv` in the same directory as the Python script.
2. Run the script using Python:
   ```
   python presentation.py
   ```

## Description

The Python script performs the following steps:

1. Loads the network traffic data from the CSV file.
2. Encodes categorical variables using label encoding.
3. Splits the data into features (X) and labels (y).
4. Splits the dataset into training and testing sets.
5. Trains a One-Class SVM model on the training set using only benign samples.
6. Predicts anomalies on the test set.
7. Evaluates the model's performance using a classification report.

## Output

The script generates a classification report showing precision, recall, and F1-score for both benign and malicious samples.

## Dataset Format

The network traffic data should be in CSV format with the following columns:

- packet_size: Size of the packet in bytes.
- protocol: Communication protocol used (e.g., TCP, UDP, ICMP).
- source_ip: Source IP address.
- destination_ip: Destination IP address.
- source_port: Source port number.
- destination_port: Destination port number.
- timestamp: Timestamp of the network traffic event.
- label: Label indicating whether the traffic is benign or malicious.

Example dataset:
```
packet_size,protocol,source_ip,destination_ip,source_port,destination_port,timestamp,label
3600,UDP,192.168.1.61,198.51.100.4,9012,123,2024-04-28 14:10:00,Malicious
2200,TCP,192.168.1.62,8.8.8.8,6789,443,2024-04-28 14:15:00,Benign
1700,UDP,10.0.0.13,203.0.113.5,8901,123,2024-04-28 14:20:00,Benign
3700,TCP,192.168.1.63,185.199.110.153,9012,80,2024-04-28 14:25:00,Malicious
1700,ICMP,192.168.1.64,8.8.4.4,7890,53,2024-04-28 14:30:00,Benign
```
