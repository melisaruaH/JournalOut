from openai import OpenAI
from django.conf import settings
import json

client = OpenAI(api_key=settings.OPENAI_KEY)


def assistUser(journal_body):

    def event_stream():
        for chunk in client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", 
         "content":
         """
         You are a helpful assistant for a journal app where people 
         journal their thoughts and how they feel on a 
         daily basis, your duty is to be a companion on their journey and give them advice.. 
         """
         },
        {"role": "user", "content": f" you are given the next paragraph \n{journal_body}\n give your thoughts about the situation and advice, please respond in the language of that paragraph"},
    ],
    stream=True
    ):
            print(chunk)
            chatcompletion_delta = chunk.choices[0].delta.content
            data = json.dumps({'content':chatcompletion_delta})
            yield f'{data}||'

    return event_stream                                                            