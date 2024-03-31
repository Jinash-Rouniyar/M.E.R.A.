from openai import OpenAI
import tiktoken
import os

class OpenAiManager:
    
    def __init__(self):
        self.chat_history = [] # Stores the entire conversation
        try:
            self.client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
        except TypeError:
            exit("Ooops! You forgot to set OPENAI_API_KEY in your environment!")

    # Asks a question with no chat history
    def chat(self, prompt=""):
        if not prompt:
            print("Didn't receive input!")
            return

        # Check that the prompt is under the token context limit
        chat_question = [{"role": "user", "content": prompt}]

        completion = self.client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=chat_question
        )

        # Process the answer
        openai_answer = completion.choices[0].message.content
        print(f"{openai_answer}")
        return openai_answer

    # Asks a question that includes the full conversation history
    def chat_with_history(self, prompt=""):
        if not prompt:
            print("Didn't receive input!")
            return

        # Add our prompt into the chat history
        self.chat_history.append({"role": "user", "content": prompt})

        completion = self.client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=self.chat_history
        )

        # Add this answer to our chat history
        self.chat_history.append({"role": completion.choices[0].message.role, "content": completion.choices[0].message.content})

        # Process the answer
        openai_answer = completion.choices[0].message.content
        print(f"{openai_answer}")
        return openai_answer