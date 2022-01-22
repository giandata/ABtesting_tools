import streamlit as st


def render():

    st.header('Calculate the sample size')
    st.write(
        'Insert the  desired increment, the significance level and the statistical power for the experiment')

    sample_form = st.form('Sample size calculator')
    sample_form.subheader("Experiment parameter settings")
    mde = round(sample_form.number_input(min_value=0.1, label="Minimum detectable effect %",
                                         step=0.1, help='The desired relevant difference between the rates you would like to discover'), 2)
    sign_level = sample_form.radio(label="Significance level",
                                   options=[80, 85, 90, 95, 99, 100])
    test_power = sample_form.slider(
        label='Test power %', min_value=80, help="the probability of detecting that difference between the original rate and the variant conversion rates")
    submit = sample_form.form_submit_button('Calculate')

    if submit:
        st.subheader("Sample size per variant needed: {}")
        st.info(
            f"To observe at  least a {mde} % improvement with a {sign_level} % significance levels and a {test_power} % probability, the experiment will need a sample of ... ")
