# Odcinek 22 "Woda pitna" -> bajka/woda.html
# Kolejnosc po zmianach: python3 build_ep22.py && python3 dubbing.py woda && python3 fix_audio.py woda
import importlib, re, sys
B = '/Users/arturwyrzykowski/Programowanie/bajka/'
sys.path.insert(0, B)
import ep22_sceny; importlib.reload(ep22_sceny)

src = open(B + 'nogi.html', encoding='utf-8').read()
head = src[:src.index('<svg id="stage"')].replace('<title>Potężny trening nóg</title>', '<title>Woda pitna</title>')
# mina "strach": okulary zjezdzaja na nos, widac wytrzeszczone oczy, usta otwarte
head = head.replace('</style>', '  .strach .okulary { transform:translateY(46px); }\n  .strach .oczy { display:inline !important; }\n  .strach .mO { display:inline !important; }\n  .strach .mC { display:none; }\n</style>', 1)

DEFS = '''  <defs>
    <filter id="grainF"><feTurbulence id="grainT" type="fractalNoise" baseFrequency="0.85" numOctaves="2" seed="3"/><feColorMatrix type="saturate" values="0"/></filter>
    <radialGradient id="vign" cx="50%" cy="50%" r="72%"><stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.6"/></radialGradient>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="10"/></filter>
    <filter id="blur4"><feGaussianBlur stdDeviation="4"/></filter>
    <filter id="mblur" x="-20%" y="-5%" width="140%" height="110%"><feGaussianBlur stdDeviation="18 0"/></filter>
''' + ep22_sceny.DEFS + '''  </defs>'''

LAYERS = f'''  <g id="cam"><g id="shots">
{ep22_sceny.SHOTS_SVG}
    <g id="fx2"></g>
  </g></g>
  <g id="snow" style="display:none" pointer-events="none"></g>
  <g id="glitch" style="display:none" pointer-events="none">
    <rect width="1600" height="40" fill="#ff00aa" opacity=".45"/><rect width="1600" height="30" fill="#00e5ff" opacity=".45"/>
    <rect width="1600" height="60" fill="#ffffff" opacity=".25"/><rect width="1600" height="20" fill="#00ff66" opacity=".4"/>
  </g>
  <rect width="1600" height="900" filter="url(#grainF)" opacity="0.08" pointer-events="none"/>
  <rect width="1600" height="900" fill="url(#vign)" pointer-events="none"/>
  <rect id="barT" width="1600" height="114" fill="#000"/><rect id="barB" y="786" width="1600" height="114" fill="#000"/>
  <text id="capTxt" x="800" y="852" text-anchor="middle" font-family="Georgia, serif" font-size="40" letter-spacing="4" fill="#e8c33a" style="display:none"></text>

  <rect id="flash" width="1600" height="900" fill="#fff" opacity="0" pointer-events="none"/>
  <rect id="fade" width="1600" height="900" fill="#000" opacity="0" pointer-events="none"/>
  <g id="chapter" style="display:none"><rect width="1600" height="900" fill="#000"/>
    <text id="chNr" x="800" y="400" text-anchor="middle" font-family="Georgia, serif" font-size="44" letter-spacing="12" fill="#e8c33a"></text>
    <text id="chTitle" x="800" y="510" text-anchor="middle" font-family="Georgia, serif" font-size="104" font-weight="700" letter-spacing="6" fill="#e8c33a"></text></g>'''

OVERLAYS = '''<div class="overlay" id="startScreen">
  <h1>WODA PITNA</h1>
  <p>odcinek 22</p>
  <button class="btn" id="playBtn" autofocus>▶ Odtwórz</button>
</div>
<div class="overlay" id="endScreen" hidden>
  <h1>KONIEC</h1>
  <button class="btn" id="againBtn">↺ Od nowa</button>
</div>'''

rd = lambda f: open(B + f, encoding='utf-8').read()
JS = (rd('ep21_core.js') + '\n' + rd('ep21_audio.js') + '\n' + rd('ep21_kino.js') + '\n' + ep22_sceny.WHO_JS + '\n' + rd('ep22_play.js') +
      '\n  const start = () => { unlockSpeech(); unlockClips(); play(); };\n  $("playBtn").addEventListener("click", start);\n  $("againBtn").addEventListener("click", start);\n')

html = (head + '<svg id="stage" viewBox="0 0 1600 900" aria-label="Bajka: Woda pitna" style="background:#000">\n' + DEFS + '\n' + LAYERS + '\n</svg>\n\n' + OVERLAYS +
        '\n</div>\n\n<script src="intro2.js"></script>\n<script>\n' + JS + '</script>\n</body>\n</html>\n')

# glosy wygenerowane wczesniej: zachowaj CLIPS z poprzedniej wersji (dubbing.py i tak je nadpisze)
try:
    old = open(B + 'woda.html', encoding='utf-8').read()
    m = re.search(r'const CLIPS = \{.*?\n?\s*\};', old, re.S)
    if m: html = html.replace('const CLIPS = {};', m.group(0), 1)
except FileNotFoundError:
    pass
open(B + 'woda.html', 'w', encoding='utf-8').write(html)
print('woda.html', len(html) // 1024, 'KB')
