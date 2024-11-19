import React, { useRef, useState } from 'react';
import Webcam from 'react-webcam';

const WebcamCapture = () => {
  const webcamRef = useRef(null);
  const [imageData, setImageData] = useState(null);

  // Function to capture the image from the webcam
  const captureImage = () => {
    if (webcamRef.current) {
      const capturedImage = webcamRef.current.getScreenshot();
      setImageData(capturedImage); // Save the base64 string
      sendImageToBackend(capturedImage); // Call the function to send data
    }
  };

  // Function to send the captured image to the Django backend
  const sendImageToBackend = async (base64Image) => {
    try {
      const response = await fetch('http://localhost:8000/detect-emotion/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ image: base64Image }), // Sending the image data
      });

      const data = await response.json();
      console.log('Response from backend:', data);
    } catch (error) {
      console.error('Error sending image to backend:', error);
    }
  };

  return (
    <div>
      <Webcam
        audio={false}
        ref={webcamRef}
        screenshotFormat="image/jpeg"
        width={320}
        height={240}
      />
      <button onClick={captureImage}>Capture Photo</button>
    </div>
   
  );
};

export default WebcamCapture;
