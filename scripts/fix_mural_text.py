from PIL import Image, ImageDraw, ImageFont
import shutil

src = r'C:\Users\28295\Desktop\重庆苍茫公司网站v2\培训点宣传材料\bf5c9c15-b868-4f1e-bf02-53107973c5af.jpg'
dst = r'C:\Users\28295\Desktop\重庆苍茫公司网站v2\assets\images\venue\training-center-mural.jpg'

shutil.copy2(src, dst)
im = Image.open(dst).convert('RGB')
draw = ImageDraw.Draw(im)
w, h = im.size

# 精确遮盖「珀」单字，改为「茫」，不触碰「培训中心」行
box = (int(w * 0.218), int(h * 0.409), int(w * 0.278), int(h * 0.441))
patch = im.crop(box)
fill = patch.getpixel((patch.width // 2, patch.height // 2))
draw.rectangle(box, fill=fill)

font = ImageFont.truetype(r'C:\Windows\Fonts\msyhbd.ttc', int(w * 0.052))
draw.text((int(w * 0.221), int(h * 0.411)), '茫', font=font, fill=(255, 255, 255), stroke_width=2, stroke_fill=(20, 20, 20))

im.save(dst, quality=95)
print('done - only 珀->茫')
