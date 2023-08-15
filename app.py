import streamlit as st
import torchaudio
from transformers import pipeline

# Load the Hugging Face model for ASR (Automatic Speech Recognition)
asr = pipeline("automatic-speech-recognition")

def main():
    st.title("Podcast Summarizer")

    uploaded_file = st.file_uploader("Upload a podcast audio file (M4A)", type=["m4a"])

    if uploaded_file is not None:
        st.audio(uploaded_file, format="audio/m4a")

        if st.button("Convert and Summarize"):
            podcast_text = audio_to_text(uploaded_file)
            st.subheader("Podcast Transcript:")
            st.text(podcast_text)

            # You can add your podcast summarization logic here
            summarized_text = summarize_podcast(podcast_text)
            st.subheader("Podcast Summary:")
            st.text(summarized_text)

def audio_to_text(uploaded_file):
    try:
        # Convert M4A to WAV and get ASR result
        audio_path = "temp.wav"
        with open(audio_path, "wb") as f:
            f.write(uploaded_file.read())

        # Load audio using torchaudio
        waveform, sample_rate = torchaudio.load(audio_path)
        
        # Convert waveform to a compatible format for ASR
        pcm_waveform = waveform.squeeze().numpy()

        # Transcribe audio using Hugging Face ASR
        asr_result = asr(pcm_waveform)
        transcript = " ".join(asr_result)

        return transcript
    except Exception as e:
        return f"Error: {e}"

def summarize_podcast(text):
    # Add your podcast summarization logic here
    return "This is a summarized version of the podcast transcript."

if __name__ == "__main__":
    main()
