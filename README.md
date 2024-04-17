# Image Generation Application Documentation
Overview
This Python script provides a simple web application for generating images based on user-provided prompts and aspect ratios. It utilizes the Streamlit framework for the user interface and makes requests to the Limewire Image Generation API to create images.

## Prerequisites
Python 3.x
Streamlit library (pip install streamlit)
Requests library (pip install requests)
## Usage
Ensure that all prerequisites are installed.
Run the script using python script_name.py.
Access the application through the provided local URL.
Enter a prompt and select an aspect ratio.
Click the "Generate Image" button to create the image.
## Code Structure
generate_image(prompt, aspect_ratio): This function sends a POST request to the Limewire Image Generation API with the provided prompt and aspect ratio. It returns the generated image data if successful, or displays an error message otherwise.
main(): The main function of the script. It creates the Streamlit web application interface, including input fields for the prompt and aspect ratio, a button to trigger image generation, and the display of the generated image.
The Streamlit st library is used to create various UI components such as text inputs, select boxes, buttons, and display messages.
The time.sleep(5) line simulates processing time to give the impression of image generation.
## Input Parameters
API : Must use your own API Key
Prompt: Text input where users can enter a prompt that describes the desired image.
Aspect Ratio: Dropdown menu for users to select the aspect ratio of the generated image. Options include 1:1, 16:9, 4:3, and 3:2.
## Output
Generated Image: If the image generation is successful, the generated image will be displayed with the caption "Generated Image". If the generation fails, an error message will be shown.
## Error Handling
If there's an HTTP error during the API request (e.g., 404, 500), an error message will be displayed to the user.
If any other exception occurs during the process, an error message will be displayed.
## Limitations
The code currently only displays the first generated image if multiple images are returned by the API.
The time.sleep(5) line is used to simulate processing time and should be removed or adjusted for real-world usage.
Security
The Limewire API authorization token is hardcoded in the script. Ensure that proper security measures are taken to protect sensitive information.
## Troubleshooting
If the image generation fails, users can try again by entering a different prompt or aspect ratio.
## Contributors
This script was developed by Bunty Prasad Nayak.
