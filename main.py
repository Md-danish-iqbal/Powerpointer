import streamlit as st
from pptx import Presentation
from io import BytesIO
import time,os
from custome_function_main import get_bot_response


# Function to generate the PowerPoint presentation


def generate_ppt(topic, theme):
    design = {
        "Theme A": "Design-1",
        "Theme B": "Design-2",
        "Theme C": "Design-3",
        "Theme D": "Design-4",
        "Theme E": "Design-5",
        "Theme F": "Design-6",
        "Theme G": "Design-7",
        "Custom Theme 1": "Design-8",
        "Custom Theme 2": "Design-9",
    }

    print(topic, design[theme])

    ppt_path, ppt_name = get_bot_response(topic, design[theme])
    return ppt_path, ppt_name



# Streamlit UI
def main():
    page_bg_img = '''
    <style>
    body {
    background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
    background-size: cover;
    }
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.title("AI-Enhanced Presentation Maker by Gemini")

    # Input for topic
    topic = st.text_input("Enter your topic:")

    # Dropdown for theme selection
    themes = ["Theme A", "Theme B", "Theme C",
              "Theme D", "Theme E", "Theme F",
              "Theme G", "Custom Theme 1", "Custom Theme 2"]
    theme = st.selectbox("Select a theme:", themes)

    # Button to trigger PPT creation
    if st.button("Create"):
        if topic:
            # Initialize the progress bar
            progress_bar = st.progress(0)
            st.text('Initializing...')

            # Simulate prompt generation progress
            st.text('Generating Prompt...')
            for percent_complete in range(100):
                time.sleep(0.10)
                progress_bar.progress(percent_complete)
            st.success(f"Prompt for '{topic}' generated successfully!")
            st.warning(f"Wait !!!  Slides for PPT is generating Initialized ")

            # Simulate PPT slides generation progress
            progress_bar = st.progress(0)
            st.text('Generating PPT Slides...')
            for percent_complete in range(100):
                time.sleep(0.10)
                progress_bar.progress(percent_complete)

            # Create the PPT
            ppt_path, ppt_name = generate_ppt(topic, theme)
            st.success(f"PPT Slides for '{topic}' created successfully!")

            with open(ppt_path, "rb") as f:
                ppt_bytes = f.read()

                # Download link for the PPT file
            st.download_button(
                label=f"Download {os.path.basename(ppt_path)}",
                data=ppt_bytes,
                file_name=os.path.basename(ppt_path),
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            )

if __name__ == "__main__":
    main()
