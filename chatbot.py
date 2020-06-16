#Import libraries

import random
from textblob import TextBlob

#Name and nickname conversion

print('Hello human what is your name? ')
name = input()
print("Do you have a nickname")
ans = input()
if 'y' in ans.lower():
    nickname = input(("What is your nickname "))
    print('Good to meet you ' + nickname)
else:
    nickname = name + 'y'
    print('I will call you ' + nickname)
    print("")

#Greeting Selection
greetings = [
    'How’s it going ' + nickname + '?',
    'How are you doing ' + nickname + '?',
    'What’s up ' + nickname +'? ',
    'What’s new ' + nickname + '? ',
    'What’s going on ' + nickname + '? ',
    'How’s your day ' + nickname +'? ',
    'How’s your day going ' + nickname + '? ',
    'Long time no see. What up homie? '
]

print(random.choice(greetings))

ans = input()
blob = TextBlob(ans)

if blob.polarity > 0:
    print("Glad you're doing well")
else:
    print("I'm a bot, I couldn't care less.")

#Random opinions on topics

topics = [
    'football',
    'guns',
    'COVID',
    'Endgame',
    'Computers',
    'Games'
]

questions = [
    'What is your take on ',
    'What do you think about ',
    'How do you feel about ',
    'What do your reckon about ',
    'I would like your opinion on ',
]
for i in range(0, random.randint(3, 4)):
    question = random.choice(questions)
    questions.remove(question)

    topic = random.choice(topics)
    topics.remove(topic)
    print("")
    print(question + topic + '?')

    answer = input()
    blob = TextBlob(answer)

    if blob.polarity > 0.5:
        print('OMG you really love ' + topic)
    elif blob.polarity > 0.1:
        print('Well you clearly like ' + topic)
    elif blob.polarity < -0.5:
        print("Dang, you really hate " + topic)
    elif blob.polarity < 0:
        print("So you don't like " + topic)
    else:
        print('That is a very neutral view on ' + topic)

    if blob.subjectivity > 0.6:
        print('and you are so biased ')
    elif blob.subjectivity > 0.3:
        print('and you are a bit biased')
    else:
        print('and you are quite objective')

#Goodbye
goodbyes = [
    'Later Alligator ',
    'Imma out of here ',
    "I'm gonna go watch netflix ",
    "I'm bored ",
    "Bye ",
]
goodbye = random.choice(goodbyes)
print("")
print(goodbye)
