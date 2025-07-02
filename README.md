# 🍷 Wine Quality Prediction - End-to-End Machine Learning Project

This project is an end-to-end implementation of a machine learning pipeline that predicts wine quality based on physicochemical properties. It follows a modular, production-ready architecture and includes all major stages — from data ingestion to deployment via a Flask web application.

---

## 🚀 Project Features

- **Automated ML Pipeline** with:
  - 🔹 Data Ingestion
  - 🔹 Data Validation
  - 🔹 Data Transformation
  - 🔹 Model Training
  - 🔹 Model Evaluation
  - 🔹 Web Deployment (Flask)

- **Config-driven** and highly **scalable**
- Includes **experiment tracking** with MLflow
- Designed using **OOP best practices**
- Supports **hyperparameter tuning** and **schema validation**

---

## 🧰 Tech Stack

| Category          | Tools Used                                  |
|-------------------|---------------------------------------------|
| Programming       | Python                                       |
| ML Framework      | Scikit-learn                                 |
| Web Framework     | Flask                                        |
| Experiment Tracking | MLflow                                     |
| Config & Parsing  | PyYAML                                       |
| Logging           | Python Logging module                        |
| Data Handling     | Pandas, NumPy                                |
| Deployment        | Flask (REST API + Web UI)                    |
| Packaging         | setup.py                                     |

---

## 🗂️ Project Structure

```
.
├── app.py                        # Flask Web App
├── main.py                       # Pipeline Orchestration Script
├── requirements.txt              # Python Dependencies
├── setup.py                      # For packaging the project
├── params.yaml                   # Model & pipeline hyperparameters
├── schema.yaml                   # Input data schema
├── .gitignore
├── README.md                     # Project Documentation
└── src/
    └── datascience/
        ├── components/           # Data ingestion, transformation, etc.
        ├── config/               # Configuration manager
        ├── entity/               # Config entities (dataclasses)
        ├── pipeline/             # Pipeline orchestrators
        └── logger.py             # Custom logger
```

---

## 📈 Workflow Stages

1. **Data Ingestion:** Loads raw wine quality data from CSV files
2. **Data Validation:** Validates schema using `schema.yaml`
3. **Data Transformation:** Handles missing values, scaling, and feature engineering
4. **Model Training:** Trains a regression model with hyperparameter tuning
5. **Model Evaluation:** Evaluates performance metrics like R², MAE, RMSE
6. **Model Deployment:** Predicts wine quality via web interface using Flask

---

## 🧪 How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/wine-quality-prediction.git
cd wine-quality-prediction
```

### 2. Create Virtual Environment
```bash
conda create -p venv python=3.10 -y
conda activate venv/
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Full Pipeline
```bash
python main.py
```

### 5. Launch Web App
```bash
python app.py
```
Then navigate to: `http://localhost:8080/` in your browser.
---
### 6. To train the model from the Web Interface
Then navigate to: `http://train` in your browser.

## 📊 MLflow Tracking

The project uses MLflow to track model performance and parameters.  
To start the MLflow UI:
```bash
mlflow ui
```
Then open `http://localhost:5000` in your browser.

---

## 📌 Future Improvements

- Dockerization for easier deployment  
- CI/CD integration using GitHub Actions  
- Cloud deployment (AWS/GCP/Heroku)  
- Feature importance visualization using SHAP  

---

## 👨‍💻 Author

**Your Name**  
📫 [aniketkj9211@gmail.com]  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/aniketkr9211/)  


---

## ⭐ License

This project is licensed under the MIT License.
