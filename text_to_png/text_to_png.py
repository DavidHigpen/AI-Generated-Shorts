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
        while(abs(draw.textlength(temp_text, font=font) - draw.textlength(temp_text[last_space+1:], font=font)) < max_width):
            prev_last = last_space
            last_space = temp_text.find(' ', last_space + 2)
            if(draw.textlength(temp_text, font=font) < max_width): return text
        last_space = prev_last
        text = text[:last_newline + 1] + temp_text[:last_space] + '\n' + temp_text[last_space+1:]
    return text
            
            
def text_to_image(image_path, profile_pic_path, sub_r, date, OP, title, body, likes, comments):
    title_font_size = 40
    body_font_size = 20
    sub_font_size = 16
    number_font_size = 16
    

    image = Image.open(image_path)
    profile_pic = Image.open(profile_pic_path)
    
    draw = ImageDraw.Draw(image)
    sub_font = ImageFont.truetype("./Verdana.ttf", size=sub_font_size)
    user_font = ImageFont.truetype("./Verdana.ttf", size=sub_font_size)
    date_font = ImageFont.truetype("./Verdana.ttf", size=sub_font_size)
    title_font = ImageFont.truetype("./Verdana.ttf", size=title_font_size)
    body_font = ImageFont.truetype("./Verdana.ttf", size=body_font_size)
    number_font = ImageFont.truetype("./Verdana.ttf", size=number_font_size)
    
    body = wrap_text(draw, body, image.width, body_font)
    # print(draw.textbbox(text=body, font=body_font))
    # draw.textlength

    profile_width = 60
    size_distance = 10
    text_width = image.width - size_distance * 2
    # wrapped = textwrap.fill(body, width=10)
    
    sub_r_x_y = (size_distance * 2 + profile_width, size_distance)
    date_x_y = (size_distance * 2 + profile_width + 80, size_distance)
    OP_x_y = (size_distance * 2 + profile_width, size_distance + 20)
    title_x_y = (size_distance, 80)
    pic_x_y = (size_distance, size_distance)
    body_x_y = (size_distance, 120)
    
    resized_image = profile_pic.resize((profile_width, profile_width)).rotate(90)
    image.paste(resized_image, pic_x_y)

    draw.text(sub_r_x_y, sub_r, fill="white", font=sub_font)
    draw.text(date_x_y, date, fill="white", font=sub_font)
    draw.text(OP_x_y, OP, fill="white", font=sub_font)
    draw.text(title_x_y, title, fill="white", font=title_font)
    draw.text(body_x_y, body, fill="white", font=body_font)
    

    
    image.save('./output_images/image_with_text.png')

    
    
image_path = './empty_post.png'
profile_pic_path = './profile_pic.jpg'
sub_r = 'r/test'
date ='1 month ago'
OP = 'Goofy_Redditor_2026'
title = 'Somebody Help Me'
body = 'Not the logo, but the site in general, such as what you\'re reading right now. I tried googling it, but could only find information about the logo. I then added much more text so that the example post could be long enough that it would have to wrap around a few times. This is just to make sure that my manually implemented function works properly'


likes = 2026
comments = 26
    
text_to_image(image_path, profile_pic_path, sub_r, date, OP, title, body, likes, comments)