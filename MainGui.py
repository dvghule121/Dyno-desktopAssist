import os
import random
import threading
from tkinter import *
import pygame
import pyttsx3
import speech_recognition as sr
from dynoFunctions import MainFunctions as Df
from WordProcessor import Dyno_response as Dr


class Gui(Tk):
    label_ans: None
    label_quest: None

    def __init__(self):
        super().__init__()
        # Windows Design
        self.i = 1

        self.geometry('305x325')
        self.resizable(False, False)
        self.title("Dyno-desktop assist")

        # extra variable for text and label image is used as background

        self.bg1 = PhotoImage(file="Data/Your_image.png")
        self.user_input_text = StringVar()
        self.ans_out_text = StringVar()
        self.quest_out_text = StringVar()

        # frames entry label and buttons

        self.frame = Label(self, image=self.bg1)
        self.frame.place(x=-64, y=-80)

        self.user_input = Entry(self, textvariable=self.user_input_text, width='20', font=('bold', 15),
                                bg='white', fg='blue')
        self.user_input.place(x=40, y=200)

        self.submit = Button(self, text='Submit', width="10", bd=0, bg='#15f800', fg='black',
                             command=GuiFunctions.threading_submit_)
        self.submit.place(x=60, y=250)

        self.expand = Button(text='|Down|', width="10", bd=0.5, bg='#014da1', fg='white',
                             command=Gui.expand)
        self.expand.place(x=0, y=300)

        self.voice_recogn_btn = Button(self, text='Voice Rec', width="10", bg='#fff500', bd=0,
                                       command=GuiFunctions.threading_voice)
        self.voice_recogn_btn.place(x=160, y=250)
        # bg = '#FF69B4'

        txt_frame = Frame(self).place(x=0, y=300)

        # text area where conversation will be shown

        self.ans_area = Text(txt_frame, width='44', height=15, font=('lucid', 10), bg="#014da1", state=DISABLED)
        self.ans_area.place(x=0, y=325)

        # status bar at bottom

        status_bar = Label(self.ans_area, width=57, text=' Dyno is running.....', bg='royalblue', fg='white',
                           justify="center")
        status_bar.place(x=0, y=250)
        self.bind('<Return>', GuiFunctions.threading_submit)
        self.user_input.focus()
        # --------------------------- Extra Content--------------------------------------------------------------------

        # self.ans_area.configure(state=DISABLED)
        # self.scroll = Scrollbar(txt_frame, command=self.ans_area.yview)
        # self.scroll.pack(side="right", pady=(350, 0), fill='y')

    def create_label(self, quest, ans):
        # the conversation will be shown in label

        self.label_ans = Label(self.ans_area, textvariable=self.ans_out_text, font=('lucid', 10), wraplength=200) \
            .place(x=80, y=75)
        self.label_quest = Label(self.ans_area, textvariable=self.quest_out_text, font=('lucid', 10), wraplength=300) \
            .place(x=20, y=20)
        # these variable be set as question and answer

        self.quest_out_text.set(quest)
        self.ans_out_text.set(ans)
        self.user_input_text.set('')

    @staticmethod
    def expand():
        if window.i % 2 != 0:
            window.geometry('305x550')
            window.i = window.i + 1
        else:
            window.geometry('305x325')
            window.i = window.i + 1


