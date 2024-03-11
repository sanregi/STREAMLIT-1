import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="EBAC | Módulo 15 | Streamlit I | Exercício",
    # page_icon="https://ebaconline.com.br/favicon.ico",
    page_icon="https://raw.githubusercontent.com/sanregi/STREAMLIT-1/main/favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown('''
<img src="https://github.com/sanregi/STREAMLIT-1/blob/main/newebac_logo_black_half.png?raw=true" alt="ebac-logo">

---

# **Profissão: Cientista de Dados**
### **Módulo 15** | Streamlit I | Exercício

Aluno [Regis Sandes](https://www.linkedin.com/in/r%C3%A9gis-sandes-b702a4123/)<br>
Data: 3 de março de 2024.

---
            ''', unsafe_allow_html=True)


st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

###############################################

st.write("SINASC RO 2019:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


import numpy as np

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)


dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))


dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


st.write(st.__version__)


df = pd.read_csv("G:\Ebac 2\Modulo 15\input_M15_SINASC_RO_2019.csv")

@st.cache
def convert_df(df):
   return df.to_csv().encode('utf-8')


csv = convert_df(df)

st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)


st.text('Tarefa 2')


st.caption('Balloons. Hundreds of them...')


def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)

with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)


import altair as alt

df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)


import time

@st.cache_data  # 👈 Added this
def expensive_computation(a, b):
    time.sleep(2)  # This makes the function take 2s to run
    return a * b

a = 2
b = 21
res = expensive_computation(a, b)

st.write("Result:", res)



@st.cache(suppress_st_warning=True)
def expensive_computation(a, b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)  # This makes the function take 2s to run
    return a * b

a = 2
b = 210  # 👈 Changed this
res = expensive_computation(a, b)

st.write("Result:", res)


'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'