
import streamlit as st
import pandas as pd

# CSV 불러오기
df = pd.read_csv('dialect.csv')
df.columns = df.columns.str.strip()
df.dropna(inplace=True)
standard_to_dialect = dict(zip(df['표준어'], df['사투리']))

# 길이순 정렬로 긴 표현 먼저 치환
def translate(sentence):
    for standard, dialect in sorted(standard_to_dialect.items(), key=lambda x: -len(x[0])):
        sentence = sentence.replace(standard, dialect)
    return sentence

# Streamlit UI
st.title("📘 표준어 → 사투리 번역기 (간단치환)")
st.write("표준어 문장을 입력하면 일부 단어 또는 구문을 사투리로 바꿔줍니다.")

user_input = st.text_input("👉 표준어 문장을 입력하세요:")

if user_input:
    result = translate(user_input)
    st.write("🗣️ 번역 결과:")
    st.success(result)
