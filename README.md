# Text to Speech Application

A simple desktop application that converts text to speech using Python. The application provides a graphical user interface where users can input or paste text and convert it to audio speech.

## Features

- Text to speech conversion
- Copy and paste functionality
- Play/Stop speech control
- Clean and intuitive user interface
- Centered window display

## Prerequisites

Before running this application, make sure you have the following packages installed:

```bash
pip install gTTS
pip install pygame
pip install pyperclip
```

## Installation

1. Clone this repository
2. Install the required dependencies
3. Run the application:
```bash
python main.py
```

## Usage

1. Launch the application
2. Enter text in the text area by:
   - Typing directly
   - Using the "Paste" button to paste clipboard content
3. Click "Submit" to convert and play the text as speech
4. Use "Stop Speech" to stop the current playback
5. Click "Clear" to clear the text area

## Controls

- **Submit**: Converts text to speech and plays it
- **Clear**: Clears all text from the text area
- **Stop Speech**: Stops the current speech playback
- **Paste**: Pastes clipboard content into the text area

## Technical Details

- Uses `gTTS` (Google Text-to-Speech) for text-to-speech conversion
- `pygame.mixer` for audio playback
- Custom threading implementation for non-blocking audio playback
- Built with Tkinter for the graphical user interface

## Project Structure

```
gui-texttospeech
├── main.py # Main application file
├── Components/
│ └── Thread.py # Custom thread implementation
└── temp.mp3 # Temporary audio file (generated during runtime)
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request