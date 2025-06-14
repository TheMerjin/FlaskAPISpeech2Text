from flask import Flask, request, jsonify
from vosk import Model, KaldiRecognizer
import wave
import json
import os

app = Flask(__name__)
model = Model(r"/model/vosk-model-small-en-us-0.15")  # path to vosk model directory


@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "file" not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400

    audio_file = request.files["file"]
    audio_path = "temp.wav"
    audio_file.save(audio_path)

    wf = wave.open(audio_path, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())

    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            results.append(json.loads(rec.Result()))
    results.append(json.loads(rec.FinalResult()))

    os.remove(audio_path)
    text = " ".join(r.get("text", "") for r in results)
    return jsonify({"transcription": text})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
