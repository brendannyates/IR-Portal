import os
from PIL import Image, ImageDraw
os.makedirs('dist/assets', exist_ok=True)
html = open('src/taskpane.html').read()
man = open('src/manifest.xml').read()
assert '`' not in man and '${' not in man
html = html.replace('`__MANIFEST__`', '`' + man.replace('\\','\\\\') + '`')
open('dist/taskpane.html','w').write(html)
open('dist/index.html','w').write('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=taskpane.html"><title>IR Portal Tracker</title><a href="taskpane.html">IR Portal Tracker</a>')
open('dist/commands.html','w').write('<!doctype html><meta charset="utf-8"><title>IR Portal Tracker commands</title><script src="https://appsforoffice.microsoft.com/lib/1/hosted/office.js"></script><script>Office.onReady(function(){});</script>')
# demo page: same app without Office.js, opens straight into demo data
demo = html.replace('<script src="https://appsforoffice.microsoft.com/lib/1/hosted/office.js"></script>', '').replace("const demo = /[?&]demo\\b/.test(location.search);", "const demo = true;")
assert 'const demo = true;' in demo
open('dist/demo.html','w').write(demo)
W=(255,253,248,255)
for sz in (16,32,64,80,128):
    S=sz*4; im=Image.new('RGBA',(S,S),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle([0,0,S-1,S-1],radius=S//4,fill=(181,83,47,255))
    lw=max(2,S//18)
    d.rounded_rectangle([S*0.27,S*0.18,S*0.73,S*0.82],radius=S*0.05,outline=W,width=lw)   # page
    d.line([(S*0.36,S*0.36),(S*0.64,S*0.36)],fill=W,width=lw)                            # text line
    d.line([(S*0.36,S*0.5),(S*0.56,S*0.5)],fill=W,width=lw)
    d.line([(S*0.36,S*0.68),(S*0.44,S*0.62),(S*0.5,S*0.7),(S*0.58,S*0.62),(S*0.64,S*0.68)],fill=W,width=lw)  # signature squiggle
    im.resize((sz,sz),Image.LANCZOS).save(f'dist/assets/icon-{sz}.png')
import shutil
for f in ('logo.png','logo-dark.png'): shutil.copy(f'src/assets/{f}', f'dist/assets/{f}')
print('built')
