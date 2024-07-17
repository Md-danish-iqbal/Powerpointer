def extract_contents_from_text(text: str) -> list[list[str]]:
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

        if line.startswith('#Slide:'):
            if current_slide:
                if recording_content:
                    current_slide.append(current_content.strip())
                slides.append(current_slide)
            current_slide = []
            current_content = ""
            recording_content = False

        elif line.startswith('#Content:'):
            if recording_content:
                current_slide.append(current_content.strip())
            current_content = ""
            recording_content = True

        elif recording_content:
            current_content += line + '\n'

    if recording_content:
        current_slide.append(current_content.strip())

    if current_slide:
        slides.append(current_slide)

    return slides

# Example usage:
# with open('Cache/custom_prompt.txt', 'r', encoding='utf-8') as f:
#     text = f.read()
# slides = extract_contents_from_text(text)
# for idx, slide in enumerate(slides, 1):
#     print(f"Slide {idx} Contents:")
#     for content in slide:
#         print(content)
#     print("\n")
