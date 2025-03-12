import streamlit as st
import random
import pandas as pd


page1 = st.Page(page="contents/page1.py", title="ネスぺワークブック", icon=":material/home:")
page2 = st.Page(page="contents/page2.py", title="ネスぺイージス", icon=":material/open_with:")
pg = st.navigation([page1,page2])
pg.run()
