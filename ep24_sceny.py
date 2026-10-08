# Odcinek 24 "Woda mineralna": ujecia (kazde = <g class="shot" id="sh...">, 1600x900, kadr widoczny y 114..786)
import importlib, math, random, sys
B = '/Users/arturwyrzykowski/Programowanie/bajka/'
sys.path.insert(0, B)
import ep21_postacie as P; importlib.reload(P)
import ep21_sceny as S21
import ep22_sceny as S22; importlib.reload(S22)
K = "#141414"
SKIN = P.SKIN
OL = f'stroke="{K}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"'
g = S22.g
MET = "#6b6a3e"          # brudna woda z beczki
HARC = "#6f7d4c"         # mundur harcerski

DEFS = S22.DEFS + '''    <radialGradient id="zar" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#fff2a0"/><stop offset=".5" stop-color="#ff7a1a"/><stop offset="1" stop-color="#c81e1e" stop-opacity="0"/></radialGradient>
    <linearGradient id="skyRano" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8ab8e8"/><stop offset=".7" stop-color="#f6dcb0"/><stop offset="1" stop-color="#ffe8c0"/></linearGradient>
    <linearGradient id="rzeka" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5a9a8a"/><stop offset="1" stop-color="#3a6a5a"/></linearGradient>
    <linearGradient id="lasG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a4a2a"/><stop offset="1" stop-color="#1a301c"/></linearGradient>
    <linearGradient id="szyba" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#cfe8f6" stop-opacity=".38"/><stop offset="1" stop-color="#8ab8d8" stop-opacity=".18"/></linearGradient>
    <linearGradient id="emalia" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#d8dde2"/></linearGradient>
'''

# ================= GLOWY (300x320, kontur 5, usta .mC/.mO) =================
def _glowa(inner, w=160):
    h = w * 320 / 300
    return (f'<svg class="glowa" viewBox="0 0 300 320" overflow="visible" x="{-w / 2}" y="{-456}" width="{w}" height="{h:.0f}">'
            f'<g stroke="{K}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round">{inner}</g></svg>')

def usta(cx=150, cy=252, w=34):
    return (f'<path class="mC" d="M{cx - w} {cy} Q{cx} {cy + 14} {cx + w} {cy}" fill="none"/>'
            f'<g class="mO" style="display:none"><path d="M{cx - w} {cy - 6} Q{cx} {cy - 10} {cx + w} {cy - 6} Q{cx + w - 6} {cy + 32} {cx} {cy + 34} Q{cx - w + 6} {cy + 32} {cx - w} {cy - 6} Z" fill="#5a1717"/>'
            f'<path d="M{cx - 14} {cy + 22} Q{cx} {cy + 12} {cx + 14} {cy + 22}" fill="#e05a5a" stroke="none"/></g>')

def head_ksiadz():
    return _glowa(f'''
      <ellipse cx="46" cy="186" rx="18" ry="28" fill="#f4b48a"/><ellipse cx="254" cy="186" rx="18" ry="28" fill="#f4b48a"/>
      <path d="M48 150 Q46 36 150 32 Q254 36 252 150 L258 222 Q256 300 150 310 Q44 300 42 222 Z" fill="#f4b48a"/>
      <path d="M78 286 Q150 330 222 286" fill="none" stroke-width="4"/><path d="M100 300 Q150 322 200 300" fill="none" stroke-width="3" opacity=".6"/>
      <path d="M50 160 Q36 112 64 84 Q78 126 72 176 Z" fill="#d8d8d4"/><path d="M250 160 Q264 112 236 84 Q222 126 228 176 Z" fill="#d8d8d4"/>
      <path d="M104 66 Q140 50 178 60" fill="none" stroke="#fff" stroke-width="8" opacity=".55"/>
      <ellipse cx="88" cy="226" rx="30" ry="18" fill="#e8605a" opacity=".55" stroke="none"/><ellipse cx="212" cy="226" rx="30" ry="18" fill="#e8605a" opacity=".55" stroke="none"/>
      <path d="M86 142 Q112 128 136 142 M164 142 Q188 128 214 142" fill="none" stroke="#a8a8a4" stroke-width="12"/>
      <g class="oczyN"><path d="M96 172 Q114 158 132 172" fill="none" stroke-width="7"/><path d="M168 172 Q186 158 204 172" fill="none" stroke-width="7"/></g>
      <g class="oczyW" style="display:none"><path d="M96 168 Q114 180 132 168" fill="none" stroke-width="7"/><circle cx="186" cy="170" r="11" fill="{K}"/></g>
      <ellipse cx="150" cy="208" rx="26" ry="22" fill="#e8806a"/>
      {usta(150, 256, 38)}''', 170)

def head_opiekun():
    return _glowa(f'''
      <ellipse cx="58" cy="182" rx="16" ry="24" fill="#eeb088"/><ellipse cx="242" cy="182" rx="16" ry="24" fill="#eeb088"/>
      <path d="M60 140 Q60 44 150 40 Q240 44 240 140 L238 230 Q228 304 150 310 Q72 304 62 230 Z" fill="#eeb088"/>
      <path d="M92 132 Q114 120 134 132 M166 132 Q186 120 208 132" fill="none" stroke="#6a4a2a" stroke-width="9"/>
      <g class="okulary"><circle cx="113" cy="168" r="28" fill="#dff0fa" fill-opacity=".5"/><circle cx="187" cy="168" r="28" fill="#dff0fa" fill-opacity=".5"/><path d="M141 168 H159 M85 164 L62 156 M215 164 L238 156" fill="none"/></g>
      <circle cx="113" cy="170" r="8" fill="{K}"/><circle cx="187" cy="170" r="8" fill="{K}"/>
      <path d="M150 178 Q136 214 146 222 Q154 228 164 222" fill="none" stroke-width="5"/>
      <path d="M104 236 Q150 220 196 236 Q190 252 150 246 Q110 252 104 236 Z" fill="#7a5230"/>
      {usta(150, 262, 26)}
      <!-- kapelusz harcerski z szerokim rondem -->
      <path d="M14 108 Q150 70 286 108 Q290 124 270 128 Q150 100 30 128 Q10 124 14 108 Z" fill="#8a7a4a"/>
      <path d="M70 108 Q66 30 112 18 Q150 34 188 18 Q234 30 230 108 Q150 90 70 108 Z" fill="#9a8a5a"/>
      <path d="M72 96 Q150 80 228 96 L228 110 Q150 94 72 110 Z" fill="#5a4a2a"/>''', 160)

