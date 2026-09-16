import streamlit as st
st.title("💵 Bill Splitter")
a = st.number_input("Bill subtotal ($)", min_value=0.0, value=50.0, step=1.0, key="subtotal")
b = st.slider("Tip %", min_value=0, max_value=30, value=18, key="tip")
c = st.number_input("Number of people", min_value=1, value=2, step=1, key="people")
t = round(a*b/100,2)
g = round(a+t,2)
p = round(g/c,2)
st.write("Tip: $"+str(t))
st.write("Grand total: $"+str(g))
st.write("Per person: $"+str(p))
if b>=20:
    st.success("That's a generous tip! 🎉")
else:
    st.info("Tip 20% or more to be considered generous.")
