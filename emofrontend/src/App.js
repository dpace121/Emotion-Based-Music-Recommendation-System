import React, { useState } from 'react';
import WebcamCapture from './components/WebcamCapture';
import Header from './components/Header';
import Footer from './components/Footer';
// import axios from 'axios';
import './App.css';

const App = () => {
    const [emotion, setEmotion] = useState('');

    const handleEmotionDetected = (detectedEmotion) => {
        setEmotion(detectedEmotion);
        // Redirect to YouTube Music based on detected emotion
        redirectToYouTube(detectedEmotion);
    };

    const redirectToYouTube = (emotion) => {
        const musicLinks = {
            happy: 'https://music.youtube.com/playlist?list=PLD8B3F6D34A67E70D',
            sad: 'https://music.youtube.com/playlist?list=PLpQG8-s7Q_pC0CynvTf3yIOovGuOeeYFg',
            angry: 'https://music.youtube.com/playlist?list=PLMyTuHLbV6MHO64cEKk4avkqF7lZC7CqC',
            neutral: 'https://music.youtube.com/playlist?list=PLs3AQj5xA7Tz5HmlhftYyS1F4BflLPJ8A',
        };

        if (musicLinks[emotion]) {
            window.open(musicLinks[emotion], '_blank');
        }
    };

    return (
        <div className="App">
            <Header />
            <main>
                <h1>Emotion Based Music Recommendation</h1>
                <h3>Let's try to detect your emotion:</h3>
                <WebcamCapture onEmotionDetected={handleEmotionDetected} />
            </main>
            <p>Current Detected Emotion: {emotion}</p>
            <Footer />
        </div>
    );
};


export default App;
