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
    file = st.file_uploader('파일 선택(csv or excel)',
                            type=['pdf', 'pptx', 'ppt'])

    if st.button('검색'):
        with st.expander("검색 결과"):
            with st.spinner('Wait for it...'):
                res = req_doc2vec(file_name=file.name)
                query_result = chroma_db.query(res['text'])
                st.write(query_result)
    if file is not None:
        # 파일 읽기
        name, ext = file.name.split('.')[0], file.name.split('.')[-1]

        save_uploaded_file(path_database_input, file)

        if st.button('벡터화'):
            with st.expander("벡터 검사 결과"):
                with st.spinner('Wait for it...'):
                    st.write(req_doc2vec(file_name=file.name))

        if st.button('db 추가'):
            with st.spinner('Wait for it...'):
                res = req_doc2vec(file_name=file.name)
                embedding = res['text']
                document = '?'
                metadata = {'file_name': file.name}
                id = file.name
                chroma_db.db_add(embedding, document, metadata, id)


#############################################
page_title = '표절검사'
page_icon = '😃'

st.set_page_config(page_title=page_title,
                   layout='wide',
                   page_icon=page_icon
                   )

last_params = {
    # '결과': None,
}
elements = last_params.copy()
path_database_input = '../database/data/input'
chroma_db = Initdb()

#############################################
# 사이드바

#############################################
# 본문

# 제목
st.markdown(f"# {page_title} {page_icon}")

# InputLayout
createInputLayout(elements)
