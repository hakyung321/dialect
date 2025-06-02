
import streamlit as st
import pandas as pd
from soynlp.tokenizer import LTokenizer

# CSV 불러오기
df = pd.read_csv('dialect.csv')
df.columns = df.columns.str.replace('\ufeff', '').str.strip()
df.dropna(subset=['사투리', '표준어'], inplace=True)

# 표준어 → 사투리 dict
standard_to_dialect = dict(zip(df['표준어'].str.strip(), df['사투리'].str.strip()))

# 간단한 LTokenizer 초기화 (길이 우선 토크나이저)
tokenizer = LTokenizer()

# 형태소 기반 치환 함수
def translate_with_soynlp(sentence):
    tokens = tokenizer.tokenize(sentence)
    translated = [standard_to_dialect.get(token, token) for token in tokens]
    return ' '.join(translated)

# Streamlit UI
st.title("📘 표준어 → 사투리 번역기 (형태소 기반)")
st.write("문장을 입력하면 사투리로 바꿔줍니다.")

user_input = st.text_input("👉 표준어 문장을 입력하세요:")

if user_input:
    result = translate_with_soynlp(user_input)
    st.write("🗣️ 번역 결과:")
    st.success(result)
