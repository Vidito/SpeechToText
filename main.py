import PySimpleGUI as sg
import speech_recognition as sr

sg.theme('DarkBlue14')  # Set the theme to a dark theme
sg.set_options(font=('Helvetica', 14))


# Create layout of the GUI
layout = [[sg.Text("Speech to Text")],
          [sg.Multiline(size=(70, 20), key="-OUTPUT-")],
          [sg.Button("Record", button_color=('white', 'gray'), border_width=10),
           sg.Button("Exit", button_color=('white', 'red'), border_width=10)]]

# Create the window
window = sg.Window("Speech to Text", layout)



# Loop for events
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "Record":
        # Initialize recognizer
        r = sr.Recognizer()

        # Record audio
        with sr.Microphone() as source:
            audio = r.listen(source)

        # Recognize speech using Google Speech Recognition
        try:
            text = r.recognize_google(audio)
            window["-OUTPUT-"].update(text)
        except sr.UnknownValueError:
            window["-OUTPUT-"].update("Could not understand audio")
        except sr.RequestError as e:
            window["-OUTPUT-"].update(f"Error: {e}")

window.close()

