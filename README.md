
# Coronary Heart Disease Prediction Web App 🫀

An interactive web application built with **Streamlit** to predict a patient’s 10-year risk of developing **Coronary Heart Disease (CHD)**. The app uses various machine learning models and clinical inputs from the **Framingham Heart Study** dataset.

🔗 **Live App**: [coronary-heart-disease-prediction-knjagdeessamal.streamlit.app](https://coronary-heart-disease-prediction-knjagdeessamal.streamlit.app/)

---

## 🎯 Key Features

- 📌 **Model Selection Dropdown**
- 🧠 **Accuracy Button** for single-model evaluation
- 📊 **Compare All Models** to view all scores side by side
- 👤 **Single Patient Risk Prediction** with sliders/inputs
- 🎨 **Styled Output** for clear interpretation
- ✅ Robust error handling and session state management

---

## 🗄️ Dataset

Uses data from the **Framingham Heart Study**, featuring patient records with attributes like:

- Demographics: `male`, `age`, `education`
- Health Indicators: `cigsPerDay`, `BPMeds`, `prevalentStroke`, `diabetes`
- Clinical Metrics: `totChol`, `sysBP`, `BMI`, `heartRate`, `glucose`

📁 Available on [Kaggle](https://www.kaggle.com/datasets/aasheesh200/framingham-heart-study-dataset)

---

## ⚙️ How to Run Locally

```bash
# Install required dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run main.py
🧭 Using the App
Interact with the Coronary Heart Disease Prediction App in these steps:

Choose a Model Use the "Choose a Model" dropdown to select a classification algorithm (e.g., KNN, Logistic Regression, Decision Tree).

Display Accuracy Click the "Accuracy" button to view how well the selected model performs on the dataset.

Compare Models Optionally, click "Compare All Models" to see the accuracy scores of all available models side by side.

Input Patient Details Under "Predict for a single patient", manually enter values for features such as:

male, age, education

cigsPerDay, BPMeds, prevalentStroke, diabetes

totChol, sysBP, BMI, heartRate, glucose

Predict Risk Click "Predict Disease Risk" to generate a styled message indicating whether the patient is at risk or not at risk of coronary heart disease.

🩺 Sample Output
"The patient is not at risk of coronary heart disease." or "The patient is at risk of coronary heart disease."

Styled dynamically using Streamlit’s Markdown rendering.

👨‍💻 Developed By
Built with ❤️ by Jagdees Samal Focused on bringing accessible machine learning solutions to healthcare.

📜 License
This project is licensed for educational and non-commercial use. Dataset attribution: Framingham Heart Study.


---

Want to spruce it up further with a badge for Streamlit Cloud or maybe an app screenshot next to the patient input panel? I’ve got you covered!
https://coronary-heart-disease-prediction-knjagdeessamal.streamlit.app/ use this link and write the readme
Absolutely, Jagdees! Based on your deployed Streamlit app at coronary-heart-disease-prediction-knjagdeessamal.streamlit.app, here’s a polished and deployment-ready README.md tailored for your GitHub repository:


---

