import streamlit as st

st.set_page_config(page_title="BMI Calculator",page_icon="⚖️",layout="centered")
st.title("🦾 BMI Calculator")
st.write("Let's Calculate Your **BODY MASS INDEX [BMI]** And Understand What It Means")

st.header("🖋️Enter Your Details")

height = st.number_input('Enter Your Height In cm',min_value=90,max_value=200,value=160)
weight = st.number_input('Enter Your Weight In kg',min_value=10,max_value=200,value=65) 

st.write(f"📏 Your Height : {height} in cm")
st.write(f"⚖️ Your Weight  : {weight} in cm")

if st.button("Calculate BMI"):
    h_m = height / 100                         #concert cm to metres 
    bmi = weight / (h_m ** 2)                  # calculating the BMI
    st.success(f"Your BMI is **{bmi:.2f}**")   # :.2f for 2 float after decimal

 # Print BMI Category
    if bmi < 18.5:                     # >18.5
        category = "Underweight 😟"
        color = "#FEF7C7"                # change this color later

    elif bmi <= 24.9:                      # 18.5 -24.9
        category = "Normal 😁"
        color = "#BAEFC0"                 # change this color later

    elif bmi <= 29.9:                      # 25.0.29.9
        category = "Overweight 😬"
        color = "#80AAEA"                  # change this color later
    
    elif bmi <= 34.9: 
        category = "Obesity (Class 1 😱)"
        color = "#EFA9A9" 

    else: 
        category = "Obesity (Class 2) 🤯"           # >30
        color = "#F5A190"

    st.markdown(
        f"""
        <div style='background-color:{color};padding:15px;border-radius:10px;text-align:center'>
        <h3>Your BMI Category : {category}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )




