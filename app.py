
import streamlit as st
import pandas as pd
import re

# CSV 불러오기
df = pd.read_csv('dialect.csv')
df.columns = df.columns.str.replace('\ufeff', '').str.strip()
df.dropna(subset=['사투리', '표준어'], inplace=True)

# 표준어 → 사투리 dict
standard_to_dialect = dict(zip(df['표준어'].str.strip(), df['사투리'].str.strip()))

# 단어 단위 치환 함수
def translate_sentence(sentence):
    result = sentence
    for standard, dialect in sorted(standard_to_dialect.items(), key=lambda x: -len(x[0])):
        result = re.sub(rf'\b{re.escape(standard)}\b', dialect, result)
    return result

# Streamlit UI
st.title("📘 표준어 → 사투리 번역기")
st.write("문장을 입력하면 사투리로 바꿔줍니다.")

user_input = st.text_input("👉 표준어 문장을 입력하세요:")

if user_input:
    result = translate_sentence(user_input)
    st.write("🗣️ 번역 결과:")
    st.success(result)
