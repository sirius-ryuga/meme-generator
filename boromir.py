from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
image = Image.open("boromir.jpg")
word = ImageDraw.Draw(image)
shadow = ImageDraw.Draw(image)
black = ImageDraw.Draw(image)
dark = ImageDraw.Draw(image)
darkness = ImageDraw.Draw(image)
font = ImageFont.truetype('/Library/Fonts/Arial.ttf', size=30)
shadow.text((21, 250), "You can't just do your Python well", fill="black", font=font)
black.text((19, 250), "You can't just do your Python well", fill="black", font=font)
dark.text((20, 251), "You can't just do your Python well", fill="black", font=font)
darkness.text((20, 249), "You can't just do your Python well", fill="black", font=font)
word.text((20, 250), "You can't just do your Python well", fill="white", font=font)
image.save("boromir.jpg")





