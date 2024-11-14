from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import io

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files['audio']
    language = request.form.get('language', 'en-US')  # Default to English

    recognizer = sr.Recognizer()

    # Read audio file using BytesIO to avoid file handling errors
    audio_data = io.BytesIO(audio_file.read())
    with sr.AudioFile(audio_data) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language=language)
        return jsonify({"text": text}), 200
    except sr.UnknownValueError:
        return jsonify({"error": "Could not understand the audio"}), 400
    except sr.RequestError as e:
        return jsonify({"error": f"Could not request results; {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
