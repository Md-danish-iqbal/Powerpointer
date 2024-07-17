import streamlit as st
from io import BytesIO
import time
import os
from custome_function_main import get_bot_response


def generate_ppt(topic: str, theme: str) -> tuple:
    """
    Function to generate the PowerPoint presentation based on the selected topic and theme.

    Parameters:
    topic (str): The topic for the PowerPoint presentation.
    theme (str): The selected theme for the PowerPoint presentation.

    Returns:
    tuple: A tuple containing the PPT file path and the PPT file name.
    """
    # Design mapping based on theme selection
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

    # Log the selected topic and design
    print(topic, design[theme])

    # Generate the bot response based on topic and design
    ppt_path, ppt_name = get_bot_response(topic, design[theme])

    # Return the PPT file path and name
    return ppt_path, ppt_name


def main() -> None:
    """
    Main function to create the Streamlit UI for AI-Enhanced Presentation Maker.
    """

    # Set the title of the Streamlit app
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
            st.warning(f"Wait !!! Slides for PPT are being generated")

            # Simulate PPT slides generation progress
            progress_bar = st.progress(0)
            st.text('Generating PPT Slides...')
            for percent_complete in range(100):
                time.sleep(0.10)
                progress_bar.progress(percent_complete)

            # Create the PPT
            ppt_path, ppt_name = generate_ppt(topic, theme)
            st.success(f"PPT Slides for '{topic}' created successfully!")

            # Read the PPT file as bytes
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
