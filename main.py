import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title='Heart Disease Prediction ',layout='centered')
st.title("CORONARY HEART DISEASE PREDICTION USING ML MODELS")

#load dataset
data =pd.read_csv(r"framingham.csv")

#filling the missing values by mean values
data.fillna(data.mean(),inplace=True)

#droping unnecessary columns

data.drop(columns=['currentSmoker', 'diaBP', 'prevalentHyp'], inplace=True)

#splitting the dataset into input and output
x=data.drop(columns=['TenYearCHD'])
y=data['TenYearCHD']

#splitting the dataset into training and testing sets
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.2,random_state=7)

#models to be used
models={
    'KNN':KNeighborsClassifier(),
    "Logistic Regression":LogisticRegression(),
    "Decision tree":DecisionTreeClassifier(),
    "Naive Bayes":GaussianNB(),
    "SVM":SVC(),
    "Random Forest":RandomForestClassifier()}

#selection of model
model_choice=st.selectbox("Choose a Model",list(models.keys()))
if st.button("Accuracy"):
    model=models[model_choice]
    model.fit(X_train,Y_train)
    acc=accuracy_score(Y_test,model.predict(X_test))
    st.success(f"Accuracy of {model_choice}: {acc:.2f}")



# comparing all models
if st.button("Compare All Models"):
    results=[]
    best_model_name=None
    best_model=None
    best_accuracy=0
    for name,model in models.items():
        model.fit(X_train,Y_train)
        accuracy=accuracy_score(Y_test,model.predict(X_test))
        results.append({"model":name,"accuracy":accuracy})
        if accuracy > best_accuracy:
            best_accuracy=accuracy
            best_model_name=name
            st.session_state.best_model=model

    results=pd.DataFrame(results)
    st.write(results.sort_values(by="accuracy", ascending=False))
    st.success(f"Best Model: {best_model_name} with accuracy: {best_accuracy:.2f}")
    

#predicting for asingle patient
st.subheader("Predict for a single patient")
st.write("Enter the values for the features of the patient:")
user_input=[st.number_input(col,value=0.0) for col in x.columns]
if st.button("Predict Disease Risk"):
    if "best_model" in st.session_state:
        prediction = st.session_state.best_model.predict([user_input])
        if prediction[0] == 1:
            st.success("The patient is at risk of coronary heart disease.")
        else:
            st.success("The patient is not at risk of coronary heart disease.")
    else:
        st.warning("Please click 'Compare All Models' first to determine the best model.")    