def head_listonosz():
    return _glowa(f'''
      <ellipse cx="54" cy="184" rx="16" ry="24" fill="#f0b48a"/><ellipse cx="246" cy="184" rx="16" ry="24" fill="#f0b48a"/>
      <path d="M56 150 Q56 50 150 46 Q244 50 244 150 L242 226 Q232 300 150 306 Q68 300 58 226 Z" fill="#f0b48a"/>
      <circle cx="114" cy="170" r="9" fill="{K}"/><circle cx="186" cy="170" r="9" fill="{K}"/>
      <path d="M96 146 Q114 136 132 146 M168 146 Q186 136 204 146" fill="none" stroke="#3a2a1a" stroke-width="8"/>
      <path d="M150 176 Q132 214 144 222 Q156 230 166 220" fill="#e89a6e"/>
      <path d="M96 236 Q124 220 150 232 Q176 220 204 236 Q196 256 150 248 Q104 256 96 236 Z" fill="#3a2a1a"/>
      {usta(150, 266, 24)}
      <path d="M50 120 Q48 40 150 34 Q252 40 250 120 Z" fill="#26407a"/>
      <rect x="50" y="96" width="200" height="30" fill="#f2c230"/>
      <text x="150" y="120" text-anchor="middle" font-family="Arial Black, sans-serif" font-size="24" fill="#26407a" stroke="none">POCZTA</text>
      <path d="M150 122 Q220 120 284 140 Q254 154 150 140 Z" fill="#1a2a5a"/>''', 156)

def head_stiven_lato():
    # Stiven bez opuszczonych nausznikow (lato)
    h = P.head_stiven()
    h = h.replace('<path d="M40 116 Q30 170 44 210 Q66 220 74 196 L72 120 Z" fill="#1c428c"/>', '')
    h = h.replace('<path d="M262 116 Q272 170 258 210 Q236 220 228 196 L230 120 Z" fill="#1c428c"/>', '')
    return h

# ================= CIALA =================
def nogi(gora, dol, buty="#2a2a2a", pose="stand"):
    # gora = spodnie/spodenki, dol = kolor lydki (skora / nogawka / podkolanowka)
    if pose == "sit":
        return (f'<path d="M-34 -106 L70 -100" stroke-width="50"/><path d="M-34 -106 L70 -100" stroke="{gora}" stroke-width="40"/>'
                f'<path d="M70 -100 L76 -34" stroke-width="40"/><path d="M70 -100 L76 -34" stroke="{dol}" stroke-width="30"/>'
                f'<path d="M52 -40 Q46 -2 66 0 H112 Q116 -22 98 -40 Z" fill="{buty}"/>')
    def noga(cls, o, sx):
        return (f'<g class="{cls}" style="transform-origin:{o}px -150px"><path d="M{o} -170 L{o + sx * 2} -30" stroke-width="44"/>'
                f'<path d="M{o} -170 L{o + sx} -96" stroke="{gora}" stroke-width="40"/><path d="M{o + sx} -96 L{o + sx * 2} -34" stroke="{dol}" stroke-width="32"/>'
                f'<path d="M{o - 30} -40 Q{o - 34} -2 {o - 18} 0 H{o + 38} Q{o + 40} -22 {o + 30} -40 Z" fill="{buty}"/></g>')
    return noga("legL", -24, -1) + noga("legR", 24, 1)

def rece(kol, pose="stand", hold="", reka=SKIN):
    item = {
        "telefon": f'<g class="telefon"><rect x="64" y="-206" width="26" height="46" rx="5" fill="#1a1a1a" stroke-width="3"/><rect x="68" y="-200" width="18" height="32" fill="#4a8ad8" stroke="none"/></g>',
        "kubek": f'<g class="kubek"><rect x="64" y="-200" width="38" height="44" rx="5" fill="#fbfbf6" stroke-width="4"/><path d="M102 -192 Q118 -180 102 -168" fill="none" stroke-width="5"/><rect x="68" y="-196" width="30" height="8" fill="#6a3a1a" stroke="none"/></g>',
        "gazeta": f'<g class="gazeta"><rect x="40" y="-250" width="96" height="120" fill="#efeee6" stroke-width="4" transform="rotate(8 88 -190)"/><path d="M54 -226 H122 M54 -210 H120 M54 -196 H110" stroke="#888" stroke-width="4" transform="rotate(8 88 -190)"/></g>',
        "flaszka": f'<g class="flaszka"><rect x="68" y="-226" width="28" height="62" rx="6" fill="#e8f4f8" opacity=".95" stroke-width="3"/><rect x="75" y="-250" width="14" height="26" fill="#e8f4f8" stroke-width="3"/><rect x="74" y="-256" width="16" height="8" fill="#c81e1e" stroke-width="2"/><rect x="68" y="-206" width="28" height="22" fill="#fff" stroke-width="2"/></g>',
        "waz": f'<g class="wazR"><path d="M82 -168 Q140 -110 150 -10" fill="none" stroke="#1a1a1a" stroke-width="22"/><path d="M82 -168 Q140 -110 150 -10" fill="none" stroke="#3a3f48" stroke-width="14"/></g>',
        "gwizdek": f'<g class="gwizdek"><rect x="70" y="-196" width="30" height="16" rx="6" fill="#c9ced6" stroke-width="3"/></g>',
    }.get(hold, '')
    lewa = (f'<path d="M-62 -296 Q-86 -220 -78 -160" fill="none" stroke-width="34"/><path d="M-70 -262 Q-86 -214 -78 -160" fill="none" stroke="{reka}" stroke-width="24"/>'
            f'<path d="M-62 -296 Q-70 -278 -70 -262" fill="none" stroke="{kol}" stroke-width="30"/><circle cx="-78" cy="-152" r="16" fill="{reka}"/>')
    if pose == "ucho":
        return lewa + (f'<g class="armR"><path d="M62 -296 Q120 -260 96 -360" fill="none" stroke-width="34"/><path d="M80 -280 Q118 -262 96 -360" fill="none" stroke="{reka}" stroke-width="24"/>'
                       f'<path d="M62 -296 Q74 -290 84 -280" fill="none" stroke="{kol}" stroke-width="30"/>'
                       f'<rect x="78" y="-406" width="26" height="50" rx="5" fill="#1a1a1a" stroke-width="3"/><circle cx="96" cy="-362" r="16" fill="{reka}"/></g>')
    if pose == "kciuk":   # prawa reka w gorze, kciuk w gore
        return lewa + (f'<g class="armR" style="transform-origin:62px -296px"><path d="M62 -296 Q120 -330 120 -420" fill="none" stroke-width="34"/>'
                       f'<path d="M62 -296 Q120 -330 120 -420" fill="none" stroke="{kol}" stroke-width="26"/>'
                       f'<rect x="100" y="-452" width="40" height="40" rx="12" fill="{reka}" stroke-width="4"/><rect x="108" y="-490" width="16" height="44" rx="8" fill="{reka}" stroke-width="4"/>'
                       f'<path d="M104 -440 H136 M104 -428 H136" stroke-width="3"/></g>')
    if pose == "machaj":
        return lewa + (f'<g class="armR" style="transform-origin:62px -296px"><path d="M62 -296 Q110 -330 104 -410" fill="none" stroke-width="34"/>'
                       f'<path d="M62 -296 Q110 -330 104 -410" fill="none" stroke="{kol}" stroke-width="26"/><circle cx="104" cy="-418" r="18" fill="{reka}"/></g>')
    return lewa + (f'<g class="armR" style="transform-origin:62px -296px"><path d="M62 -296 Q88 -240 82 -176" fill="none" stroke-width="34"/>'
                   f'<path d="M72 -262 Q88 -224 82 -176" fill="none" stroke="{reka}" stroke-width="24"/><path d="M62 -296 Q70 -278 72 -262" fill="none" stroke="{kol}" stroke-width="30"/>'
                   f'{item}<circle cx="82" cy="-170" r="16" fill="{reka}"/></g>')

