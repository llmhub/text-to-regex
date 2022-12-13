# text-to-regex

<p align="center">
    <a href="https://www.llmhub.com/2/functions/21/share"><img src="https://img.shields.io/badge/LLMHub%20-%E2%AD%90%EF%B8%8F-brightgreen" alt="LLMHub"></a>
</p>

Uses GPT-3's latest `text-davanci-003` model via [LLMHub](https://www.llmhub.com) to convert text to Python `re` expressions. 

<img src="https://raw.githubusercontent.com/llmhub/text-to-regex/main/sample.jpg" />

There are two main features:
- explicit "assumptions". This lets you find errors, and iterate towards getting a final regex that "works".
- quickly test the regex on the same page and iterate towards


## Running your own server
```bash
# Setup Python environment.
conda create -n t2r python
conda activate t2r
pip install -r requirements.txt

# Setup LLMHub dependency.
npm install -g llmhub
llmhub auth

# Start Streamlit app.
streamlit run app.py
```

## TODO
1. Add ability to gather feedback from users (upvote/downvote).
2. People usually think of a string they want to match and then come up with a regex. So, we should change prompt so that it includes the string people are trying to again match against whilst coming up with the regex.
