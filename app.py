import streamlit as st
import librosa
import numpy as np
import matplotlib.pyplot as plt
from tempfile import NamedTemporaryFile
from pydub import AudioSegment

# ----------------- Helper Functions -----------------

def analyze_speech_patterns(audio_path):
    """
    Analyze basic speech patterns:
    - Duration, pitch, clarity (simplified for demo)
    """
    y, sr = librosa.load(audio_path, sr=None)
    duration = librosa.get_duration(y=y, sr=sr)
    pitch = np.mean(librosa.yin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7')))
    pauses = np.sum(np.abs(y) < 0.01)/len(y)  # simplified silence ratio
    clarity_score = max(0, min(100, 100 - pauses*100))  # dummy score
    return {
        "Duration (s)": round(duration,2),
        "Average Pitch (Hz)": round(pitch,2),
        "Silence Ratio": round(pauses,2),
        "Clarity Score": round(clarity_score,2)
    }

def developmental_assessment(clarity_score, duration):
    """
    Provide basic development assessment based on clarity and speech duration
    """
    if clarity_score > 85 and duration > 2:
        return "Speech development is within normal range."
    elif clarity_score > 60:
        return "Speech development is slightly delayed. Monitoring recommended."
    else:
        return "Speech development may require attention. Consider evaluation by a speech therapist."

def therapy_recommendations(clarity_score):
    """
    Provide simple therapy recommendations
    """
    recommendations = []
    if clarity_score < 70:
        recommendations.append("Practice articulation exercises daily.")
        recommendations.append("Use simple words and repetition to improve clarity.")
    else:
        recommendations.append("Maintain current speech practice and activities.")
    return recommendations

def plot_audio_waveform(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    plt.figure(figsize=(8,2))
    plt.plot(y)
    plt.title("Audio Waveform")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    st.pyplot(plt)

# ----------------- Streamlit App -----------------

st.set_page_config(page_title="Pediatric Speech Analyzer", layout="wide")
st.title("🗣️ Pediatric Speech Analyzer")

st.markdown("Record or upload a child's speech to analyze speech patterns, assess development, and receive therapy recommendations.")

# Upload or record audio
uploaded_file = st.file_uploader("Upload speech audio (WAV/MP3/FLAC)", type=["wav","mp3","flac"])

if uploaded_file:
    # Save temporary file
    with NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getbuffer())
        audio_path = tmp_file.name
    
    st.success("Audio uploaded successfully!")

    # Display audio player
    st.audio(audio_path)

    # Plot waveform
    st.subheader("📊 Audio Waveform")
    plot_audio_waveform(audio_path)

    # Speech pattern analysis
    st.subheader("🗂 Speech Pattern Analysis")
    analysis = analyze_speech_patterns(audio_path)
    for key, value in analysis.items():
        st.write(f"{key}: {value}")

    # Developmental assessment
    st.subheader("📈 Developmental Assessment")
    assessment = developmental_assessment(analysis["Clarity Score"], analysis["Duration (s)"])
    st.write(assessment)

    # Therapy recommendations
    st.subheader("📝 Therapy Recommendations")
    recommendations = therapy_recommendations(analysis["Clarity Score"])
    for rec in recommendations:
        st.write("- " + rec)