def wrap(pid, inner, cls=""):
    return (f'<g id="{pid}" class="postac {cls}"><g class="bob" style="transform-origin:0px 0px"><g stroke="{K}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">'
            f'{inner}</g></g></g>')

def koszulka(col, dlugi=False):
    bot = -130 if dlugi else -150
    return (f'<path d="M-70 -312 Q-84 -230 -72 {bot} L72 {bot} Q84 -230 70 -312 Q0 -330 -70 -312 Z" fill="{col}"/>'
            f'<path d="M-22 -318 Q0 -300 22 -318" fill="none" stroke-width="4"/>')

def szyja(col=SKIN):
    return f'<rect x="-18" y="-330" width="36" height="22" fill="{col}" stroke-width="3"/>'

def ksiadz(pid, rece_pose="stand", hold=""):
    sut = "#1c1c22"
    robe = (f'<path d="M-68 -322 Q-100 -200 -92 -8 L92 -8 Q96 -50 104 -86 C190 -130 196 -268 70 -322 Q0 -342 -68 -322 Z" fill="{sut}"/>'
            f'<path d="M104 -96 C170 -140 176 -250 90 -300" fill="none" stroke="#3a3a46" stroke-width="12" opacity=".9"/>'
            f'<path d="M96 -150 C136 -180 140 -230 110 -262" fill="none" stroke="#5a5a6a" stroke-width="8" opacity=".7"/>'
            + ''.join(f'<circle cx="{4 + (60 if -260 < y < -110 else 0) * math.sin((y + 300) / 200 * math.pi) * .9:.0f}" cy="{y}" r="4" fill="#3a3a44" stroke="none"/>' for y in range(-300, -20, 22))
            + f'<path d="M-30 -8 Q-36 4 -10 6 H26 Q30 -6 22 -8 Z" fill="#0a0a0a"/><path d="M40 -8 Q40 4 66 6 H96 Q100 -6 92 -8 Z" fill="#0a0a0a"/>')
    kolo = (f'<path d="M-34 -330 Q0 -312 34 -330 L32 -312 Q0 -296 -32 -312 Z" fill="{sut}"/><rect x="-12" y="-326" width="24" height="12" rx="2" fill="#fff" stroke-width="3"/>')
    return wrap(pid, robe + szyja("#f4b48a") + kolo + rece(sut, rece_pose, hold, "#f4b48a") + head_ksiadz())

def opiekun(pid, rece_pose="stand", hold=""):
    chusta = (f'<path d="M-40 -324 Q0 -300 40 -324 L10 -236 Q0 -228 -10 -236 Z" fill="#c8302c"/><path d="M-40 -324 Q0 -300 40 -324" fill="none" stroke="#ffd23f" stroke-width="5"/>'
              f'<circle cx="0" cy="-286" r="9" fill="#d8b04a"/>')
    kieszenie = (f'<rect x="-56" y="-284" width="34" height="30" fill="none" stroke-width="3"/><rect x="22" y="-284" width="34" height="30" fill="none" stroke-width="3"/>'
                 f'<path d="M-70 -312 L-40 -316 M70 -312 L40 -316" stroke-width="6"/><rect x="-74" y="-168" width="148" height="16" fill="#5a3a1a"/><rect x="-10" y="-170" width="20" height="20" fill="#d8b04a" stroke-width="3"/>')
    sznurek = '<path d="M-24 -318 Q-30 -250 70 -200" fill="none" stroke="#e8e8e8" stroke-width="3"/>'
    return wrap(pid, nogi(HARC, HARC, "#5a3a1a") + koszulka(HARC) + kieszenie + chusta + sznurek + szyja("#eeb088")
                + rece(HARC, rece_pose, hold, "#eeb088") + head_opiekun())

def listonosz(pid, hold="gazeta"):
    torba = (f'<path d="M-60 -316 L60 -170" stroke="#5a3a1a" stroke-width="12"/><rect x="34" y="-200" width="70" height="62" rx="6" fill="#7a5230"/>'
             f'<path d="M34 -186 H104" stroke-width="3"/>')
    return wrap(pid, nogi("#26407a", "#26407a", "#1a1a1a") + koszulka("#3a5aa0") + torba + szyja("#f0b48a")
                + rece("#3a5aa0", "stand", hold, "#f0b48a") + head_listonosz())

def stiven(pid, rece_pose="stand", hold=""):
    swe = "#efe3c4"
    pas = ''.join(f'<path d="M-68 {y} Q0 {y + 8} 68 {y}" fill="none" stroke="#d8c8a0" stroke-width="4"/>' for y in (-270, -230, -190))
    return wrap(pid, nogi("#2d3a55", "#2d3a55", "#2f4a2a") + koszulka(swe) + pas + szyja("#f2b083") + rece(swe, rece_pose, hold, "#f2b083") + head_stiven_lato())

def syket(pid, pose="stand", rece_pose="stand", hold=""):
    dy = 56 if pose == "sit" else 0
    plecak = '<path d="M-96 -300 Q-112 -220 -96 -170 L-62 -176 L-62 -300 Z" fill="#2a2a2a"/><path d="M-90 -260 H-66" stroke-width="3"/>'
    swoosh = '<path d="M-6 -236 Q20 -222 58 -258 Q30 -232 6 -226 Q-8 -226 -6 -236 Z" fill="#fff" stroke="none"/>'
    body = plecak + koszulka("#d42a2a") + swoosh + szyja() + rece("#d42a2a", rece_pose, hold) + P.head("syket")
    return wrap(pid, nogi("#8a7a5a", "#8a7a5a", "#2a2a2a", pose) + f'<g transform="translate(0,{dy})">{body}</g>')

def andrzej(pid, pose="stand", hold="", rece=None):
    return S22.andrzej(pid, pose=pose, hold=hold, rece=rece)

def triwet(pid, pose="stand", hold="", rece=None):
    return S22.triwet(pid, pose=pose, hold=hold, rece=rece)

# ---------- harcerze (dzieciaki ~12-15 lat) ----------
HAIR = ["#3a2412", "#d8a84a", "#7a4a20", "#1a1a1a", "#b8682a", "#e8c878"]
SKINS = ["#f0ad78", "#f4c09a", "#e8a070", "#f2b88e"]
CHUSTY = ["#c8302c", "#2a6ac8", "#e8b030", "#2a8a4a"]

