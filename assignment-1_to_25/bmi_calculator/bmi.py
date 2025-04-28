import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="🤸")
st.title("BMI Calculator 🏋️♂️")
st.markdown("Discover your Body Mass Index and health status! 📈")

# Using columns for better layout
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Enter your weight (Kg) 🏋️", 
                           min_value=30.0, 
                           max_value=300.0,
                           value=65.0)
with col2:
    height = st.number_input("Enter your height (cm) 📏", 
                           min_value=100.0, 
                           max_value=250.0,
                           value=170.0)

# Add visual separation
st.divider()

if st.button("Calculate BMI 🧮", type="primary"):
    # Convert height to meters and calculate BMI
    height_in_m = height / 100
    bmi = weight / (height_in_m ** 2)
    
    # Display results with emojis and styling
    st.balloons()
    st.success(f"Your BMI is: **{bmi:.1f}** 📊")
    
    # Health status with emojis and color coding
    if bmi < 18.5:
        st.warning("Underweight 🩺\n\nEat more frequently and choose nutrient-rich foods!")
    elif 18.5 <= bmi < 24.9:
        st.info("Healthy Weight ✅\n\nGreat job! Maintain your balanced diet!")
    elif 25 <= bmi < 29.9:
        st.warning("Overweight ⚠️\n\nConsider more physical activity and healthier food choices!")
    else:
        st.error("Obese 🚨\n\nConsult a healthcare professional for guidance!")
    
    # BMI category chart
    st.divider()
    st.subheader("BMI Categories ℹ️")
    st.markdown("""
    - **Underweight**: < 18.5 🟦
    - **Healthy Weight**: 18.5 - 24.9 🟩
    - **Overweight**: 25 - 29.9 🟧
    - **Obese**: 30+ 🟥
    """)

# Footer
st.divider()
st.caption("Made with ❤️ using Streamlit | Maintain a healthy lifestyle! 🍎🏃♀️")