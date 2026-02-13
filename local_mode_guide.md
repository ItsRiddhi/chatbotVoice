# Local/Free Mode Guide

Since Google Cloud Services require a billing account (credit card), we are switching to a **Local/Free Mode**.

## How it Works
1.  **Speech-to-Text**: We use your **Browser's built-in** speech recognition (Web Speech API). It's free and works great in Chrome/Edge.
2.  **Text-to-Speech**: We use your **Browser's built-in** voices.
3.  **Logic**: The Python backend (`app.py`) will just handle the logic (medication checks, safety protocols) without calling paid APIs.

## Advantages
- **Free**: $0 cost.
- **Easy**: No setup in Google Cloud Console.
- **Private**: Audio stays in your browser; only text is sent to the local backend.
