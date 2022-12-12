# text-to-regex

<p align="center">
    <a href="https://www.llmhub.com/abhagsain/ai-cli"><img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fapi.llmhub.com%2Fshields%2Fstars%2Fvatsalaggarwal%2Ftext-to-regex" alt="LLMHub"></a>
</p>

Uses GPT-3's latest `text-davanci-003` model via [LLMHub](https://www.llmhub.com) to convert text to Python `re` expressions. 

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
