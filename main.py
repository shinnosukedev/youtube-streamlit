# py -m pip install streamlit --user

import streamlit as st
import numpy as np
import pandas as pd

st.title('For study')

st.write('DataFrame')
Shinjuku = [35.69, 139.70]
df = pd.DataFrame(
    np.random.rand(100,2)/[10,10]+Shinjuku,
    columns=['lat','lon']
)

st.map(df)