def glowa_harcerza(v):
    random.seed(100 + v)
    hair, skin = HAIR[v % len(HAIR)], SKINS[v % len(SKINS)]
    dziewczyna = v % 4 == 1
    fr = v % 3
    if dziewczyna:
        wlosy = (f'<path d="M50 160 Q36 30 150 26 Q264 30 250 160 Q240 110 150 100 Q60 110 50 160 Z" fill="{hair}"/>'
                 f'<path d="M50 150 Q20 230 40 300 Q60 310 70 290 Q60 220 70 160 Z" fill="{hair}"/><path d="M250 150 Q280 230 260 300 Q240 310 230 290 Q240 220 230 160 Z" fill="{hair}"/>')
    elif fr == 0:
        wlosy = f'<path d="M54 140 Q48 34 150 30 Q252 34 246 140 Q226 92 186 104 Q170 76 140 98 Q110 80 92 106 Q66 98 54 140 Z" fill="{hair}"/>'
    elif fr == 1:
        wlosy = ''.join(f'<path d="M{x} 110 L{x + 14} 34 L{x + 30} 110 Z" fill="{hair}"/>' for x in range(56, 240, 26)) + f'<path d="M54 120 Q150 70 246 120 L246 100 Q150 50 54 100 Z" fill="{hair}"/>'
    else:
        wlosy = f'<path d="M50 150 Q40 30 150 26 Q260 30 250 150 Q246 120 230 110 Q150 140 70 110 Q54 120 50 150 Z" fill="{hair}"/>'
    piegi = ''.join(f'<circle cx="{x}" cy="{y}" r="3" fill="#c8784a" stroke="none"/>' for x, y in ((96, 210), (110, 220), (190, 214), (204, 206))) if v % 3 == 2 else ''
    return _glowa(f'''<ellipse cx="54" cy="190" rx="16" ry="22" fill="{skin}"/><ellipse cx="246" cy="190" rx="16" ry="22" fill="{skin}"/>
      <path d="M56 160 Q56 54 150 50 Q244 54 244 160 Q244 290 150 300 Q56 290 56 160 Z" fill="{skin}"/>
      <g class="oczyN"><ellipse cx="114" cy="178" rx="13" ry="16" fill="#fff" stroke-width="3"/><ellipse cx="186" cy="178" rx="13" ry="16" fill="#fff" stroke-width="3"/>
      <circle cx="118" cy="180" r="7" fill="{K}" stroke="none"/><circle cx="190" cy="180" r="7" fill="{K}" stroke="none"/></g>
      <path d="M150 196 Q140 222 156 226" fill="none" stroke-width="4"/>{piegi}{usta(150, 252, 24)}{wlosy}''', 150)

def harcerz(pid, v, rece_pose="stand", hold=""):
    skin = SKINS[v % len(SKINS)]
    ch = CHUSTY[v % len(CHUSTY)]
    chusta = f'<path d="M-36 -322 Q0 -302 36 -322 L8 -250 Q0 -244 -8 -250 Z" fill="{ch}"/>'
    return wrap(pid, nogi(HARC if v % 2 else "#4a5a3a", skin, "#3a2a1a") + koszulka(HARC) + chusta + szyja(skin)
                + rece(HARC, rece_pose, hold, skin) + glowa_harcerza(v), "dzieciak")

# ================= POJAZDY =================
def kabina(ludzie=""):
    # kabina Ursusa: tylna szyba, ludzie, rama + przednia szyba na wierzchu
    return (f'<g class="kabina">'
            f'<path d="M-196 -330 L-196 -650 L150 -650 L150 -330 Z" fill="#9ac4dc" fill-opacity=".35" stroke="none"/>'
            f'{ludzie}'
            f'<g {OL}><path d="M-196 -330 V-650 M150 -330 L150 -650 M-30 -330 V-650" stroke-width="16" fill="none"/>'
            f'<path d="M-196 -330 V-650 M150 -330 L150 -650 M-30 -330 V-650" stroke="{S21.RED}" stroke-width="8" fill="none"/>'
            f'<rect x="-214" y="-680" width="384" height="36" rx="8" fill="{S21.RED}"/><rect x="-214" y="-680" width="384" height="10" fill="#e85a50" stroke="none"/>'
            f'<path d="M-196 -650 H150" stroke-width="6"/></g>'
            f'<path d="M-196 -330 L-196 -650 L150 -650 L150 -330 Z" fill="url(#szyba)" stroke="none"/>'
            f'<path d="M-150 -400 L-90 -620 M-120 -400 L-70 -580 M40 -420 L100 -630" stroke="#fff" stroke-width="7" opacity=".45"/>'
            f'<path d="M-196 -490 L-110 -490" stroke="{K}" stroke-width="4" opacity=".5"/></g>')

def traktor(tid, x, y, s, ludzie="", beczka_svg=""):
    t = S21.c330(tid, driver=False)
    i = t.index('<g class="kR"')
    t = t[:i] + kabina(ludzie) + t[i:]
    return f'<g id="{tid}W" transform="translate({x},{y}) scale({s})">{beczka_svg}{t}</g>'

def w_kabinie(pref):
    # Triwet za kierownica, SYKET wcisniety obok (z tylu)
    return (g(pref + "S", -130, -250, .74, syket(pref + "SP", pose="sit"))
            + g(pref + "R", -40, -262, .8, triwet(pref + "RP", pose="sit", rece="stand")))

def beczka(bid, **kw):
    kw.setdefault("malowana", True); kw.setdefault("napis", True)
    return S22.beczka(bid, -720, 0, 1.0, **kw)

def muchy(mid, x, y, n=6, r=60):
    random.seed(len(mid) * 7 + n)
    return (f'<g id="{mid}" class="muchy" transform="translate({x},{y})">'
            + ''.join(f'<g class="mucha" style="transform-origin:0px 0px"><g transform="translate({random.randint(-r, r)},{random.randint(-r // 2, r // 2)})">'
                      f'<ellipse cx="0" cy="0" rx="7" ry="5" fill="#1a1a1a"/><ellipse cx="-3" cy="-6" rx="6" ry="4" fill="#dfe8f0" opacity=".8"/>'
                      f'<ellipse cx="4" cy="-6" rx="6" ry="4" fill="#dfe8f0" opacity=".8"/></g></g>' for _ in range(n)) + '</g>')

# ================= OTOCZENIE =================
niebo, chmura, drzewo = S22.niebo, S22.chmura, S22.drzewo

def sosna(x, y, h, col="#2f5a3a"):
    return (f'<g {OL}><path d="M{x} {y} V{y - h * .3}" stroke-width="16"/><path d="M{x} {y} V{y - h * .3}" stroke="#6b4a2a" stroke-width="9"/>'
            f'<path d="M{x - h * .28} {y - h * .25} L{x} {y - h} L{x + h * .28} {y - h * .25} Z" fill="{col}"/>'
            f'<path d="M{x - h * .22} {y - h * .5} L{x} {y - h * 1.05} L{x + h * .22} {y - h * .5}" fill="none" stroke-width="3" opacity=".5"/></g>')

