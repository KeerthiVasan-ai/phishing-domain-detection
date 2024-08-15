
# Phishing Domain Detection

## Overview
Phishing is a type of fraud where attackers impersonate a reputable company or individual to obtain sensitive information, such as login credentials or account information, through email or other communication channels. The main objective of this project is to build a machine learning solution that can predict whether a domain is real or malicious.

## Project Structure
The project is organized as follows:

```
Phishing Domain Detection
│
├── build
├── src/backend
│   ├── utils
│   ├── data_processing
│   └── feature
├── app.py
│
├── frontend
│   ├── public
│   ├── src
│   │   ├── components
│   │   ├── App.js
│   │   ├── index.js
│   │   └── styles.css
│   ├── package.json
│   └── README.md
│
├── notebook
│   └── phishing_domain_detection.ipynb
│
├── dataset
│   └── phishing_domains.csv
│
└── models
    ├── classifier-v1
    ├── RF-Classifier-v1
    └── RF-Classifier-v2
```

### 1. Backend
- **utils**: Contains utility functions used across the backend, such as data loading and preprocessing utilities.
- **data_processing**: Responsible for cleaning, transforming, and preparing the dataset for model building.
- **feature_extraction**: Implements feature engineering, including URL-based, domain-based, page-based, and content-based features.

### 2. Frontend
- **basic React.js project**: A simple frontend using React.js to interact with the model and display predictions.
- **src/components**: Contains the components used in the React.js application.
- **App.js**: The main React component.
- **index.js**: Entry point of the React application.
- **styles.css**: Contains styling for the React application.

### 3. Notebook
- This directory contains Jupyter notebooks that document the process of data exploration, feature engineering, and model building.

### 4. Dataset
- Contains the dataset used for training and testing the model. The dataset includes features that help distinguish between real and phishing domains.

### 5. Models
- Stores the trained machine learning models and related files.

## Approach

### 1. Data Cleaning
- Clean the dataset by handling missing data, removing duplicates, and normalizing data where necessary.

### 2. Feature Engineering
- Extract relevant features to enhance the model's predictive capabilities:
  - **URL-Based Features**: Analyzes characteristics like URL length, presence of special characters, etc.
  - **Domain-Based Features**: Looks at domain-related information such as domain age, registration details, etc.
  - **Page-Based Features**: Extracts features based on the content of the webpage.
  - **Content-Based Features**: Analyzes the actual content served by the domain (e.g., presence of suspicious keywords).

### 3. Model Building
- Experiment with different classical machine learning algorithms such as Logistic Regression, Decision Trees, Random Forests, and others, along with a Deep Learning Model, to find the best-performing model.

### 4. Model Testing
- Evaluate the performance of the models using metrics like accuracy, precision, recall, and F1-score. Fine-tune the best model for optimal results.

## Models Tested
- **Logistic Regression**
- **Support Vector Classifier**
- **Random Forest Classifier**
- **Decision Tree Classifier**
- **Deep Learning Model**

Out of all these models, the **Random Forest Classifier** provided the best accuracy.

## Results
The final solution is capable of accurately predicting whether a domain is real or fake based on the extracted features and trained models.

## Technologies Used
- **Python**: For backend development, data processing, and machine learning.
- **React.js**: For frontend development.
- **Jupyter Notebooks**: For exploratory data analysis and model experimentation.
- **Scikit-learn**: For building and evaluating machine learning models.

## How to Run the Project
1. **Clone the repository**:
   ```bash
      git clone https://github.com/KeerthiVasan-ai/phishing-domain-detection
   ```

2. **Backend Setup**:
   - Navigate to the `backend` directory.
   - Install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```
   - Run the backend server.

Once the server is started, follow the link in the running server to view the project or view the deployement here : ```https://antiphish-ai.onrender.com/```


## Contribution
Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
