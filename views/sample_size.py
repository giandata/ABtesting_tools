import streamlit as st
from experiments import sample_size


def render():

    st.header('Calculate the sample size')
    st.write(
        'Insert the  desired increment, the significance level and the statistical power for the experiment')

    sample_form = st.form('Sample size calculator')
    sample_form.subheader("Experiment parameter settings")
    baseline = round(sample_form.number_input(
        label="Baseline conversion", min_value=0.1, value=20.0, step=0.01), 2)

    mde = round(sample_form.slider(min_value=1, max_value=50, value=5, label="Minimum detectable effect %",
                                   help='The desired relevant difference between the rates you would like to discover'), 2)
    sign_level = sample_form.radio(label="Confidence level %",
                                   options=[90, 95, 98, 99], help="Establish the significance level")
    test_power = sample_form.radio(
        label='Test power %', options=[80, 90, 95], help="the probability of detecting that difference between the original rate and the variant conversion rates")
    submit = sample_form.form_submit_button('Calculate')

    if submit:

        sample = sample_size.sample_size_calc(
            sign_level, test_power, baseline, mde)

        st.subheader(f"Sample size per variant needed: {sample}")
        st.info(
            f"To observe at  least a {mde} % improvement with a {sign_level} % significance levels and a {test_power} % probability, the experiment will need a sample of  {sample} for each variant")
