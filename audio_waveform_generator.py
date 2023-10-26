import tkinter as tk
from tkinter import filedialog, messagebox
from pydub import AudioSegment
import matplotlib.pyplot as plt
from datetime import datetime
from io import StringIO
import sys
import threading
import time

# Redirect sys.stdout to a StringIO object for displaying in GUI
output_buffer = StringIO()
sys.stdout = output_buffer

def get_audio_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3;*.ogg;*.flac")])
    return file_path

def plot_waveform(audio_file, output_image):
    audio = AudioSegment.from_file(audio_file)

    samples = audio.get_array_of_samples()

    duration = len(samples) / audio.frame_rate
    sample_rate = audio.frame_rate

    time = [i / sample_rate for i in range(len(samples))]

    plt.figure(figsize=(10, 4))
    plt.plot(time, samples, color='b')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Audio Waveform')
    plt.savefig(output_image, bbox_inches='tight', pad_inches=0, dpi=300)
    plt.close()

def process_audio():
    start_time = time.time()
    
    input_audio_file = get_audio_path()
    if input_audio_file:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_image_file = f'waveform_{timestamp}.png'
        
        def processing_thread():
            print(f"[!] Processing '{input_audio_file}', please wait...")
            plot_waveform(input_audio_file, output_image_file)
            end_time = time.time()
            conversion_time = end_time - start_time
            print(f"[!] Waveform image saved as {output_image_file}")
            print(f"[!] Conversion took {conversion_time:.2f} seconds")
            print("="*69)

        processing_thread = threading.Thread(target=processing_thread)
        processing_thread.start()

        def update_console():
            while processing_thread.is_alive():
                console_text.config(state=tk.NORMAL)
                console_text.delete(1.0, tk.END)
                console_text.insert(tk.END, output_buffer.getvalue())
                console_text.config(state=tk.DISABLED)
                time.sleep(0.1)
            console_text.config(state=tk.NORMAL)
            console_text.delete(1.0, tk.END)
            console_text.insert(tk.END, output_buffer.getvalue())
            console_text.config(state=tk.DISABLED)

        update_thread = threading.Thread(target=update_console)
        update_thread.start()

def save_output():
    output_text = console_text.get("1.0", tk.END)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_name = f'conversionlog_{timestamp}.txt'
    with open(file_name, 'w') as file:
        file.write(output_text)
    messagebox.showinfo("Save Output", f"Output saved to {file_name}")

def about():
    about_window = tk.Toplevel(root)
    about_window.title("About")
    about_window.geometry("300x150")

    info_label = tk.Label(about_window, text="App: Waveform generation from audio files\nApp Version: 1.0.5 fr\nAuthor: Lucian")
    info_label.pack(pady=20)

# Create the main window
root = tk.Tk()
root.title("Audio Waveform Generator")
root.geometry("600x400")  # Set the size of the window
root.resizable(False, False)  # Make the window non-resizable

# Create a menu bar
menubar = tk.Menu(root)

# Create a File menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Save Output", command=save_output)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

# Create an About menu
about_menu = tk.Menu(menubar, tearoff=0)
about_menu.add_command(label="About", command=about)
menubar.add_cascade(label="About", menu=about_menu)

# Add the menu bar to the main window
root.config(menu=menubar)

# Add a button to trigger the process
process_button = tk.Button(root, text="Process Audio", command=process_audio)
process_button.pack(pady=20)

# Add a Text widget to display console output
console_text = tk.Text(root, wrap=tk.WORD, height=10, width=60)
console_text.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
console_text.config(state=tk.DISABLED)

# Run the GUI application
root.mainloop()