def plebania():
    return f'''<rect x="-200" y="0" width="1010" height="900" fill="#f0e2c0"/>
      <g {OL}><rect x="80" y="180" width="240" height="300" fill="#bfe0f2"/><path d="M200 180 V480 M80 330 H320" stroke-width="10"/>
      <path d="M120 470 L150 360 L180 470 Z" fill="#e8e4dc" opacity=".8"/><path d="M150 360 V340 M140 350 H160" stroke-width="4"/>
      <rect x="470" y="150" width="20" height="120" fill="#8a5a2a"/><rect x="440" y="180" width="80" height="20" fill="#8a5a2a"/>
      <rect x="560" y="220" width="160" height="200" fill="#d8b04a"/><rect x="574" y="234" width="132" height="172" fill="#7a9ad8"/>
      <circle cx="640" cy="300" r="34" fill="#f4b48a"/><path d="M600 406 Q640 340 680 406 Z" fill="#fff"/>
      <rect x="-200" y="700" width="1010" height="200" fill="#9a6a3a"/>
      <rect x="-60" y="610" width="760" height="40" fill="#7a4a24"/><path d="M-30 650 V760 M670 650 V760" stroke-width="22"/><path d="M-30 650 V760 M670 650 V760" stroke="#7a4a24" stroke-width="14"/>
      <ellipse cx="80" cy="600" rx="90" ry="20" fill="#fbfbf6"/><path d="M20 596 Q60 560 120 590 Q140 580 150 596 Z" fill="#c8783a"/>
      <path d="M40 588 Q80 576 130 588" stroke="#f2c230" stroke-width="5" fill="none"/>
      <rect x="200" y="540" width="40" height="70" rx="6" fill="#7a2a3a"/><rect x="208" y="526" width="24" height="18" fill="#7a2a3a"/>
      <rect x="260" y="560" width="60" height="50" rx="8" fill="#e8d8b8"/><path d="M320 572 Q338 584 320 596" fill="none" stroke-width="5"/></g>'''

def lawka(x, y):
    return (f'<g {OL}><rect x="{x}" y="{y - 70}" width="300" height="20" fill="#8a5a2a"/><rect x="{x}" y="{y - 140}" width="300" height="18" fill="#8a5a2a"/>'
            f'<path d="M{x + 20} {y - 50} V{y} M{x + 280} {y - 50} V{y}" stroke-width="14"/></g>')

def sh_telefon():
    # ekran dzielony: ksiadz (plebania) | Andrzej i Triwet na lawce przed domem
    return f'''<g>{plebania()}{g("kTel", 400, 925, 1.0, ksiadz("kTelP", "ucho"))}</g>
      <g><rect x="810" y="0" width="1000" height="900" fill="url(#skyLato)"/>{chmura(1300, 220, .8)}
      <g transform="translate(560,120) scale(.75)">{S22.dom_ze_zdjecia()}</g>
      <rect x="810" y="620" width="1000" height="300" fill="#7ab05a"/>
      <g transform="translate(940,760) scale(1.1)">{lawka(0, 0)}</g>
      {g("aTel", 1050, 820, .95, andrzej("aTelP", pose="sit", hold="telefon"))}
      {g("rTel", 1290, 820, .95, triwet("rTelP", pose="sit"))}
      <g transform="translate(1460,770)" {OL}><rect x="0" y="-60" width="28" height="60" rx="5" fill="#2e7d32"/><rect x="0" y="-48" width="28" height="18" fill="#ffd23f" stroke-width="2"/></g></g>
      <path d="M810 0 V900" stroke="{K}" stroke-width="14"/>'''

def stodola(x=1050):
    return f'''<g {OL}><rect x="{x}" y="250" width="520" height="420" fill="#8a3a2a"/><path d="M{x - 30} 260 L{x + 260} 120 L{x + 550} 260 Z" fill="#5a5f66"/>
      <rect x="{x + 130}" y="400" width="260" height="270" fill="#6a2a1a"/><path d="M{x + 130} 400 L{x + 390} 670 M{x + 390} 400 L{x + 130} 670" stroke-width="6"/></g>'''

def kran(x, y):
    return (f'<g {OL}><rect x="{x}" y="{y - 120}" width="30" height="120" fill="#8a8e94"/><path d="M{x + 30} {y - 110} H{x + 70} V{y - 90}" fill="none" stroke-width="14"/>'
            f'<path d="M{x + 30} {y - 110} H{x + 70} V{y - 90}" fill="none" stroke="#c9ced6" stroke-width="8"/><circle cx="{x + 46}" cy="{y - 124}" r="10" fill="#c81e1e"/></g>')

def sh_podworko():
    return (niebo() + '<rect x="-400" y="640" width="2400" height="300" fill="#7ab05a"/>' + stodola() + drzewo(140, 650, 320)
            + kran(980, 680)
            + traktor("trPod", 1300, 760, .55)
            + f'<g id="bPodW" transform="translate(560,740) scale(.62)">{S22.beczka("bPod", 0, 0, 1.0, malowana=True, napis=True)}</g>'
            + muchy("muPod", 740, 560, 7, 120)
            + g("uPod", 260, 790, .62, stiven("uPodP"))
            + g("rPod", 420, 800, .62, triwet("rPodP"), ' style="transform:translate(420px,800px) scale(-.62,.62)"')
            + g("sPod", 540, 800, .62, syket("sPodP"), ' style="transform:translate(540px,800px) scale(-.62,.62)"'))

def trzciny(x0, x1, y):
    random.seed(x0)
    return ''.join(f'<path d="M{x} {y} Q{x + random.randint(-12, 12)} {y - 60} {x + random.randint(-20, 20)} {y - random.randint(80, 130)}" fill="none" stroke="#4a7a3a" stroke-width="6"/>'
                   for x in range(x0, x1, 18))

def sh_rzeka():
    fale = ''.join(f'<path d="M{x} {y} q20 -8 40 0" fill="none" stroke="#bfe8e0" stroke-width="4"/>' for x, y in ((200, 680), (420, 720), (700, 700), (980, 740), (300, 780)))
    return (niebo() + '<rect x="-400" y="430" width="2400" height="90" fill="#6aa84a"/>'
            + ''.join(drzewo(x, 470, 170, "#4a8a3a") for x in (-100, 160, 420, 700, 980, 1240, 1500))
            + f'<rect x="-400" y="510" width="1700" height="400" fill="url(#rzeka)"/>{fale}'
            + '<g id="wir"><ellipse cx="900" cy="720" rx="40" ry="10" fill="none" stroke="#bfe8e0" stroke-width="4"/></g>'
            + f'<path d="M1100 560 Q1250 540 1300 600 L2000 600 V900 H1000 Q980 700 1100 560 Z" fill="#7ab05a" {OL}/>'
            + trzciny(980, 1140, 640)
            + traktor("trRz", 1880, 760, .5, ludzie=g("rRzR", -40, -262, .8, triwet("rRzRP", pose="sit", rece="stand")), beczka_svg=beczka("bRz"))
            + f'<path id="wazRz" d="M1520 700 Q1300 660 1200 720 Q1060 790 920 730" fill="none" stroke="#1a1a1a" stroke-width="20"/>'
            + f'<path d="M1520 700 Q1300 660 1200 720 Q1060 790 920 730" fill="none" stroke="#3a3f48" stroke-width="13"/>'
            + g("sRz", 1180, 780, .5, syket("sRzP"), ' style="transform:translate(1180px,780px) scale(-.5,.5)"')
            + '<g id="zaba" style="display:none"><g transform="translate(860,700)" ' + OL + '><ellipse cx="0" cy="0" rx="34" ry="20" fill="#5aa83a"/>'
              '<circle cx="-16" cy="-18" r="10" fill="#5aa83a"/><circle cx="16" cy="-18" r="10" fill="#5aa83a"/><circle cx="-16" cy="-20" r="4" fill="#141414"/><circle cx="16" cy="-20" r="4" fill="#141414"/>'
              '<path d="M-14 4 Q0 12 14 4" fill="none" stroke-width="3"/></g></g>')

