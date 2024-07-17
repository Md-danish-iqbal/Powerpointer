def extract_contents_from_text(text):
    """
    Extracts slide contents from a text input where slides and contents are demarcated by specific markers.

    Args:
    text (str): The input text containing slide and content markers.

    Returns:
    list: A list of slides, where each slide is a list of its contents.
    """
    lines = text.strip().split('\n')  # Split the input text into lines
    slides = []  # Initialize a list to hold all slides
    current_slide = []  # Initialize a list to hold contents of the current slide
    current_content = ""  # Initialize a string to accumulate the current content
    recording_content = False  # Flag to indicate if we are recording content

    for line in lines:
        line = line.strip()  # Strip any leading/trailing whitespace from the line

        # Check if the line indicates the start of a new slide
        if line.startswith('#Slide:'):
            if current_slide:  # If there is an ongoing slide
                if recording_content:  # If we are in the middle of recording content
                    current_slide.append(current_content.strip())  # Add the recorded content to the current slide
                    recording_content = False  # Reset the recording flag
                slides.append(current_slide)  # Add the completed slide to the list of slides
            current_slide = []  # Reset for the new slide

        # Check if the line indicates the start of new content
        elif line.startswith('#Content:'):
            if recording_content:  # If we are in the middle of recording content
                current_slide.append(current_content.strip())  # Add the recorded content to the current slide
            current_content = ""  # Reset the content accumulator for the new content
            recording_content = True  # Set the recording flag

        # If we are currently recording content
        elif recording_content:
            # Check if the line indicates the start of a new slide
            if line.startswith('#Slide:'):
                recording_content = False  # Reset the recording flag
                current_slide.append(current_content.strip())  # Add the recorded content to the current slide
                current_content = ""  # Reset the content accumulator
                slides.append(current_slide)  # Add the completed slide to the list of slides
                current_slide = []  # Reset for the new slide
            else:
                current_content += line + '\n'  # Add the line to the current content accumulator

    if recording_content:  # If there is any remaining content after the loop
        current_slide.append(current_content.strip())  # Add it to the current slide

    if current_slide:  # If there is any remaining slide after the loop
        slides.append(current_slide)  # Add it to the list of slides

    return slides  # Return the list of slides


# text = ""
# with open(f'Cache/custom_prompt.txt', 'r', encoding='utf-8') as f:
#     text = f.read()
# # Extract the contents from the text
# slides = extract_contents_from_text(text)
#
# # Print the contents of each slide
# for idx, slide in enumerate(slides, 1):
#     print(f"Slide {idx} Contents:")
#     for content in slide:
#         print(content)
#     print("\n")
