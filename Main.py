import streamlit as st
from model import GeneralModel


def app():

    # Creating an object of prediction service
    pred = GeneralModel()

    api_key = st.sidebar.text_input("APIkey", type="password")
    # Using the streamlit cache
    # @st.cache
    def process_prompt(product_description, seed_words):

        return pred.model_prediction(
            product_description=product_description.strip(),
            seed_words=seed_words.strip(),
            api_key=api_key,
        )

    if api_key:

        # Setting up the Title
        st.title("Generate Product names using description and seed words")

        # st.write("---")

        product_description = st.text_input(
            "Description of the product",
            value="A pair of shoes that can fit any foot size.",
        )
        seed_words = st.text_input(
            "List of seed words", value="adaptable, fit, omni-fit."
        )

        if st.button("Submit"):
            with st.spinner(text="In progress"):
                report_text = process_prompt(product_description, seed_words)
                st.markdown(report_text)
    else:
        st.error("🔑 Please enter API Key")