def sh_las():
    random.seed(11)
    tyl = ''.join(sosna(x, 620, random.randint(300, 420), "#2a4a30") for x in range(-300, 4200, 120))
    przod = ''.join(f'<g {OL}><rect x="{x}" y="-100" width="70" height="1000" fill="#4a3220"/><path d="M{x + 20} 100 V800" stroke="#3a2414" stroke-width="5"/></g>' for x in range(-200, 5200, 640))
    galaz = ''.join(f'<path d="M{x} 300 Q{x + 140} 330 {x + 300} 290" fill="none" stroke="#4a3220" stroke-width="14"/>'
                    f'<ellipse cx="{x + 260}" cy="300" rx="70" ry="34" fill="#3a6a32" {OL}/>' for x in range(0, 4200, 900))
    return (f'<rect x="-400" y="-200" width="2400" height="1300" fill="#a8c8a0"/>'
            + f'<g id="lasTyl">{tyl}{galaz}</g>'
            + '<rect x="-400" y="620" width="2400" height="300" fill="#3a5a2a"/>'
            + '<path d="M-400 700 H2000 V790 H-400 Z" fill="#9a7a4a"/><path d="M-400 720 H2000 M-400 770 H2000" stroke="#7a5a32" stroke-width="6" stroke-dasharray="40 30"/>'
            + traktor("trLas", 560, 760, .5, ludzie=w_kabinie("las"), beczka_svg=beczka("bLas"))
            + f'<g id="lasPrzod" style="filter:url(#mblur)">{przod}</g>')

def sh_kabina():
    # widok przez przednia szybe: Triwet za kierownica, SYKET przycisniety do bocznej szyby
    return f'''<rect x="-200" y="-200" width="2000" height="1300" fill="#2a4a2a"/>
      <g id="kabLiscie">{''.join(f'<ellipse cx="{x}" cy="{y}" rx="90" ry="40" fill="#3a7a32" {OL}/>' for x, y in ((200, 250), (600, 200), (1100, 260), (1400, 220), (900, 300)))}</g>
      <rect x="200" y="160" width="1200" height="620" fill="#c8a07a" opacity=".25"/>
      {g("kabR", 640, 990, 1.4, triwet("kabRP", pose="sit", rece="stand"))}
      {g("kabS", 1060, 970, 1.4, syket("kabSP", pose="sit"), ' style="transform:translate(1060px,970px) scale(1.25,1.4)"')}
      <g {OL}><circle cx="700" cy="760" r="150" fill="none" stroke-width="30"/><circle cx="700" cy="760" r="150" fill="none" stroke="#2a2a2a" stroke-width="20"/>
      <path d="M700 760 L700 900 M700 760 L560 800 M700 760 L840 800" stroke-width="20"/><rect x="100" y="790" width="1400" height="120" fill="#3a3f48"/></g>
      <rect x="160" y="140" width="1280" height="660" fill="url(#szyba)" stroke="{S21.RED}" stroke-width="40"/>
      <rect x="160" y="140" width="1280" height="660" fill="none" stroke="{K}" stroke-width="6"/>
      <path d="M1340 160 V780" stroke="{S21.RED}" stroke-width="30"/>
      <path d="M300 640 L500 200 M380 660 L560 260" stroke="#fff" stroke-width="12" opacity=".35"/>
      <g id="galazUderz" style="display:none"><path d="M-300 300 Q300 340 900 260" fill="none" stroke="#4a3220" stroke-width="30" {OL}/>
        {''.join(f'<ellipse cx="{x}" cy="{y}" rx="80" ry="34" fill="#3a7a32" {OL}/>' for x, y in ((200, 300), (500, 330), (800, 270), (0, 300)))}</g>'''

def brama():
    return (f'<g {OL}><path d="M-60 780 V380 M260 780 V380" stroke-width="30"/><path d="M-60 780 V380 M260 780 V380" stroke="#8a5a2a" stroke-width="20"/>'
            f'<rect x="-100" y="380" width="400" height="76" fill="#a8783e"/>'
            f'<text x="100" y="432" text-anchor="middle" font-family="Georgia, serif" font-size="40" font-weight="700" fill="#3a2410" stroke="none">OBÓZ</text>'
            f'<path d="M100 330 L70 380 H130 Z" fill="#3a6a2a"/><path d="M80 350 L100 316 L120 350" fill="#4a8a3a"/></g>')

def namiot(x, y, col, w=260, h=200):
    return (f'<g {OL}><path d="M{x} {y} L{x + w / 2} {y - h} L{x + w} {y} Z" fill="{col}"/>'
            f'<path d="M{x + w / 2} {y - h} L{x + w / 2 - 30} {y} L{x + w / 2 + 30} {y} Z" fill="#1a1a1a" opacity=".55"/>'
            f'<path d="M{x + w / 2} {y - h} V{y - h - 30}" stroke-width="6"/><path d="M{x} {y} L{x - 40} {y + 10} M{x + w} {y} L{x + w + 40} {y + 10}" stroke-width="3"/></g>')

def wanna(x, y, s=1.0):
    return f'''<g id="wanna" transform="translate({x},{y}) scale({s})">
      <g {OL}><path d="M-110 -10 L-120 20 M110 -10 L120 20" stroke-width="14"/>
      <path d="M-160 -150 H160 Q160 -10 90 -10 H-90 Q-160 -10 -160 -150 Z" fill="url(#emalia)"/>
      <ellipse cx="0" cy="-150" rx="164" ry="22" fill="#e8eef2"/></g>
      <defs><clipPath id="wannaClip"><ellipse cx="0" cy="-150" rx="150" ry="16"/></clipPath></defs>
      <g clip-path="url(#wannaClip)"><rect id="wannaWoda" x="-170" y="-150" width="340" height="40" fill="{MET}" opacity="0"/></g>
      <g id="smrod" fill="none" stroke="#8ab83a" stroke-width="7" stroke-linecap="round" opacity="0">
        <path d="M-80 -170 q-24 -20 0 -40 q24 -20 0 -40 q-24 -20 0 -40"/><path d="M0 -180 q-24 -20 0 -40 q24 -20 0 -40 q-24 -20 0 -40 q24 -20 0 -40"/>
        <path d="M80 -170 q-24 -20 0 -40 q24 -20 0 -40 q-24 -20 0 -40"/></g>
      <g {OL}><rect x="-210" y="-120" width="12" height="120" fill="#8a5a2a"/><rect x="-224" y="-130" width="40" height="20" rx="6" fill="#fbfbf6"/>
      <rect x="-236" y="-100" width="64" height="70" fill="#e85a7a"/></g></g>'''

