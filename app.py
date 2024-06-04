from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if 'frame' not in request.files:
        return jsonify({'error': 'No frame part in the request'}), 400

    frame = request.files['frame'].read()
    image = Image.open(io.BytesIO(frame))

    # Here you would add your model prediction code
    # For the sake of example, let's return a dummy prediction
    prediction = {'label': 'example', 'confidence': 0.99}

    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True)
