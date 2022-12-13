import re

import streamlit as st
from llmhub.client import Client as LLMHubClient

llm = LLMHubClient("https://www.llmhub.com/2/functions/21/share")


@st.cache
def run_llm(input_data):
    result = llm.run(input_data)
    return result


st.set_page_config(page_title="Text-to-Regex", page_icon="🔍")

st.title("Text to Python `re` Converter")
st.markdown(
    """ 
            <p align="center">
                <a href="https://github.com/llmhub/text-to-regex"><img src="https://badgen.net/badge/icon/GitHub?icon=github&label" alt="GitHub"></a>
                <a href="https://www.llmhub.com/2/functions/21/share"><img src="https://img.shields.io/badge/LLMHub%20-%E2%AD%90%EF%B8%8F-brightgreen" alt="LLMHub"></a>
            </p>
            """,
    unsafe_allow_html=True,
)

text_input = st.text_input("Describe your Regex in plain English (make sure to end it with a .):")

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

    # Allow user to input a string to check if it matches their regex.
    regex_check_input = st.text_input("Input a string to check if it matches your regex:")
    if len(regex_check_input) > 0:
        regex = re.search("Regex: `(.*)`", output.strip()).group(1)

        if re.match(regex, regex_check_input):
            st.write("✅ Match!")
        else:
            st.write("❌ No Match!")

    st.write("The text-to-regex query took ", str(round(latency, 1)), "seconds to run.")
