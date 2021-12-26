import json
import random

with open('Data/intents.json', 'r') as f:
    intents = json.load(f)
score = 0
tag_names = list()
for intent in intents['intents']:
    tag = intent['tags']
    tag_names.append(tag)
print('tag name', tag_names)



class Dyno_response:
    def __init__(self):
        pass

    @staticmethod
    def bag_of_words(tag_name):
        quest_words = set()
        ans_word = list()
        tag_words = dict()
        tag_ans = dict()
        for items in intents["intents"]:
            if tag_name == items['tags']:
                for quest in items['quest']:

                    quest_word = quest.split(' ')
                    for word in quest_word:
                        quest_words.add(word)
                        ans_word.extend(items['ans'])
                tag_words[items['tags']] = quest_words
                tag_ans[items['tags']] = ans_word

        return [tag_words, tag_ans]

    @staticmethod
    def tag_score(input_choice, tag_name):
        score_g = 0
        tag_words = Dyno_response.bag_of_words(tag_name)[0]
        choice_list = input_choice.split(' ')
        for word in tag_words[tag_name]:
            for co_word in choice_list:
                if co_word == word:
                    score_g = score_g + 1

        return score_g

    @staticmethod
    def predict_tag(user_choice):
        score_dict = dict()
        prob = list()
        for tag_name in tag_names:
            tag_score = Dyno_response.tag_score(user_choice, tag_name)
            tag_score = tag_score / len(tag_name)
            print(tag_score, tag_name)
            score_dict[tag_score] = tag_name
            prob.append(tag_score)

        if max(prob) == 0:
            print(' sorry could not recognise your words')
            tag_dict = 'search'


        else:
            tag_dict = score_dict[max(prob)]

        print (tag_dict, max(prob))
        return tag_dict

    @staticmethod
    def give_response(tag_name):

        tag_ans = Dyno_response.bag_of_words(tag_name)[1]
        tag_ans_choice = tag_ans[tag_name][random.randrange(len(tag_ans[tag_name]))]
        return tag_ans_choice

    @staticmethod
    def clean_sentence(input_choice, tag):
        choice_list = input_choice.split(' ')
        tag_choice = tag
        tag_words = Dyno_response.bag_of_words(tag_choice)[0]

        for word in tag_words[tag_choice]:
            for choices in choice_list:
                if choices == word:
                    choice_list.remove(choices)
        final_sentence = ' '.join(choice_list)
        return final_sentence




if __name__ == '__main__':

    while True:
        choice = input('message: ')
        tag = Dyno_response.predict_tag(choice)
        ans = Dyno_response.give_response(tag)
        final = Dyno_response.clean_sentence(choice)
        print(final+'\n', ans)
