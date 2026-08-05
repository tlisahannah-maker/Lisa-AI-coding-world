# main.py (Streamlit)
# Switch provider bby changing the import line:
from groq import generate_response  # For Groq
# from hf import generate_response  # For Hugging Face

import streamlit as st
import re

def looks_incomplete(text: str) -> bool:
    if not text or len(text.strip()) < 10:
        return True

    t = text.strip()

    # commom "cut" signs: ends mid word, mid-markdown, or no closing punctuation
    if t.endswith(('**', '*', '-', '—', ':', ',', '(', '[', '{')):
        return True

    if re.search(r"\d+\.\s*\*\*$", t):  # like 3. **
        return True

    if not re.search(r"[.!?]\s*$", t):  # no sentence-ending punctuation
        return True

    return False

def complete_answer(question: str, max_rounds: int = 2) -> str:
    # Ask for a clean structured answer (help avoid unfinished answers)
    base_prompt = (
        "Answer clearly in numbered points."
        "Do not cut sentences. Finish each point fully.\n\n"
        f"Question: {question}"
    )

    ans = generate_response(base_prompt, temperature=0.3, max_tokens=1024)

    #2) If it looks cut, contine form last line without repeating
    rounds = 0

    while rounds < max_rounds and looks_incomplete(ans):
        con_prompt = (
            "Continue EXACTLY from where you stopped."
            "Do not repeat earlier text."
            "Finish the incomplete point and complete the answer."
            f"Question: {question}\n\n"
            f"Answer so far: \n{ans}\n\n Continue:"
        )  

        more = generate_response(con_prompt, temperature=0.3, max_tokens=1024)

        if not more or more.strip() == "":
            break

        ans = (ans.rstrip() + "\n" + more.lstrip()).strip()
        rounds += 1

    return ans

def main():
    st.title("AI Teaching Assistant")
    st.write("Ask a question and get a clear, structured answer in numbered points.")

    user_input = st.text_area("Enter your question here:")

    if user_input:
        st.write(f"**Your Question:** {user_input}")
        response = complete_answer(user_input)
        st.write("**AI Response:**")
        st.markdown(response) # Markdown renders numbered points nicely

    else:
        st.info("Please enter a question to ask.")

if __name__ == "__main__":
    main()
