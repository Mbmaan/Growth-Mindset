import string
import random
import streamlit as st
import re

st.title("Growth Mindset Web App")
st.write("Welcome to the Growth Mindset Challenge!")

# Learning Goals Input
st.header("Set Your Learning Goals")
goals = st.text_input("What are your learning goals?")
if st.button("Submit"):
    st.write(f"Your learning goals: {goals}")

    # Reflection Journal
st.header("Reflection Journal")
reflection = st.text_area("Reflect on your learning experiences:")
if st.button("Save Reflection"):
    st.write("Your reflection has been saved!")

    # Feedback Section
st.header("Feedback")
feedback = st.text_area("Share your feedback or experiences:")
if st.button("Submit Feedback"):
    st.write("Thank you for your feedback!")

    # Resources Section
st.header("Resources")
st.write("Here are some resources to help you develop a growth mindset:")
st.markdown("""
- [Mindset: The New Psychology of Success by Carol S. Dweck](https://www.amazon.com/Mindset-Psychology-Carol-S-Dweck/dp/0345472322)
- [TED Talk: The Power of Believing That You Can Improve](https://www.ted.com/talks/carol_dweck_the_power_of_believing_that_you_can_improve)
- [Growth Mindset Resources](https://www.mindsetworks.com/)
""")