def maszt(x, y):
    return (f'<g {OL}><path d="M{x} {y} V{y - 420}" stroke-width="12"/><path d="M{x} {y} V{y - 420}" stroke="#d8d8d8" stroke-width="6"/>'
            f'<g id="flaga" style="transform-origin:{x}px {y - 410}px"><rect x="{x + 4}" y="{y - 410}" width="130" height="40" fill="#fff"/><rect x="{x + 4}" y="{y - 370}" width="130" height="40" fill="#d42a2a"/></g></g>')

def siatka(x, y):
    return (f'<g {OL}><path d="M{x} {y} V{y - 260}" stroke-width="12"/><rect x="{x - 6}" y="{y - 260}" width="12" height="110" fill="#fff" stroke-width="2"/>'
            f'<path d="M{x} {y - 260} V{y - 150}" stroke="#1a1a1a" stroke-width="2"/>'
            + ''.join(f'<path d="M{x - 3} {yy} H{x + 3}" stroke-width="2"/>' for yy in range(y - 250, y - 150, 12))
            + f'</g><circle id="pilka" cx="{x}" cy="{y - 380}" r="22" fill="#fbfbf6" {OL}/>')

def ognisko(x, y, s=.6):
    return (S21.flames(x, y, s, "ognisko")
            + f'<g {OL}><rect x="{x - 200}" y="{y + 6}" width="120" height="30" rx="14" fill="#7a4a24"/><rect x="{x + 80}" y="{y + 6}" width="120" height="30" rx="14" fill="#7a4a24"/></g>')

# rozmieszczenie 20 harcerzy na lace: (x, y, czynnosc)
HARCERZE = [
    (180, 640, ""), (560, 640, "machaj"), (900, 650, ""), (1400, 655, ""), (1560, 650, "machaj"),      # z tylu: namioty, maszt
    (1460, 800, ""), (1520, 840, "machaj"), (1700, 835, ""), (1780, 800, ""), (1610, 870, ""),          # przy ognisku
    (1980, 790, "machaj"), (2060, 800, ""), (2140, 790, "machaj"),                                      # siatkowka lewa
    (2340, 790, "machaj"), (2420, 800, ""), (2500, 790, ""),                                            # siatkowka prawa
    (2620, 820, ""), (2260, 860, ""), (1880, 860, ""), (1420, 880, ""),
]
KOLEJKA_X0, KOLEJKA_DX, KOLEJKA_Y = 360, -58, 830

def sh_oboz():
    out = ('<rect x="-1200" y="-300" width="5200" height="1200" fill="url(#skyLato)"/>' + niebo() + chmura(2300, 200, 1.2) + chmura(2900, 260, .9)
           + '<rect x="-400" y="430" width="3400" height="60" fill="#6aa84a"/>'
           + ''.join(drzewo(x, 460, 180, "#4a8a3a") for x in range(-300, 3200, 260))
           + '<rect x="-400" y="470" width="3400" height="80" fill="url(#rzeka)"/>'
           + ''.join(f'<path d="M{x} 510 q20 -8 40 0" fill="none" stroke="#bfe8e0" stroke-width="4"/>' for x in range(-300, 3200, 210))
           + '<rect x="-400" y="545" width="3400" height="400" fill="#86bc5a"/>'
           + ''.join(f'<path d="M{x} {y} l6 -18 l6 18" fill="none" stroke="#5a9a3a" stroke-width="3"/>' for x, y in ((random.seed(5) or 0) and [] or [(random.randint(-300, 3100), random.randint(580, 880)) for _ in range(90)]))
           + namiot(60, 660, "#3a7a3a") + namiot(380, 650, "#d87a2a", 240, 190) + namiot(700, 660, "#3a5aa0", 250, 200)
           + maszt(1480, 690)
           + g("brama", -260, 0, 1.0, brama())
           + ognisko(1600, 780) + siatka(2240, 800)
           + wanna(420, 800, .9))
    dz = lambda back: ''.join(g(f"hk{i}", x, y, .4, harcerz(f"hk{i}P", i, pose)) for i, (x, y, pose) in enumerate(HARCERZE) if (y < 700) == back)
    flaszka = (f'<g id="flaszkaLot" style="display:none"><g {OL}><rect x="-14" y="-31" width="28" height="62" rx="6" fill="#e8f4f8"/>'
               f'<rect x="-7" y="-55" width="14" height="26" fill="#e8f4f8"/><rect x="-8" y="-61" width="16" height="8" fill="#c81e1e"/><rect x="-14" y="-11" width="28" height="22" fill="#fff" stroke-width="2"/></g></g>')
    return (out + dz(True)
            + traktor("trOb", -1100, 780, .5, ludzie=w_kabinie("ob"), beczka_svg=beczka("bOb"))
            + '<path id="wazOb" d="M0 0" fill="none" stroke="#1a1a1a" stroke-width="16" style="display:none"/>'
            + f'<path id="strumien" d="M0 0" fill="none" stroke="{MET}" stroke-width="12" stroke-linecap="round" style="display:none"/>'
            + muchy("muOb", 420, 600, 6, 90)
            + g("oOb", 260, 800, .62, opiekun("oObP", hold="gwizdek"))
            + dz(False) + flaszka)

def sh_droga():
    return (niebo() + S22.kosciol(1000, 620, .9)
            + '<rect x="-400" y="620" width="2400" height="80" fill="#7ab05a"/><rect x="-400" y="700" width="2400" height="200" fill="#8a8e94"/>'
            + g("kDr", 1250, 690, .5, ksiadz("kDrP", "kciuk"))
            + traktor("trDr", -900, 830, .5, ludzie=w_kabinie("dr"), beczka_svg=beczka("bDr")))

def sh_ksiadz_cu():
    return (f'<rect x="-200" y="-200" width="2000" height="1300" fill="url(#skyLato)"/>{chmura(400, 260, 1.2)}'
            + S22.kosciol(1300, 900, 1.3)
            + g("kCu", 760, 980, 1.6, ksiadz("kCuP", "kciuk"))
            + '<g id="blysk" style="display:none"><path d="M0 -60 L12 -12 L60 0 L12 12 L0 60 L-12 12 L-60 0 L-12 -12 Z" fill="#fff6a0" stroke="#141414" stroke-width="4"/></g>')

