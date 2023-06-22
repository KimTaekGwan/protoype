import streamlit as st

import time
import numpy as np
import pandas as pd
import os


from api.util import save_uploaded_file
from api.request_fastapi import req_doc2vec
from api.manage_vetcordb import Initdb
# Input Layout 생성


def createInputLayout(elements):
    pass


#############################################
page_title = 'VectorDB'
page_icon = '😃'

st.set_page_config(page_title=page_title,
                   layout='wide',
                   page_icon=page_icon
                   )

last_params = {
    # '결과': None,
}
elements = last_params.copy()


# path_database_input = '../database/data/input'

#############################################
# 사이드바

#############################################
# 본문

# 제목
st.markdown(f"# {page_title} {page_icon}")

# InputLayout
createInputLayout(elements)
