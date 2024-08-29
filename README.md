# SpeakToScript.io

A simple web application for converting audio files to text using speech recognition. Built with Flask (Python) for the backend, and HTML/CSS for the frontend.

## Features

- Upload audio files for conversion.
- Select the language for speech recognition.
- Convert speech to text with real-time feedback.
- Loading animation during the conversion process.

## Technologies Used

- **Python**: For the backend server and speech recognition.
- **Flask**: Web framework for building the server.
- **HTML**: Structure of the web application.
- **CSS**: Styling and aesthetics of the web application.
- **JavaScript**: Handling file uploads and form submission.

## Installation

### Prerequisites

- Python 3.x
- Flask
- SpeechRecognition library
- Other Python dependencies (see `requirements.txt`)

### Steps to Run Locally

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/speech-to-text-converter.git
    cd speech-to-text-converter
    ```

2. **Install the required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask application**:
    ```bash
    python app.py
    ```

4. **Open your browser** and go to `http://127.0.0.1:5000/` to use the application.

## Project Structure

- **app.py**: Main Python file that runs the Flask server and handles the conversion logic.
- **static/styles.css**: CSS file for styling the web page.
- **templates/index.html**: HTML file that contains the structure of the web page.

## Usage

1. **Upload an audio file** by dragging and dropping it into the upload area or by clicking to select a file.
2. **Select the language** for speech recognition from the dropdown menu.
3. **Click the "Convert" button** to start the conversion process.
4. **Wait for the conversion**: A loading spinner will appear during the process. The resulting text will be displayed once the conversion is complete.

## Loading Animation

A loading spinner is displayed during the conversion process to indicate that the application is working on the task.

## Contributing

Feel free to submit issues and pull requests if you find bugs or want to add new features. Please follow the contribution guidelines outlined in the `CONTRIBUTING.md` file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or comments, you can reach me at siddiqueearhaan@gmail.com
