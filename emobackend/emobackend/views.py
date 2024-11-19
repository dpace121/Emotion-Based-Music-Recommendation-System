from django.http import JsonResponse
from .views import model

def predict_emotion(request):
    # Assume you have input data (e.g., extracted from request)
    input_data = ...  # Preprocess your input data as needed

    # Use the loaded model to make a prediction
    predictions = model.predict(input_data)

    # Return a response (e.g., predicted emotion)
    predicted_emotion = predictions.argmax()  # Example of getting class with the highest score
    return JsonResponse({'predicted_emotion': int(predicted_emotion)})
