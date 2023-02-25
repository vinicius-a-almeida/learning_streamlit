#importando as blibs
import pandas as pd
import streamlit as st
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


#titulo
st.write("""
Prevendo Diabetes\n
app que utiliza machine learning para predição de diabetes.\n
Fonte: PIMA - INDIA (kaggle)
""")

#dataset
df = pd.read_csv("/home/vinicius/UFERSA/learning_streamlit/diabetes.csv")


#cabeçalho
st.subheader("Informação dos dados")

user_input = st.sidebar.text_input("digite seu nome")

st.write("paciente :{}".format(user_input))

#dados de entrada

X = df.drop(['Outcome'], 1)
Y = df['Outcome']

#dados treinamento e teste

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#função para pegar os dados do usuario

def get_user_data():
    pregnancies = st.sidebar.slider("Gravidez", 0, 15, 1)
    glucose = st.sidebar.slider("glicose", 0, 200, 110)
    blood_pressure = st.sidebar.slider("pressão sanguinea", 0, 122, 72)
    skin_thickness = st.sidebar.slider("Espessura da pele", 0, 99, 20)
    insulin = st.sidebar.slider("insulina", 0, 900, 30)
    bmi = st.sidebar.slider("Indice de massa corporal", 0.0, 70.0, 15.0)
    dpf = st.sidebar.slider("Historico familiar de diabetes", 0.0, 3.0, 0.0)
    age = st.sidebar.slider("Idade", 15, 100, 21)

    user_data = {"gravidez": pregnancies,
             "glicose": glucose,
             "Pressão sanguinea": blood_pressure,
             "Espessura da pele": skin_thickness,
             "Insulina": insulin,
             "Indice massa corporal": bmi,
             "Historico familiar de diabetes": dpf,
             "Idade": age
             }
    #user_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]
    features = pd.DataFrame(user_data, index = [0])
    return features

user_input_variables = get_user_data()

#grafico

st.bar_chart(user_input_variables)

st.subheader("Dados do usuario")
st.write(user_input_variables)

dtc = DecisionTreeClassifier(criterion = 'entropy', max_depth = 3)
dtc.fit(x_train, y_train)

#acuracia do modelo
st.subheader('Acurácia do modelo')
st.write(accuracy_score(y_test, dtc.predict(x_test)) * 100)

#previsão

prediction = dtc.predict(user_input_variables)

st.subheader("previsão: ")
st.write(prediction)