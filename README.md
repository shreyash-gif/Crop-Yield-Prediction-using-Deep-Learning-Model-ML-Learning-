# Crop Yield Prediction using Machine Learning

## Overview
This repository contains code and resources for predicting crop yields using machine learning models. The project focuses on leveraging historical crop yield data and advanced modeling techniques to forecast agricultural productivity accurately. 

## Problem Statement
Accurate crop yield prediction is vital for India's agricultural sector, which contributes significantly to the GDP and employs a large portion of the workforce. However, challenges such as smallholder farming and climate change make accurate forecasting difficult. This project aims to address these challenges by developing robust, accurate, and scalable models using machine learning.

## Objectives
- Accurate Yield Forecasting
- Improved Model Performance
- Handling Multimodal Data
- Temporal Dynamics Modelling
- Scalability and Robustness
- Contributing to Agriculture Sustainability
- Transfer Learning and Pretrained Models
- Interpretability and Explainability

## Applications
Crop yield prediction has numerous practical applications including:
- Optimizing Farm Management Practices
- Risk Management and Insurance
- Supply Chain Management
- Market Analysis and Trading
- Government Policy and Planning
- Research and Development
- Climate Change Adaptation

## Dataset
The dataset used in this project can be found [here](https://aps.dac.gov.in/APY/Public_Report1.aspx). It comprises historical crop yield data in numerical format.

## Methodology
1. **Data Collection**: Data sourced from a Hackathon organized by IISC Bangalore.
2. **Data Preprocessing**: Cleaning and preparing the dataset.
3. **Data Loading and Feature Selection**: Selecting relevant features and transforming categorical variables.
4. **Model Selection and Training**: Choosing and training various machine learning models.
5. **Evaluation Metrics**: Assessing model performance using metrics like MAE, MSE, and RMSE.
6. **Model Comparison**: Comparing performance of different models.
7. **Deployment**: Deploying the project using Flask library for local deployment.

## Results
### Performance Evaluation
- **R-squared Score**: Measures the proportion of variance in the crop yield data explained by the models.
- **Mean Squared Error (MSE)**: Quantifies the average deviation between predicted and actual crop yields.

## Conclusion
The project demonstrates the efficacy of various machine learning models in accurately predicting crop yields. It highlights the strengths and weaknesses of each model and emphasizes the practical implementation of these models for agricultural decision-making.

## Future Work
- Addressing limited ground truth data.
- Improving interpretability and explainability of models.
- Integrating prior knowledge into models.
- Generalizing models across different regions and crops.

## References
1. Semret, N., 2021. [Predicting crop yields with little ground truth: A simple statistical model for in-season forecasting](https://arxiv.org/abs/2106.08720).
2. Wolanin, A. et al., 2020. [Estimating and understanding crop yields with explainable deep learning in the Indian Wheat Belt](https://iopscience.iop.org/article/10.1088/1748-9326/ab6c4b/meta).
3. Sharma, S. et al., 2020. [Wheat crop yield prediction using deep LSTM model](https://arxiv.org/abs/2011.01498).
4. Qiao, M. et al., 2023. [KSTAGE: A knowledge-guided spatial-temporal attention graph learning network for crop yield prediction](https://www.sciencedirect.com/science/article/pii/S0020025522003782).
5. Nejad, S.M.M. et al., 2022. [Multispectral crop yield prediction using 3D-convolutional neural networks and attention convolutional LSTM approaches](https://ieeexplore.ieee.org/document/9596487).

## Research Gap
The research gap identified in this project includes:
1. Limited ground truth data.
2. Interpretability and explainability of models.
3. Integration of prior knowledge into models.
4. Generalization of models across different regions and crops.

## How to Use
1. Clone this repository: `git clone <repository-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Flask app: `python app.py`
4. Access the app in your browser: `http://localhost:5000`

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
