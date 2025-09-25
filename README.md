
# Pediatric Speech Analyzer 🗣️

A **Streamlit-based Python application** to record or upload a child's speech and analyze it for speech patterns, developmental assessment, and therapy recommendations.

---

## **Features**

1. **Record or Upload Speech Audio**  
   - Upload audio files in WAV, MP3, or FLAC format.

2. **Speech Pattern Analysis**  
   - Duration of speech  
   - Average pitch (Hz)  
   - Silence ratio (simplified metric)  
   - Clarity score (simplified metric)

3. **Developmental Assessment**  
   - Provides basic guidance on speech development: normal, slightly delayed, or requires attention.

4. **Therapy Recommendations**  
   - Suggests exercises or monitoring strategies based on speech clarity and duration.

5. **Audio Visualization**  
   - Displays waveform of the uploaded audio.

---

## **Requirements**

- Python 3.8+  
- Streamlit  
- numpy  
- librosa  
- matplotlib  
- pydub  

Install dependencies:

```bash
pip install streamlit numpy librosa matplotlib pydub
Setup Instructions
Clone the repository:

bash
Copy code
git clone <repository-url>
cd pediatric-speech-analyzer
Create a virtual environment (recommended):

bash
Copy code
python -m venv venv
Activate the virtual environment:

Windows

bash
Copy code
venv\Scripts\activate
Linux / Mac

bash
Copy code
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Running the App
Ensure your virtual environment is active.

Run the Streamlit app:

bash
Copy code
streamlit run app.py
Open the URL displayed in the terminal (usually http://localhost:8501).

Upload a child's speech audio file (WAV/MP3/FLAC).

View speech pattern analysis, development assessment, therapy recommendations, and audio waveform.

Sample Input
Audio File: child_speech.wav

Transcript Example:

pgsql
Copy code
Hello, my name is Emma. I like to play with my toys. I can count to five: one, two, three, four, five.
Expected Output
Audio Waveform

Visual plot of the uploaded speech audio.

Speech Pattern Analysis

yaml
Copy code
Duration (s): 8.12
Average Pitch (Hz): 215.5
Silence Ratio: 0.07
Clarity Score: 93
Developmental Assessment

pgsql
Copy code
Speech development is within normal range.
Therapy Recommendations

diff
Copy code
- Maintain current speech practice and activities.
Notes
