from openai import OpenAI
import gradio as gr
import os

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def predict(message, history):
    try:
        history_openai_format = []
        for human, assistant in history:
            history_openai_format.append({"role": "user", "content": human })
            history_openai_format.append({"role": "assistant", "content":assistant})
        history_openai_format.append({"role": "user", "content": message})
  
        response = client.chat.completions.create(model='gpt-3.5-turbo',
        messages= history_openai_format,
        temperature=1.0,
        stream=True)
        return response.choices[0].message.content
        # partial_message = ""
        # for chunk in response:
        #     if chunk.choices[0].delta.content is not None:
        #         partial_message = partial_message + chunk.choices[0].delta.content
        #         yield partial_message
    except Exception as e:
        print(f"An error occurred: {e}")  # Log to console for debugging.
        return f"An error occurred: {str(e)}"  # Return a user-friendly error message.

gr.ChatInterface(predict).launch(debug=True)