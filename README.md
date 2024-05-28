### Introduction to the Project

#### Objective
The primary objective of this project is to replicate the methods and results of the research paper by Navid Mottaghi and Sara Farhangdoost. This study focuses on forecasting stock prices amidst the heightened volatility caused by the COVID-19 pandemic using various machine learning models.

#### Background
The COVID-19 pandemic has introduced unprecedented volatility in stock markets globally. Accurate stock price forecasting during such turbulent periods is critical for investors and policymakers. Traditional models like Autoregression and newer machine learning techniques such as Long-Short Term Memory (LSTM) networks, XGBoost, and simple benchmarks like the Last Value model were evaluated for their predictive capabilities.

#### Scope of Work
This project will involve the following steps to replicate the study:

1. **Data Collection**: Acquire daily stock price data for Facebook, Amazon, Tesla, Google, and Apple from January 2015 to April 2021, ensuring to include high, low, open, close, and volume metrics, with a focus on closing prices.

2. **Data Preparation**: Split the data into training (pre-January 2020) and testing sets (January 2020 to April 2021), capturing the period of the COVID-19 pandemic.

3. **Model Implementation**:
    - **Autoregression Model**: Implement an Autoregression model to leverage the correlation between consecutive daily prices.
    - **LSTM**: Develop and train a Long-Short Term Memory neural network to handle the sequential nature of stock price data.
    - **XGBoost**: Apply the eXtreme Gradient Boosting model to enhance prediction accuracy through ensemble learning.
    - **Last Value Model**: Use the Last Value model as a benchmark, based on the Efficient Market Hypothesis.

4. **Evaluation**: Assess model performance using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) metrics to determine prediction accuracy during the volatile pandemic period.

5. **Analysis and Comparison**: Compare the predictive accuracy of all models to identify which performs best under high market volatility conditions.

#### Expected Outcomes
By replicating the methods outlined in the paper, this project aims to verify the original findings that traditional models like Autoregression and Last Value outperform more complex machine learning models during periods of high volatility, such as the COVID-19 pandemic. The results will provide insights into the robustness and reliability of different forecasting techniques under extraordinary market conditions.

#### Significance
The replication and validation of this research are crucial for investors and market analysts to develop more reliable forecasting tools, especially in times of significant economic disruptions. By understanding the strengths and limitations of various models, stakeholders can make more informed decisions to mitigate risks and capitalize on market opportunities.
