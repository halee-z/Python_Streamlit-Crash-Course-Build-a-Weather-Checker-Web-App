import streamlit as st
import random

def get_fake_weather(city):
    conditions = ["Sunny", "Cloudy", "Rainy", "Windy", "Stormy"]
    temperature = random.randint(15, 40)
    condition = random.choice(conditions)
    return condition, temperature

# Streamlit App UI
st.title("🌤️ Simple Weather Checker")

city = st.text_input("Enter a city name:")

if city:
    condition, temp = get_fake_weather(city)
    st.subheader(f"Weather in {city}")
    st.write(f"Condition: {condition}")
    st.write(f"Temperature: {temp}°C")
