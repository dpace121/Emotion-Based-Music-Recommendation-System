from django.http import JsonResponse
from rest_framework.decorators import api_view
import base64
from PIL import Image
import io
import tensorflow as tf
import numpy as np
import os

# Build the absolute path to your model file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'music_app', 'models', 'emotion_model.h5')

# Load the model
model = tf.keras.models.load_model(model_path)

# A list of possible emotions that the model can predict
EMOTIONS = ['angry', 'happy', 'sad', 'neutral']

@api_view(['POST'])
def detect_emotion(request):
    try:
        # Get the base64 string from the request body
        image_data = request.data.get('image')

        # Optional: Remove the "data:image/jpeg;base64," prefix if present
        if ',' in image_data:
            image_data = image_data.split(',')[1]

        # Decode the base64 string to bytes
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes))

        # Preprocess the image to the format required by the model
        image = image.convert('RGB')  # Ensure the image is in RGB format
        image = image.resize((48, 48))  # Resize to the input shape expected by the model (adjust accordingly)
        image_array = np.array(image)  # Convert image to numpy array
        image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
        image_array = image_array / 255.0  # Normalize the image data

        # Predict the emotion using the model
        prediction = model.predict(image_array)

        # Get the emotion with the highest probability
        emotion_index = np.argmax(prediction)
        emotion = EMOTIONS[emotion_index]

        return JsonResponse({"emotion": emotion}, status=200)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
