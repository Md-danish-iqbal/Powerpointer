# PowerPoint Generator using python-pptx and Gemini-pro
This PowerPoint generator creates eye-catching and informative slides using Python-PPTX and Gemini-Pro. 
MARP is not used by PowerPoint. The PowerPoints are created directly, allowing for easy editing and completion within PowerPoint. 
It has picture placeholders as well!

To change the design of the PowerPoint, Use the Theme dropdown.


## Warning: The code for this tool may require modifications or optimization to meet specific needs.

The PowerPoint generator comes with a Streamlit web UI, which will be used to generate the PowerPoint presentation. With this tool, 
you can easily create stunning and informative presentations in no time.

You need a Gemini API Key.It's Free. These will likely be more than enough for you.

# How it works:
- The user sends a Topic and selects a Theme for prompt.
- The UI interface will receive the prompt and send it to the Gemini-pro model.
- The Gemini-pro model generates content based on the prompt.
- The Python-pptx library converts the generated content into a PowerPoint presentation and then sends it back to the UI interface.
- This tool is perfect for anyone who wants to quickly create professional-looking PowerPoint presentations without spending hours on design and content creation.

To use this, clone the repository and install the following packages: (It should do it automatically when running the bat file)
```
pip install flask python-pptx flask_limiter google.generativeai regex collection
```
After this, place your Gemini-pro API Key inside .env

Finally, start the flask webserver by running "start_app.bat"

Please report any issues and feel free to fix my code!

Made by Md Danish Iqbal (syncwithdanish@gmail.com)

