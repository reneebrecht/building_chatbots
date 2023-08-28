from collections import Counter
from responses import responses, blank_spot
from user_functions import preprocess, compare_overlap, pos_tag, extract_nouns, compute_similarity
import spacy
word2vec = spacy.load('en')

exit_commands = ("quit", "goodbye", "exit")

class ChatBot:
  
  #define .make_exit() below:
  def make_exit(self, user_message):
    for exit_command in exit_commands:
      if exit_command in user_message:
        print("Goodbye sucker! ") 
        return True
    return False
  #define .chat() below:
  def chat(self):
    user_message = input("Welcome to Cyborg Cantina, your favourite mexican restaurant!")
    while not self.make_exit(user_message):
      user_message = self.respond(user_message)

  #define .find_intent_match() below:
  def find_intent_match(self, responses, user_message):
    bow_user_message = Counter(preprocess(user_message))
    processed_responses = [Counter(preprocess(response)) for response in responses]
    similarity_list = [compare_overlap(bow_user_message, response) for response in processed_responses]
    response_index = similarity_list.index(max(similarity_list))
    return responses[response_index]
  
  #define .find_entities() below:
  def find_entities(self, user_message):
    tagged_user_message = pos_tag(preprocess(user_message))
    message_nouns = extract_nouns(tagged_user_message)
    tokens = word2vec(" ".join(message_nouns))
    category = word2vec(blank_spot)
    word2vec_result = compute_similarity(tokens, blank_spot)
    word2vec_result = sort(key=lambda x: x[2])
    if word2vec_result:
    return word2vec_result[-1][0]
else:
    return blank_spot
  #define .respond() below:
  def respond(self, user_message):
    best_response = self.find_intent_match(responses, user_message)
    entity = self.find_entities(user_message)
    print(best_response.format(entity))
    input_message = input("Do you have any other questions? ")           
    return input_message

#initialize ChatBot instance below:
ChatBot = ChatBot()
#call .chat() method below:
ChatBot.chat()