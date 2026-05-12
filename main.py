import streamlit as st
st.title('나의 첫 앱 서비스')
a=st.text_input( '이름을 입력하세요')
b=st.selectbox('좋아하는 음식을 선택하세요!', ['마라탕', '피자', '볶음밥'])
if st.buttom('인사말 생성'):
  st.write(a+'님, 안녕하세요!')
