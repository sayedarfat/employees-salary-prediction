# employees-salary-prediction
"Predicting employee salaries using machine learning techniques for TechWorks Consulting. This project includes data preprocessing, model building, and feature importance analysis. Key features include Random Forest model and exploratory data analysis (EDA)."

# Employee Salary Prediction Using Machine Learning

## Project Overview
This project aims to predict the salary of newly hired employees using machine learning techniques. It was developed for TechWorks Consulting, a leading IT staffing company, to ensure fair and competitive compensation for their employees.

## Problem Statement
TechWorks Consulting faced the challenge of determining appropriate salaries for new hires based on various factors such as their previous experience, qualifications, and market trends. The goal was to create a machine learning model that could accurately predict the salary of new employees.

## Data Description
The dataset used for this project includes the following features:
- **College**: The tier of the college attended by the employee.
- **City**: Whether the city is a metro (1) or non-metro (0).
- **Previous CTC**: The employee's previous cost to company (CTC).
- **Previous Job Change**: The number of job changes the employee has had.
- **Graduation Marks**: The employee's graduation marks percentage.
- **Experience**: Total work experience in months.
- **Role**: The role of the employee (Manager/Executive).

## Methodology
1. **Data Preprocessing**: Converting categorical data into numerical form, handling missing values, and creating dummy variables.
2. **Exploratory Data Analysis (EDA)**: Understanding data distribution, identifying patterns and outliers using visualizations.
3. **Model Building**: Training various regression models including Linear Regression, Decision Tree, Random Forest, and Gradient Boosting.
4. **Model Evaluation**: Evaluating models using Mean Squared Error (MSE) and R² score. The Random Forest model was chosen as the best performer with an R² score of 0.593.
5. **Feature Importance Analysis**: Analyzing which features were most significant in predicting salary.

## Results
The Random Forest model provided the best predictions with a mean squared error of [MSE Value] and an R² score of 0.593. The most important features influencing salary predictions were 'Previous CTC' and 'Total Work Experience'.

## Future Work
Future improvements could include:
- Adding more features such as industry trends and economic factors.
- Applying advanced techniques like hyperparameter tuning and cross-validation.
- Exploring more complex models for better accuracy.

## Installation Instructions
To run this project locally, follow these steps:
1. Clone the repository:
2. Install the required dependencies:
3. Run the Jupyter Notebook:


## Contact Information
For any queries or suggestions, feel free to reach out:
- **Email**: [sayedarfat01@gmail.com]



