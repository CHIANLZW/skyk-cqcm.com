from PIL import Image, ImageDraw, ImageFont
import os

mural_src = r'C:\Users\28295\.cursor\projects\c-Users-28295-Desktop-v2\assets\training-center-mural-cangmang.jpg'
mural_dst = r'C:\Users\28295\Desktop\重庆苍茫公司网站v2\assets\images\venue\training-center-mural.jpg'

im = Image.open(mural_src).convert('RGB')
draw = ImageDraw.Draw(im)
mw, mh = im.size
font_mural = ImageFont.truetype(r'C:\Windows\Fonts\msyhbd.ttc', 95)

# Only cover the extra 心 character area at end of 培训中心心
box = (int(mw * 0.52), int(mh * 0.535), int(mw * 0.68), int(mh * 0.60))
region = im.crop(box)
px = region.getpixel((10, region.height // 2))
draw.rectangle(box, fill=px)

im.save(mural_dst, quality=95)
print('mural typo fixed')
