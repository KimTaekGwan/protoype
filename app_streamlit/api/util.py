import os
import streamlit as st


# 디렉토리와 파일을 주면, 해당 디렉토리에 파일을 저장하는 함수!!
def save_uploaded_file(directory, file):
    # 1. 디렉토리가 있는지 확인하여, 없으면 만든다.
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 2.이제는 디렉토리가 있으니, 파일을 저장
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())
    return st.success('Saved file: in '.format(file.name, directory))
