import google.generativeai as genai
from decouple import config

genai.configure(api_key=config('GOOGLE_GENAI_KEY'))

safety = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=None,
                              safety_settings=safety)

chat = model.start_chat(history=[])

initialPrompt = """
We are playing a text-based adventure game!
Make up a story about anything you'd like and be my narrator along the journey and respond to my actions.
Limit responses to one or two sentence max. 
Only respond with the narrators side of the story, my response will impact future outcomes and guide the story forward.
Limit your descriptive words and be more direct with the situation.
"""

try:
  response = chat.send_message(initialPrompt)
  print(response.text)
except Exception as e:
  print(f'{type(e).__name__}: {e}')

def getNewAIMessage(message):
  res = chat.send_message(message)
  return res.text