# Audio Waveform Generator

## Overview

This Python script is designed to generate an image of an audio waveform from various audio file formats. It utilizes libraries such as `pydub`, and `matplotlib` for audio processing and waveform visualization. The generated image can serve various purposes, such as visualizing audio content or preparing content for presentations.

## Features

- Supports multiple audio file formats including WAV, MP3, OGG, and FLAC.
- Provides a GUI (Graphical User Interface) for user-friendly interaction.
- Outputs the audio waveform as a high-resolution PNG image.
- Offers the option to save the console output to a text file for reference.

## Usage

### Prerequisites

- Python 3.x installed on your system.
- Required libraries can be installed using `pip`. Use the following command to install them:

```py
pip install pydub matplotlib tkinter
```

### Running the Script

1. Execute the script `audio_waveform_generator.py` or run the `Waveform Generator.exe`.
2. The GUI window will appear.
3. Click the "Select Audio File" button to choose an audio file.
4. The script will process the audio and generate a waveform image.
5. The console output will display the progress and completion messages.

### Menu Options

- **File Menu**:
* **Save Output**: Save the console output to a file named `conversionlog{date and time of file generation}.txt`.
- **Exit**: Close the application.

- **About Menu**:
- **About**: Displays information about the application, including version and author.

## Standalone Executable

You can convert the script into a standalone executable for easier distribution. Follow these steps:

1. Install [PyInstaller](https://www.pyinstaller.org/):

```py
pip install pyinstaller
```

2. Use the following command to create the executable:

```py
pyinstaller --onefile --hidden-import matplotlib --hidden-import pydub --hidden-import tkinter --hidden-import numpy --noconsole audio_waveform_generator.py
```

This will create a standalone executable in the `dist` directory.

## Notes

- Make sure to test the executable on a clean environment to ensure all necessary dependencies are included.
- If you encounter issues with packaging, consult the PyInstaller documentation or community forums for specific guidance.

## Author

- [ByteBendr](https://github.com/ByteBendr) 

## Version

- 1.0.5 fr (Final Release)

## License

This project is licensed under the [MIT License](LICENSE).
