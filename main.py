import streamlit as st
from views import conversion_rates, sample_size


with st.sidebar:
    st.markdown(
        "Author: [Giancarlo Di Donato](https://www.linkedin.com/in/giancarlodidonato/)")


st.title('AB Testing tools 🧪')
# buy me a coffee


options = ["Sample size", "Test duration", "Conversion rates",
           "Statistical significance", "Bayesian AB test"]
page = st.radio('Select a calculator', options)

if page == "Sample size":

    sample_size.render()

if page == "Conversion rates":

    conversion_rates.render()

    # st.write('Tests for statistical significance are used to address the question: what is the probability that what we think is a relationship between two variables is really just a chance occurrence?')