class GuiFunctions:

    def __init__(self):
        pass

    @staticmethod
    def threading_submit(event="<return>"):
        t1 = threading.Thread(target=cmd.response)
        t1.daemon = True  # if this value is not set thread will continue to run even after closing app
        t1.start()

    @staticmethod
    def threading_submit_():
        cmd.threading_submit()

    @staticmethod
    def threading_voice():
        t1 = threading.Thread(target=cmd.star_detecting_speech)
        t1.daemon = True
        t1.start()

        # window.submit.config(state=DISABLED)

    @staticmethod
    def get_audio():
        r = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print('listening, Please give command')
            audio = r.listen(source, phrase_time_limit=5)
            print('...', end=' ')
            speech = ''

            try:
                speech = r.recognize_google(audio)

            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print('no network')

        return speech

    @staticmethod
    def speak(audio):
        try:

            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            engine.setProperty('rate', 145)

            # print(voices[1].id)
            engine.setProperty('voice', voices[0].id)

            engine.say(audio)
            engine.runAndWait()
        except RuntimeError:
            window.user_input_text.set('please wait i am speaking')

    @staticmethod
    def star_detecting_speech():
        wake_word = 'start'
        i = 0
        while i < 15:
            word = cmd.get_audio()
            print(word)

            if wake_word in word or "guru" in word:
                if i != 0:
                    i = i - 1
                else:
                    i = -1

                cmd.rec_voice()

            elif 'exit' in word or 'stop' in word:
                cmd.speak('yes boss i am quiting but you can use me by text assist mode')
                break

            else:
                pass
            i = i + 1
            print(i)
        print('successfully exited')

    @staticmethod
    def rec_voice():
        """
        rec voice uses google speech recognition to recognise user speech and converts it to text.
        """

        r = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            # # r.adjust_for_ambient_noise(mic)
            # r.pause_threshold = 0.7
            # r.energy_threshold = 750
            # r.dynamic_energy_threshold = False
            # for playing wav file
            print('listening, Please give command')
            cmd.speak('listening, Please give command')
            pygame.init()

            pygame.mixer.init()
            my_sound = pygame.mixer.Sound('Data/beep-08b.wav')
            my_sound.play()

            while pygame.mixer.get_busy():
                pygame.time.delay(10)
                pygame.event.poll()

            audio = r.listen(source, phrase_time_limit=10)

        try:

            cmd.speak('recognising.')
            print('recognising.')
            speech = r.recognize_google(audio).lower()
            print(speech)

        except sr.UnknownValueError:
            speech = ''
        except sr.RequestError:
            speech = 'check your internet and retry'

        window.user_input_text.set(speech)
        print(speech)
        cmd.response()

    @staticmethod
    def insert_ans(quest, statement):
        user = "You"
        dyno = 'Dyno'
        window.ans_area.configure(state=NORMAL)

        window.create_label(f'{user}: {quest}', f'{dyno}: {statement}')

        window.ans_area.configure(state=DISABLED)

    @staticmethod
    def greeting(final_word):
        print(final_word)
        return 'i am fine, thank you for your kind response.'

    @staticmethod
    def get_entry_text():
        choice = window.user_input_text.get()
        return choice

    @staticmethod
    def play_song(song_name):
        print(song_name)
        music_dir = "C:\\Users\\sv330\\Music\\"
        dir_list = os.listdir(music_dir)
        songs = []

        if song_name != '':
            for i, items in enumerate(dir_list):
                if '.mp3' in items:
                    item = items.lower()
                    songs.insert(i, item)

            for i, item_p in enumerate(songs):
                if song_name in item_p:
                    os.startfile(os.path.join(music_dir + songs[i]))

                    song = songs[i]
                    ans = f'yes sir playing {song}'
                    break
            else:
                print('song is not available')
                cmd.speak('song is not available')
                ans = 'song is not available'

        else:
            index = random.randint(0, 4)
            os.startfile(os.path.join(music_dir + dir_list[index]))
            ans = 'Playing random songs'

        return ans

    @staticmethod
    def to_do(choice):

        if choice == 'clear':
            with open('Data/todo_list.txt', 'w') as f:
                f.write('')
                f.close()
            data = 'list is formatted successfully sir '

        elif choice != 'quite':
            with open('Data/todo_list.txt', 'a') as f:
                f.write(choice + '\n')
                f.close()
                data = 'item added to todo list successfully '

        else:
            with open('Data/todo_list.txt', 'r') as f:
                data = f.read()

        return data

    @staticmethod
    def response():
        mapping = {
            "greeting": cmd.greeting,
            "p_song": Df.play_song,
            "time": Df.tell_time,
            "close": Df.close_app,
            "open_app": Df.open_app,
            "open_file": Df.open_file,
            "p_movie": Df.play_movies,
            "weather": Df.tell_weather,
            "todo": cmd.to_do,
            "search": Df.search,
            "math": Df.calc,
            "voice_rec": cmd.threading_voice,
            "opnsite": Df.open_site,
            "location": Df.find_direction
        }

        choice = cmd.get_entry_text()
        tag = Dr.predict_tag(choice)
        final_words = Dr.clean_sentence(choice, tag)
        if tag in mapping.keys():
            try:
                ans = mapping[tag](final_words)
                cmd.insert_ans(choice, ans)
                cmd.speak(ans)
            except LookupError:
                print('sorry this error occurred \n')
        else:
            response = Dr.give_response(tag)
            cmd.insert_ans(choice, response)
            cmd.speak(response)


class DynoSubFunction:
    def __init__(self):
        pass

    @staticmethod
    def change_button_to(func, text):
        window.submit.configure(text=text, command=func)


window = Gui()
cmd = GuiFunctions()
window.mainloop()
