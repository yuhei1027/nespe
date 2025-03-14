import streamlit as st
import random
import pandas as pd
from glob import glob


base_dir='./contents'
df=pd.read_csv(f'{base_dir}/nespe_output.csv')

category_list=df['category'].unique().tolist()
category_flag=[]
for i,category in enumerate(category_list):
    a=st.checkbox(category_list[i])
    if a:
        category_flag.append(category_list[i])
a=st.checkbox('すべて選択')
if a:
    category_flag=category_list.copy()
if len(category_flag)>0:
    df=df[df['category'].isin(category_flag)].reset_index(drop=True)

if 'state' not in st.session_state:
    st.session_state["state"] = 0

if 'category' not in st.session_state:
    st.session_state["category"] = ''

if 'question' not in st.session_state:
    st.session_state["question"] = ''

if 'answer' not in st.session_state:
    st.session_state["answer"] = ''

if 'explanation' not in st.session_state:
    st.session_state["explanation"] = ''

if 'index' not in st.session_state:
    st.session_state["index"] = 0


col1, col2 = st.columns(2)

with col1:
    if st.button('次の問題',key=1) and st.session_state['state']==0:
        st.session_state['index']=random.randint(0,len(df))
        st.session_state['category']=df['category'].iloc[st.session_state['index']]
        st.session_state['question']=df['question'].iloc[st.session_state['index']]
        st.session_state['answer']=''
        st.session_state['explanation']=''
        st.session_state['state']=1


with col2:
    if st.button('解答を表示',key=0)  and st.session_state['state']==1:
        st.session_state['category']=df['category'].iloc[st.session_state['index']]
        st.session_state['question']=df['question'].iloc[st.session_state['index']]
        st.session_state['answer']=df['answer'].iloc[st.session_state['index']]
        st.session_state['explanation']=df['explanation'].iloc[st.session_state['index']]
        st.session_state['state']=0


st.write('カテゴリ：',st.session_state['category'])
st.write('問題：',st.session_state['question'])
st.write('答え：',st.session_state['answer'])
st.write('解説：',st.session_state['explanation'])


