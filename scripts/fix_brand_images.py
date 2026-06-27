from PIL import Image, ImageDraw, ImageFont
import os

base = r'C:\Users\28295\Desktop\重庆苍茫公司网站v2\assets\images'
font_bold = ImageFont.truetype(r'C:\Windows\Fonts\msyhbd.ttc', 52)
font_small = ImageFont.truetype(r'C:\Windows\Fonts\msyhbd.ttc', 44)

vest_path = os.path.join(base, 'training', 'outdoor-flight-01.jpg')
im = Image.open(vest_path).convert('RGB')
draw = ImageDraw.Draw(im)
w, h = im.size

boxes = [
    (int(w * 0.48), int(h * 0.28), int(w * 0.72), int(h * 0.52)),
    (int(w * 0.02), int(h * 0.30), int(w * 0.22), int(h * 0.50)),
]
for box in boxes:
    region = im.crop(box)
    px = region.getpixel((region.width // 2, region.height // 2))
    draw.rectangle(box, fill=px)

draw.text((int(w * 0.50), int(h * 0.32)), '重庆苍茫', font=font_bold, fill=(20, 20, 20))
draw.text((int(w * 0.50), int(h * 0.32) + 58), '科技有限公司', font=font_small, fill=(20, 20, 20))
draw.text((int(w * 0.04), int(h * 0.34)), '苍茫', font=font_bold, fill=(20, 20, 20))
im.save(vest_path, quality=95)
print('vest saved')

mural_src = r'C:\Users\28295\.cursor\projects\c-Users-28295-Desktop-v2\assets\training-center-mural-cangmang.jpg'
mural_dst = os.path.join(base, 'venue', 'training-center-mural.jpg')
im2 = Image.open(mural_src).convert('RGB')
draw2 = ImageDraw.Draw(im2)
mw, mh = im2.size
font_mural = ImageFont.truetype(r'C:\Windows\Fonts\msyhbd.ttc', 110)
box2 = (int(mw * 0.08), int(mh * 0.52), int(mw * 0.72), int(mh * 0.62))
region2 = im2.crop(box2)
px2 = region2.getpixel((region2.width // 2, region2.height // 2))
draw2.rectangle(box2, fill=px2)
draw2.text((int(mw * 0.10), int(mh * 0.515)), '培训中心', font=font_mural, fill=(255, 255, 255), stroke_width=4, stroke_fill=(0, 0, 0))
im2.save(mural_dst, quality=95)
print('mural saved')

bag_src = r'C:\Users\28295\.cursor\projects\c-Users-28295-Desktop-v2\assets\textbook-equipment-cangmang.jpg'
bag_dst = os.path.join(base, 'training', 'textbook-equipment.jpg')
Image.open(bag_src).save(bag_dst, quality=95)
print('bag saved')
