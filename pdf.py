from PIL import Image
from PIL import ImageDraw
import img2pdf
from PIL import ImageFont
import re
import os
file=open("candidate_list.txt")
for name in file:
        name = name.rstrip()
        img = Image.open('/home/nu/Documents/python/sample-1.png')
        width,height=img.size
        I1 = ImageDraw.Draw(img)
        myFont = ImageFont.truetype('OpenSans-Regular.ttf',78)
        y=int(height/2)
        x = int((width/2))
        I1.text((x,y+50), name,font=myFont, fill=(0, 0, 0),anchor="mm")
        name=re.sub(r"\s+", '_', name)
        img.save(str(name)+"_cert.png")
        img_path = str(name)+"_cert.png"
        pdf_path = str(name)+"_cert.pdf"
        image = Image.open(img_path)
        pdf_bytes = img2pdf.convert(image.filename)
        file = open(pdf_path, "wb")
        file.write(pdf_bytes)
        file.close()
        os.remove(img_path)


