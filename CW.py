import streamlit as st
st.set_page_config(layout="wide")
import warnings
import pandas as pd
from datetime import datetime
import warnings
import os, fnmatch
from PIL import Image
import glob
warnings.filterwarnings("ignore")

st.title("Markah Course Work WAIP")
id = st.number_input("Insert your ID : ", value=0, placeholder="Type your ID...")
st.write('The ID entered is ', id)
cw_df = pd.read_csv("CW.csv")
# st.write(cw_df)
cw_df = cw_df.reset_index(drop=True)
cw_df.index = cw_df.index+1
result = cw_df.loc[cw_df["ID"]==id]
st.dataframe(result['Mark'],hide_index=True)

# display = st.dataframe(
#         result,hide_index=True,
#         column_config={
#             "ID": st.column_config.NumberColumn(
#                 "ID", help="Matric Number", min_value=0, format="%d"
#             )
#         },
#     )
