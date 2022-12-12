import re

import streamlit as st
from llmhub.client import Client as LLMHubClient

llm = LLMHubClient("https://www.llmhub.com/2/functions/21/share")

st.title("Text to Python `re` Converter")

text_input = st.text_input("Describe your Regex in plain English (make sure to end it with a .):")


@st.cache
def run_llm(input_data):
    result = llm.run(input_data)
    return result


if len(text_input) > 0:
    # Run LLM.
    result = run_llm({"description": text_input})
    output = result["output"]
    latency = result["duration_s"]

    for l in output.split("\n"):
        if "Assumption:" in l:
            st.markdown(f'<h1 style="color:red;font-size:24px;">{l}</h1>', unsafe_allow_html=True)
        elif "Step-by-step: " in l or "- " in l:
            pass
        else:
            st.write(l)

    # # User Feedback on Results.
    # feedback_buttons = st.columns(2)
    # feedback_buttons[0].button("👍")
    # feedback_buttons[1].button("👎")

    # Allow user to input a string to check if it matches their regex.
    regex_check_input = st.text_input("Input a string to check if it matches your regex:")
    if len(regex_check_input) > 0:
        regex = re.search("Regex: `(.*)`", output.strip()).group(1)

        if re.match(regex, regex_check_input):
            st.write("✅ Match!")
        else:
            st.write("❌ No Match!")

    st.write("The text-to-regex query took ", str(round(latency, 1)), "seconds to run.")
