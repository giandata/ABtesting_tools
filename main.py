import streamlit as st
from views import conversion_rates


with st.sidebar:
    st.markdown(
        "Author: [Giancarlo Di Donato](https://www.linkedin.com/in/giancarlodidonato/)")


st.title('AB Testing tools 🧪')
# buy me a coffee


options = ["Sample size", "Test duration", "Conversion rates",
           "Statistical significance", "Z-score", "Bayesian AB test"]
page = st.radio('Select a calculator', options)

if page == "Conversion rates":

    conversion_rates.render()

    # st.write('Tests for statistical significance are used to address the question: what is the probability that what we think is a relationship between two variables is really just a chance occurrence?')

else:
    st.info("Section work in progress")
