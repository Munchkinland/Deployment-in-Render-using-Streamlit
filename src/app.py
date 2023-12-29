from pickle import load
import streamlit as st

model_path = r"C:\Users\Rubén\Desktop\Deployment-in-Render-using-Streamlit\models\decision_tree_classifier_default_42.sav"

with open(model_path, "rb") as model_file:
    model = load(model_file)

class_dict = {
    "0": "Iris setosa",
    "1": "Iris versicolor",
    "2": "Iris virginica"
}

st.title("Iris - Model prediction")

val1 = st.slider("Petal width", min_value=0.0, max_value=4.0, step=0.1)
val2 = st.slider("Petal length", min_value=0.0, max_value=4.0, step=0.1)
val3 = st.slider("Sepal width", min_value=0.0, max_value=4.0, step=0.1)
val4 = st.slider("Sepal length", min_value=0.0, max_value=4.0, step=0.1)

if st.button("Predict"):
    prediction = str(model.predict([[val1, val2, val3, val4]])[0])
    pred_class = class_dict[prediction]
    st.write("Prediction:", pred_class)
