import streamlit as st

st.title('AB Testing tools')

st.header("Calculate Conversion")
st.write('Introduce the number of visitors and conversions in each group to calculate the conversion rates')


def conversions(cc, tc):
    if tc > cc:
        return "Test"
    elif tc < cc:
        return "Control"
    elif tc == cc:
        return "Same"


conversion_form = st.form('conversion rate')
conversion_form.subheader("Control group")
control_visitors = conversion_form.number_input(
    label='Visitors', min_value=1, step=1, key='control_vis', help='How many participants there are in the control group?')
control_conversions = conversion_form.number_input(
    label='Conversions', min_value=1, step=1, key='control_conv')
conversion_form.subheader("Test group")
test_visitors = conversion_form.number_input(
    label='Test group', step=1, min_value=1, key='test_vis', help='How many participants there are in the test group?')
test_conversions = conversion_form.number_input(
    label='Conversions', step=1, min_value=1, key='test_conv')
submit = conversion_form.form_submit_button('Calculate')

if submit:

    # make sure do not divide by 0
    # check if conversion is higher than visits
    if (control_conversions > control_visitors | test_conversions > test_visitors):
        st.warning("Conversions must be lower than visitors")
    else:

        cc = round(control_conversions/control_visitors*100, 2)
        tc = round(test_conversions/test_visitors*100, 2)
        conv_diff = round(tc - cc, 2)
        conv_impr = round((conv_diff/control_conversions)*100, 1)
        conv_change = round((conv_diff/test_conversions)*100, 1)

        if tc > cc:
            st.write(
                f"The {conversions(cc,tc)} group has higher conversion. It converts {(conv_diff)} points more, which is a {conv_impr} percent improvement.")

        if tc < cc:
            st.write(
                f"The {conversions(cc,tc)} group has higher conversion. It converts {( - conv_diff)} percentual points more, which is a  {conv_change} % change.")

        if tc == cc:
            st.write(
                "Control and test groups have the same conversion.")
            st.metric(label='Conversion:', value=f"{cc} %")
        else:
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label='Conversion in the control group',
                          value=f"{cc} %", delta=f"{ -conv_diff} %")
            with col2:
                st.metric(label='Conversion in the test group',
                          value=f"{tc} %", delta=f"{conv_diff} %")


# st.write('Tests for statistical significance are used to address the question: what is the probability that what we think is a relationship between two variables is really just a chance occurrence?')
