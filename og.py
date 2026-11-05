# generated with: uv run --with pillow python og.py
from PIL import Image, ImageDraw, ImageFont
W,H=1200,630
HELV="/System/Library/Fonts/Helvetica.ttc"
def font(size,bold=False):
    try: return ImageFont.truetype(HELV,size,index=1 if bold else 0)
    except Exception: return ImageFont.load_default()
img=Image.new("RGB",(W,H),"#ffffff"); d=ImageDraw.Draw(img)
d.text((80,92),"Paper Crorepati",font=font(76,True),fill="#111111")
d.text((80,196),"What your ESOPs are worth on paper, what actually reaches your bank,",font=font(28),fill="#6b6b6b")
d.text((80,236),"and what happens if you quit at 18 months.",font=font(28),fill="#6b6b6b")
d.line([(80,318),(W-80,318)],fill="#e3e3e3",width=2)
cols=[("ON PAPER","₹3.6 Cr","What HR says it is worth"),("IN HAND","₹1.7 Cr","After dilution, cost and tax"),("IF YOU QUIT AT 18 MONTHS","₹55 L","Only after paying ₹11 L in cash")]
x=80; cw=(W-160)//3
for k,big,cap in cols:
    d.text((x,350),k,font=font(18),fill="#6b6b6b")
    d.text((x-2,386),big,font=font(68,True),fill="#111111")
    d.text((x,478),cap,font=font(21),fill="#6b6b6b")
    x+=cw
d.line([(80,536),(W-80,536)],fill="#e3e3e3",width=2)
d.text((80,556),"Example: 10,000 options, ₹100 exercise price, ₹1,200 current value, 3× growth. Nothing you type leaves your browser.",font=font(19),fill="#6b6b6b")
img.save("og.png",optimize=True); print("og.png",img.size)