def dom_stivena():
    return f'''<g {OL}><rect x="80" y="330" width="560" height="340" fill="#e8dcc0"/><path d="M50 340 L360 150 L670 340 Z" fill="#8a4428"/>
      <rect x="140" y="420" width="110" height="110" fill="#bfe0f2"/><path d="M195 420 V530 M140 475 H250" stroke-width="6"/>
      <rect x="320" y="470" width="110" height="200" fill="#7a4a2a"/><circle cx="410" cy="570" r="7" fill="#d8b04a"/>
      <rect x="480" y="420" width="110" height="110" fill="#bfe0f2"/><path d="M535 420 V530 M480 475 H590" stroke-width="6"/>
      <rect x="290" y="660" width="170" height="24" fill="#b8b0a0"/></g>'''

def sh_rano():
    return (f'<rect x="-400" y="-200" width="2400" height="1300" fill="url(#skyRano)"/><circle cx="1400" cy="380" r="70" fill="#ffe27a" stroke="#141414" stroke-width="5"/>'
            + '<rect x="-400" y="640" width="2400" height="300" fill="#7ab05a"/>' + dom_stivena() + stodola(1150)
            + f'<g id="bRanoW" transform="translate(760,760) scale(.62)">{S22.beczka("bRano", 0, 0, 1.0, malowana=True, napis=True)}</g>'
            + muchy("muRano", 940, 580, 8, 120)
            + f'<g id="kogut" transform="translate(130,690)" {OL}><ellipse cx="0" cy="-40" rx="44" ry="34" fill="#c8783a"/><circle cx="34" cy="-80" r="20" fill="#c8783a"/>'
              f'<path d="M26 -100 l6 -14 l6 12 l6 -12 l4 16" fill="#d42a2a"/><path d="M54 -80 L70 -74 L54 -70 Z" fill="#f2c230"/><circle cx="38" cy="-84" r="4" fill="#141414"/>'
              f'<path d="M-44 -50 Q-90 -100 -60 -120 Q-60 -80 -36 -66" fill="#2a6a3a"/><path d="M-6 -8 V0 M10 -8 V0" stroke-width="5"/></g>'
            + g("uRano", 380, 780, .62, stiven("uRanoP", hold="kubek"))
            + g("lRano", 1900, 790, .62, listonosz("lRanoP"), ' style="transform:translate(1900px,790px) scale(-.62,.62)"'))

def sh_gazeta():
    tekst = lambda x, y, w, n: ''.join(f'<rect x="{x}" y="{y + i * 22}" width="{w - (60 if i % 4 == 3 else 0)}" height="9" fill="#9a9a94"/>' for i in range(n))
    return f'''<rect x="-200" y="-200" width="2000" height="1300" fill="#7ab05a"/>
      <g id="gazetaG" transform="rotate(-3 800 470)">
      <rect x="250" y="120" width="1100" height="720" fill="#f2efe4" stroke="#141414" stroke-width="6"/>
      <text x="800" y="200" text-anchor="middle" font-family="Georgia, serif" font-size="64" font-weight="700" fill="#141414">KURIER ZNAD RZEKI</text>
      <path d="M290 222 H1310 M290 232 H1310" stroke="#141414" stroke-width="4"/>
      <text x="800" y="300" text-anchor="middle" font-family="Arial Black, Impact, sans-serif" font-size="58" fill="#c81e1e">ZATRUCIE NA OBOZIE HARCERSKIM!</text>
      <text x="800" y="350" text-anchor="middle" font-family="Georgia, serif" font-size="30" font-style="italic" fill="#141414">Salmonella i bakterie coli w „wodzie mineralnej”</text>
      <rect x="300" y="380" width="460" height="320" fill="#d8d4c8" stroke="#141414" stroke-width="4"/>
      <g transform="translate(330,640) scale(.5)">{S22.beczka("bGaz", 0, 0, 1.0, malowana=True, napis=True)}</g>
      <g transform="translate(680,690) scale(.34)">{harcerz("gazH", 2)}</g>
      <rect x="300" y="380" width="460" height="320" fill="#8a8070" opacity=".25"/>
      <text x="530" y="730" text-anchor="middle" font-family="Georgia, serif" font-size="20" font-style="italic" fill="#3a3a3a">Sanepid szuka niebieskiej beczki z napisem WODA PITNA</text>
      {tekst(800, 390, 500, 14)}{tekst(300, 760, 1000, 3)}</g>'''

def sh_beczka_cu():
    return (f'<rect x="-400" y="-200" width="2400" height="1300" fill="url(#skyRano)"/><rect x="-400" y="640" width="2400" height="300" fill="#7ab05a"/>'
            + f'<g transform="translate(260,860) scale(1.6)">{S22.beczka("bCu", 0, 0, 1.0, malowana=True, napis=True)}</g>' + muchy("muCu", 800, 440, 10, 260))

SHOTS = [("shTelefon", sh_telefon()), ("shPodworko", sh_podworko()), ("shRzeka", sh_rzeka()), ("shLas", sh_las()), ("shKabina", sh_kabina()),
         ("shOboz", sh_oboz()), ("shWajcha", S22.sh_wajcha()), ("shDroga", sh_droga()), ("shKsiadzCu", sh_ksiadz_cu()),
         ("shRano", sh_rano()), ("shGazeta", sh_gazeta()), ("shBeczkaCu", sh_beczka_cu())]

WHO_JS = '''  const who = {
    a: { el: "aTelP", vPitch: 0.8, vRate: 1.2 },
    r: { el: "rTelP", vPitch: 0.95, vRate: 1.2 },
    s: { el: "sPodP", vPitch: 1.2, vRate: 1.2 },
    u: { el: "uPodP", vPitch: 0.7, vRate: 1.15 },
    k: { el: "kTelP", vPitch: 0.6, vRate: 1.05 },
    o: { el: "oObP", vPitch: 1.0, vRate: 1.2 },
    h: { el: "hk0P", vPitch: 1.6, vRate: 1.25 },
    l: { el: "lRanoP", vPitch: 0.9, vRate: 1.2 }
  };
'''

SHOTS_SVG = '\n'.join(f'    <g class="shot" id="{i}" style="display:none">{svg}</g>' for i, svg in SHOTS)

# podglad postaci: python3 ep24_sceny.py -> ep24_postacie_test.html
if __name__ == "__main__":
    items = [ksiadz("k"), ksiadz("k2", "kciuk"), opiekun("o", hold="gwizdek"), listonosz("l"), stiven("u", hold="kubek"), syket("s"),
             andrzej("a"), triwet("t")] + [harcerz(f"h{i}", i) for i in range(6)]
    gg = ''.join(f'<g transform="translate({120 + (i % 7) * 220},{520 + (i // 7) * 520}) scale(.9)">{s}</g>' for i, s in enumerate(items))
    trak = traktor("tt", 600, 1500, .7, ludzie=w_kabinie("tt"), beczka_svg=beczka("btt"))
    open(B + 'ep24_postacie_test.html', 'w', encoding='utf-8').write(
        f'<!doctype html><meta charset="utf-8"><body style="margin:0;background:#cfe3f0"><svg viewBox="0 0 1600 1600" width="1600" height="1600"><defs>{DEFS}</defs>{gg}{trak}</svg></body>')
    print("ok")
