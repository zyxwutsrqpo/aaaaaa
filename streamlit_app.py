import streamit as at
import random
st.title("おみくじアプリ")
if st.buttun("おみくじを引く")
results=["大吉"、"中吉"、"小吉"、"吉"、"凶"、"大凶"]
result=random.choice(results)
st.write(f"結果:{result}")