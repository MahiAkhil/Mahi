import streamlit as st
import pandas as pd
import openai

openai.api_key = "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"

st.title("CSV Data Analyzing App")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")
    st.write(df)

    question = st.text_input("Ask a question:")

    if st.button("Get Answer"):
        if question:
            text = " ".join(df.astype(str).values.flatten())

            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=f"Answer the following question:\n\n{question}\n\nData:\n{text[:4000]}",
                max_tokens=150,
            )

            answer = response.choices[0].text.strip()

            st.subheader("Answer:")
            max_display_length = 1000
            for i in range(0, len(answer), max_display_length):
                st.write(answer[i:i + max_display_length])

        else:
            st.warning("Please enter a question.")
