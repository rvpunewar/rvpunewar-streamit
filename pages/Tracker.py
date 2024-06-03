import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
from st_aggrid import AgGrid

st.set_page_config(
    page_title="Dataframe demo",
    page_icon="excel"
)

data = {'Date':['John','Anna','Peter'],
        'Age':[28,35,45]

       }

df =pd.DataFrame(data)

AgGrid(df)



