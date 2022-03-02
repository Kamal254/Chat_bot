# Chat_bot 
I create a chatbot on my local server using Rasa NLU, Rasa Core.
using custom actions for reply by BOT

# Steps
Install rasa in your computer using 

pip install rasa

rasa init --no-prompt

There are many files generated after initialising Rasa. I only used few of them
1. data/nlu.yml
   
   This is the folder where you give examples of how the specific intents can be asked. 
   For Intent (think of this as your intention to do something) like "greet",
   you would be asking "hi", "hello", "nice to meet you" and so on.
   This is where you list out these examples.
   ## intent:greet
   - hey
   - hello
   - hi
2. data/stories.yml
   
   This is where you are basically narrating.
   It is where you give examples of how the flow of the chat can go.
   This is where you write down as many possible path of the chatflow as you can.
   ## happy path
  * greet
    - utter_greet
  * mood_great
    - utter_happy

3. domain.yml
    
    You can basically think of this as the library. This is where you declare everything. 
    All the intents that you are planning to use in your stories and nlu list them under intents.
    All the actions refer to what the bot will do when it detects a certain intent. 
    Templates are for special kind of actions called utterances which is what the bot will reply. 
    This is where utterances that were under actions get defined.

    There are also slots and entities that can be defined in this file.

    intents:
      - greet
      - goodbye


    actions:
    - utter_greet
    - utter_cheer_up


    templates:
        utter_greet:
        - text: "Hey! How are you?"

        utter_cheer_up:
        - text: "Here is something to cheer you up:"
            image: "https://i.imgur.com/nGF1K8f.jpg"
        
# Rasa Train & Test
  Now our Bot is ready to Chat
  Use following comands to  train and active our bot to chat
  - cd rasa
  - rasa train
  - rasa shell
  Now we are ready to chat with our chat bot
  

  
   
