import streamlit as st 

st.set_page_config(page_title="BMI Calculator",page_icon="⚖️",layout="centered")
st.title("⚖️ BMI Calculator")
st.write("Let's Calculate Your **BODY MASS INDEX [BMI]** And Understand What It Means")

st.header("🖊️ Enter Your Details ")

height = st.number_input("Enter Your Height (cm)", min_value=90,max_value=200,value=170)
weight = st.number_input("Enter Your Weight (kg)", min_value=10,max_value=200,value=65)

st.write(f"📏 Your Height : {height} in cm")
st.write(f"🏋🏻 Your Weight : {weight} in kg")

if st.button("Calculate BMI"):
    h_m = height / 100   # converting cm to meters 
    bmi = weight / (h_m ** 2)
    st.success(f"YOUR BMI IS **{bmi :.2f}** 💪🏼")

    # Print BMI Category
    if bmi < 18.5:
        category = "Underweight 😶‍🌫️"
        color = "#ED9821"

    elif 18.5 <= bmi < 25:
        category = "Normal 😁"
        color = "#1C8022"
    
    elif 25 <= bmi < 30:
        category = "Overweight 😳"
        color = "#0022FF"
    
    else:
        category = "Obese 😵‍💫"
        color = "#BA1406"

    st.write(category)


st.markdown(
        f"""
        <div style='background-color:{color};padding:15px;border-radius:10px;text-align:center'>
        <h3>Your BMI Category : {category}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )