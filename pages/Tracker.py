import streamlit as st
import pandas as pd

from st_aggrid import AgGrid,GridUpdateMode
from st_aggrid import GridOptionsBuilder

st.set_page_config(
    page_title="Tracker",
    page_icon="excel"
)

def data_upload():
    df=pd.read_csv("Test_data.csv")
    return df

df = data_upload()
#st.dataframe(data=df)
#st.info(len(df))

gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_pagination(enabled=True)
gd.configure_default_column(editable=True,groupable=True)

sel_mode = st.radio('selection Type', options = ['single','multiple'])
gd.configure_selection(selection_mode=sel_mode,use_checkbox=True)
gridoptions = gd.build()
grid_Table = AgGrid(df,gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED,
                    height=500,
                    allow_unsafe_jscode=True)

sel_row = grid_Table["selected_rows"]
st.write(sel_row)
