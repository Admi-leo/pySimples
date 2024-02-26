import tkinter as tk
from tkinter import filedialog
import moviepy.editor as mp

def convert_video_to_audio():
    try:
        video_file_path = filedialog.askopenfilename()
        if not video_file_path:
            return  # Если пользователь не выбрал файл, выходим из функции

        audio_file_path = filedialog.asksaveasfilename(defaultextension=".mp3")
        if not audio_file_path:
            return  # Если пользователь не указал путь для сохранения, выходим из функции

        clip = mp.VideoFileClip(video_file_path)
        clip.audio.write_audiofile(audio_file_path)

        status_label.config(text="Конвертация завершена!")
    except Exception as e:
        status_label.config(text="Произошла ошибка при конвертации: " + str(e))

# Создание главного окна
root = tk.Tk()
root.title("Конвертер видео в аудио")

# Создание кнопки для запуска конвертации
convert_button = tk.Button(root, text="Выбрать файл и конвертировать", command=convert_video_to_audio)
convert_button.pack(pady=20)

# Метка для отображения статуса
status_label = tk.Label(root, text="", fg="red")
status_label.pack()

# Запуск главного цикла обработки событий
root.mainloop()
