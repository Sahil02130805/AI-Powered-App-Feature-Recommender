import streamlit as st

st.title("AI App Feature Recommender")

business_type = st.text_input("Enter your business type (e.g., Restaurant, Salon):")
budget = st.number_input("Enter your budget ($)", min_value=0)

if st.button("Recommend Features"):
    if business_type:
        recommendations = recommend_features(business_type, budget)
        st.subheader("Recommended Features:")
        for feature in recommendations:
            st.write("✅", feature)
    else:
        st.warning("Please enter a business type.")
