# Quick Voice bot demo

This is a alpha demo showing a bot that uses Text-To-Speech, Speech-To-Text, and a language model to have a conversation with a user.

This demo is set up to use [Deepgram](www.deepgram.com) for the audio service and [Groq](https://groq.com/) the LLM.

This demo utilizes streaming for sst and tts to speed things up.

Video tutorial coming soon

The files in `building_blocks` are the isolated components if you'd like to inspect them

```
python3 QuickAgent.py

```

# Language Model Processor with Streamlit Frontend

This project includes a language model processor that uses Groq and OpenAI for language processing, Deepgram for transcription, and Streamlit for the frontend interface.

## Setup

Before running the application, you need to install the necessary dependencies.

### Prerequisites

- Python 3.8+
- `portaudio19-dev` for audio processing

### Install Dependencies

Run the following script to install the required system dependencies:

```sh
./setup.sh
