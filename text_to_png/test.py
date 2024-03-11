from PIL import Image, ImageDraw, ImageFont
import textwrap

#TODO add bold font

def wrap_text(draw, text, max_width, font):
    last_newline = text.rfind('\n')
    temp_text = text[last_newline + 1:]
    while(draw.textlength(temp_text, font=font) > max_width):
        last_space = -1
        last_newline = text.rfind('\n') 
        temp_text = text[last_newline + 1:]
        while(len(temp_text) > 5 and abs(draw.textlength(temp_text, font=font) - draw.textlength(temp_text[last_space+1:], font=font)) < max_width):
        # for i in range(10):
            print(repr(text))
            print()
            print(repr(temp_text))
            print()
            print(temp_text[last_space+1:])
            print()
            print(abs(draw.textlength(temp_text, font=font) - draw.textlength(temp_text[last_space+1:], font=font)))
            print(max_width)
            last_space = text.find(' ', last_space + 2)
        last_space = text.rfind(' ', 0, last_space)
        text = text[:last_newline + 1] + temp_text[:last_space] + '\n' + temp_text[last_space+1:]
    return text
            
            
def text_to_image(image_path, profile_pic_path, sub_r, date, OP, title, body, likes, comments):
    body_font_size = 26
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    body_font = ImageFont.truetype("./Verdana.ttf", size=body_font_size)
    
    body = wrap_text(draw, body, image.width, body_font)
    # print(draw.textbbox(text=body, font=body_font))
    # draw.textlength

    profile_width = 60
    size_distance = 10
    text_width = image.width - size_distance * 2
    
    body_x_y = (size_distance, 120)
    draw.text(body_x_y, body, fill="white", font=body_font)
    

    
    image.save('./output_images/testImage.png')

    
    
image_path = './empty_post.png'
profile_pic_path = './profile_pic.jpg'
sub_r = 'r/test'
date ='1 month ago'
OP = 'Goofy_Redditor_2026'
title = 'Somebody Help Me'
body = 'Not the logo, but the site in general, such as what you\'re reading right now. I tried googling it, but could only find information about the logo.'


likes = 2026
comments = 26
    
text_to_image(image_path, profile_pic_path, sub_r, date, OP, title, body, likes, comments)