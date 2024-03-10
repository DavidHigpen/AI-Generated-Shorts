import openai
import os
import pandas as pd

#make sure to have a .emv file where OPENAI_API_KEY=<yourkey>

# openai.api_key = OPENAI_API_KEY
folder_path = './generated_stories'
storyNames = 'shortStory'

# def get_completion(prompt, model="gpt-3.5-turbo"):
#     messages = [{"role": "user", "content": prompt}]
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=0,
#     )
#     return response.choices[0].message["content"]

def print_to_file(text):
    if os.path.exists(folder_path) and os.path.isdir(folder_path) and len(os.listdir(folder_path)) > 0:
        new_num = max(
            [int(name[4:-4]) if 
             len(name) >= len(storyNames) + 5 and name[:len(storyNames)] == storyNames and name[4:-4].isnumeric() 
             else -1 for name in os.listdir(folder_path)]
            ) + 1
    else: new_num = 0
    file_title = storyNames + str(new_num) + '.txt'
    file_path = os.path.join(folder_path, file_title)
    with open(file_path, "w") as text_file:
        text_file.write(text)
        text_file.close()
    

# prompt = "Tell me a joke"
# response = get_completion(prompt)
# print(response)

print_to_file("test content")