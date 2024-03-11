import os

folder_path = './../story_generation/generated_stories'
file_title = 'shortStory0.txt'
file_path = os.path.join(folder_path, file_title)
with open(file_path, 'r') as text_file:
    print(text_file.read())