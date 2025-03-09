import streamlit as st
import random
import pandas as pd

def main():
    st.title('クイズアプリ')

    base_dir='/content/drive/MyDrive/networkspecialist/'
    #df=pd.read_csv(f'{base_dir}output.csv')

    if 'state' not in st.session_state:
      st.session_state["state"] = 0


    if 'question' not in st.session_state:
      st.session_state["question"] = ''

    if 'answer' not in st.session_state:
      st.session_state["answer"] = ''

    if 'index' not in st.session_state:
      st.session_state["index"] = 0

    @st.fragment
    def quiz():
      #st.write('問題：',st.session_state['question'])
      #st.write('答え：',st.session_state['answer'])

      col1, col2 = st.columns(2)

      with col1:
        if st.button('次の問題',key=1) :
          st.session_state['index']=random.randint(0,len(df))


      with col2:
        if st.button('解答を表示',key=0):
          st.session_state['index']=random.randint(0,len(df))


      st.write('問題：',st.session_state['question'])
      st.write('答え：',st.session_state['answer'])



    quiz()

if __name__ == '__main__':
    main()
