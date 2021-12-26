import datetime
import os
import random
import webbrowser

import requests
import wikipedia
import wolframalpha


class MainFunctions:
    programmes = ['pycharm64.exe', 'zoom.exe', 'code.exe', 'teams.exe', 'vlc.exe', 'music.ui.exe', 'notepad.exe',
                  'chrome.exe', 'winword.exe']

    def __init__(self):
        pass

    @staticmethod
    def search_file(path, extension):
        path_file = dict()

        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(extension):
                    path_file[file.lower()] = root
        return path_file

    @staticmethod
    def open_app(choice):
        dir_path = "C:\\Users\\Dyno\\Documents\\Application\\"
        dir_list = os.listdir(dir_path)
        program = []
        ans = 'this program i am searching but seems to be not in list'

        for i, items in enumerate(dir_list):
            if '.lnk' in items:
                item = items.lower()
                program.insert(i, item)

        for i, item_p in enumerate(program):
            if choice in item_p:
                os.startfile(os.path.join(dir_path + program[i]))

                ans = 'i have opened app'

        return ans

    @staticmethod
    def play_movies(movie_name, dir_p="E:\\Movies\\"):

        dir_list = os.listdir(dir_p)
        movies = []
        ans = 'Movie is not available'

        choice = movie_name

        for i, items in enumerate(dir_list):
            if '.mp4' or '.mkv' or '.avi' in items:
                item = items.lower()
                movies.insert(i, item)

        for i, item_p in enumerate(movies):
            if choice in item_p:
                os.startfile(os.path.join(dir_p + movies[i]))
                print(f'boss playing {movies[i]} enjoy your day sir')
                ans = f'boss playing {movies[i]}. enjoy your day sir'
                break
        file_path = MainFunctions.search_file(dir_p, '.mkv')
        list_movies = list(file_path.keys())
        for file in list_movies:
            if movie_name in file:
                os.startfile(os.path.join(file_path[file] + '\\' + file))
                ans = f'boss playing {file}. enjoy your day sir'
                break

        return ans

    @staticmethod
    def close_app(choice):
        print('close', choice)
        try:
            for item in MainFunctions.programmes:
                if choice in item:
                    try:
                        os.system(f"TASKKILL /f /im {item}")
                        return f'Successfully terminated {item}'

                    except Exception as e:
                        return f'sir this error occured,{e}'

        except LookupError:
            return "sorry boss i don't have permission to terminate this app"

    @staticmethod
    def play_song(final_choice):
        music_dir = "C:\\Users\\sv330\\Music\\"
        dir_list = os.listdir(music_dir)
        ans = 'Movie is not available'

        if final_choice == "" or final_choice == 'songs':
            index = random.randint(0, 4)
            os.startfile(os.path.join(music_dir + dir_list[index]))
            ans = f'boss playing {final_choice}. enjoy your day sir'

        elif 'youtube' in final_choice:
            webbrowser.open('https://www.youtube.com/results?search_query=' + final_choice)
            ans = "playing on youtube"

        else:
            file_path = MainFunctions.search_file(music_dir, '.mp3')
            list_movies = list(file_path.keys())
            for file in list_movies:
                if final_choice in file:
                    os.startfile(os.path.join(file_path[file] + '\\' + file))
                    ans = f'boss playing {file}. enjoy your day sir'
                    break

        return ans

    @staticmethod
    def find_direction(choice, your_location='Kingaon,+Maharashtra+413523'):
        final_sentence = choice
        if len(choice) != 0:
            webbrowser.open('https://www.google.com/maps/dir/' + your_location + '/' + final_sentence)
            print("please wait boss i am searching for your choice")
            return "please wait boss i am searching for your choice"

        else:
            print(' error - none input')
            return "no input please check"

    @staticmethod
    def tell_time(choice):
        print(choice)
        str_time = datetime.datetime.now().strftime("%H:%M")
        ans = f"Sir, the time is {str_time}"
        return ans

    @staticmethod
    def tell_weather(o_choice):
        choice = 'latur'
        if len(o_choice) != 0:
            choice = o_choice
            print(choice)

        # Python program to find current
        # weather details of any city
        # using openweathermap api

        # Enter your API key here
        api_key = "a10fd8a212e47edf8d946f26fb4cdef8&q"

        # base_url variable to store url
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        # Give city name
        city_name = choice

        # complete_url variable to store
        # complete url address
        complete_url = base_url + "&q=" + city_name + "&units=metric&appid=" + api_key

        # get method of requests module
        # return response object
        response = requests.get(complete_url)
        # to confirm how it works
        # webbrowser.open(complete_url)

        # json method of response object
        # convert json format data into
        # python format data
        x = response.json()

        # Now x contains list of nested dictionaries
        # Check the value of "cod" key is equal to
        # "404", means city is found otherwise,
        # city is not found
        if x["cod"] != "404":
            print(x)

            # store the value of "main"
            # key in variable y
            y = x["main"]

            # store the value corresponding
            # to the "temp" key of y
            current_temperature = y["temp"]

            # store the value corresponding
            # to the "pressure" key of y
            description = x["wind"]['speed']

            # store the value corresponding
            # to the "humidity" key of y
            current_humidity = y["humidity"]

            # store the value of "weather"
            # key in variable z
            z = x["weather"]

            # store the value corresponding
            # to the "description" key at
            # the 0th index of z
            weather_description = z[0]["description"]

            # print following values
            return (" Temperature (in kelvin unit) = " +
                    str(current_temperature) +
                    "\n Wind speed = " +
                    str(description) +
                    "\n humidity (in percentage) = " +
                    str(current_humidity) +
                    "\n description = " +
                    str(weather_description))

        else:
            print(" City Not Found ")

    @staticmethod
    def search(choice):
        choice = choice.replace('search', '')
        if 'wikipedia' or 'who is' in choice:

            choice = choice.replace('wikipedia', '')
            choice = choice.replace('who is', '')
            choice = choice.replace('what is', '')
            choice = choice.replace('what is ', '')
            print(choice)
            try:
                data = wikipedia.summary(choice, sentences=3)

            except RuntimeError:
                webbrowser.open('https://www.google.com/search?q=' + choice)
                data = ''

        else:
            webbrowser.open('https://www.google.com/search?q=' + choice)
            data = ''

        return 'i have searched this on web for you hope this works.', data

    @staticmethod
    def to_do(choice):

        if choice != 'quite':
            with open('Data/todo_list.txt', 'a') as f:
                f.write(choice + '\n')
                f.close()
                data = 'item added to todo list successfully '

        else:
            with open('Data/todo_list.txt', 'r') as f:
                data = f.read()

        return data

    @staticmethod
    def open_file(file_name, dir_p="C:\\Users\\sv330\\Downloads\\"):

        dir_list = os.listdir(dir_p)
        movies = []
        ans = 'i have searched in directory but could not find specified file'

        choice = file_name

        for i, items in enumerate(dir_list):
            if '.jpj' or '.txt' or '.png' or '.pdf' in items:
                item = items.lower()
                movies.insert(i, item)

        for i, item_p in enumerate(movies):
            if choice in item_p:
                os.startfile(os.path.join(dir_p + movies[i]))
                ans = 'i have opened it.'
        return ans

    @staticmethod
    def crete_note(file_name, note_content):
        with open(file_name + '.txt', 'w') as f:
            f.write(note_content)
            f.close()
        return 'note successfully saved'

    @staticmethod
    def calc(choice):
        client = wolframalpha.Client('R2K75H-7ELALHR35X')
        try:
            res = client.query(choice)
            answer = next(res.results).text
        except StopIteration:
            answer = MainFunctions.search(choice)

        return answer

    @staticmethod
    def open_site(final_sentence):
        query = final_sentence
        if 'google' in query:
            webbrowser.open('https://www.' + 'google.com')
            ans = "yes i have opened this site"

        elif 'youtube' in query:
            webbrowser.open('https://www.' + 'youtube.com')
            ans = "yes i have opened this site"

        elif 'instagram' in query or 'insta' in query:
            webbrowser.open('https://www.' + 'instagram.com')
            ans = "yes i have opened this site"

        elif 'twitter' in query:
            webbrowser.open('https://www.' + 'twitter.com')
            ans = "yes i have opened this site"

        elif 'facebook' in query or 'fb' in query:
            webbrowser.open('https://www.' + 'facebook.com')
            ans = "yes i have opened this site"

        elif 'drive' in query or 'drive' in query:
            webbrowser.open('https://' + 'drive.google.com')
            ans = "yes i have opened this site"

        elif 'gmail' in query or 'mail' in query:
            webbrowser.open('https://' + 'mail.google.com')
            ans = "yes i have opened this site"
        else:
            ans = MainFunctions.open_app(query)

        return ans

    # @staticmethod
    # def load_site(final_sentence):
    #     import website_loading
    #     web = website_loading.
# if __name__ == '__main__':
# MainFunctions.play_movies('master')
# pass
