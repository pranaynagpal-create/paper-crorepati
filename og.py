 generated with: uv run --with pillow python og.pyfrom PIL import Image, ImageDraw, ImageFont
 generated with: uv run --with pillow python og.pyW,H=1200,630
 generated with: uv run --with pillow python og.pyimg=Image.new("RGB",(W,H),"#EDF2EC"); d=ImageDraw.Draw(img)
 generated with: uv run --with pillow python og.pydef font(path,size):
 generated with: uv run --with pillow python og.py    try: return ImageFont.truetype(path,size)
 generated with: uv run --with pillow python og.py    except Exception: return ImageFont.load_default()
 generated with: uv run --with pillow python og.pyserif=font("/System/Library/Fonts/Supplemental/Baskerville.ttc",96)
 generated with: uv run --with pillow python og.pyserif_sm=font("/System/Library/Fonts/Supplemental/Baskerville.ttc",40)
 generated with: uv run --with pillow python og.pymono=font("/System/Library/Fonts/Menlo.ttc",18)
 generated with: uv run --with pillow python og.pysans=font("/System/Library/Fonts/Supplemental/Arial.ttf",24)
 generated with: uv run --with pillow python og.py# sheet
 generated with: uv run --with pillow python og.pyd.rectangle([40,40,W-40,H-40],fill="#F9FBF7",outline="#C7D4CA")
 generated with: uv run --with pillow python og.pyd.rectangle([48,48,W-48,H-48],outline="#C7D4CA")
 generated with: uv run --with pillow python og.pyd.text((80,78),"AN ESOP REALITY CHECK  ·  INDIA",font=mono,fill="#44564C")
 generated with: uv run --with pillow python og.pyd.text((76,104),"Paper Crorepati",font=serif,fill="#122119")
 generated with: uv run --with pillow python og.pyd.text((80,222),"Your stock options on paper, in your bank account, and if you quit at month 18.",font=sans,fill="#44564C")
 generated with: uv run --with pillow python og.py# three tiles
 generated with: uv run --with pillow python og.pytiles=[("ON PAPER","₹3.6 Cr","the town-hall number","#8F6A1A"),("IN HAND","₹1.7 Cr","after cost and tax at exit","#1C6B47"),("QUIT AT MONTH 18","₹55 L","after finding ₹11 L in 90 days","#A8271F")]
 generated with: uv run --with pillow python og.pyx=80; tw=(W-160-2*24)//3
 generated with: uv run --with pillow python og.pyfor k,big,cap,col in tiles:
 generated with: uv run --with pillow python og.py    d.rectangle([x,290,x+tw,540],fill="#EDF2EC",outline="#C7D4CA")
 generated with: uv run --with pillow python og.py    d.text((x+22,312),k,font=mono,fill=col)
 generated with: uv run --with pillow python og.py    d.text((x+20,350),big,font=serif_sm.font_variant(size=72),fill=col)
 generated with: uv run --with pillow python og.py    d.text((x+22,470),cap,font=font("/System/Library/Fonts/Supplemental/Baskerville.ttc",21),fill="#44564C")
 generated with: uv run --with pillow python og.py    x+=tw+24
 generated with: uv run --with pillow python og.pyd.text((80,566),"Example grant: 10,000 options · ₹100 exercise price · ₹1,200 FMV · 3× exit · 20% dilution. Nothing you type leaves your browser.",font=font("/System/Library/Fonts/Supplemental/Baskerville.ttc",19),fill="#44564C")
 generated with: uv run --with pillow python og.pyimg.save("/Users/pranaynagpal/paper-crorepati/og.png",optimize=True)
 generated with: uv run --with pillow python og.pyprint("og.png", img.size)
