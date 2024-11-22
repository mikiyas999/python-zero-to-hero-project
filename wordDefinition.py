import pyttsx3
from PyDictionary import PyDictionary

def get_word_definition(word):
   dictionary = PyDictionary()
   definition = dictionary.meaning(word)
   if definition:
      return definition.get('Noun', ['No definition found'])[0]
   else:
      return 'No definition found'

def text_to_speech(text):
   engine = pyttsx3.init()
   engine.say(text)
   engine.runAndWait()

def main():
   # Provide spoken prompt
   prompt_text = "Which word do you want to find the meaning of? Please write the word and I will wait."
   text_to_speech(prompt_text)

   # Wait for user to input the word
   print(prompt_text)
   word = input("Word: ").strip()

   if word:
      definition = get_word_definition(word)
      print(f"Definition: {definition}")

      # Provide the definition in audio form
      text_to_speech(definition)
   else:
      print("No word provided.")

if __name__ == "__main__":
   main()
