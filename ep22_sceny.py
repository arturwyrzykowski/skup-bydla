# Odcinek 22 "Woda pitna": ujecia (kazde = <g class="shot" id="sh...">, 1600x900, kadr widoczny y 114..786)
import importlib, math, random, sys
B = '/Users/arturwyrzykowski/Programowanie/bajka/'
sys.path.insert(0, B)
import ep21_postacie as P; importlib.reload(P)
import ep21_sceny as S21
K = "#141414"
SKIN = P.SKIN
OL = f'stroke="{K}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"'
RED, RED_D = S21.RED, S21.RED_D
BRAZ, BRAZ_D = "#6b4a1e", "#4a3210"

DEFS = '''    <linearGradient id="skyLato" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5aa2e6"/><stop offset="1" stop-color="#cfe8fb"/></linearGradient>
    <linearGradient id="woda" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a9ad8"/><stop offset="1" stop-color="#2a6aa8"/></linearGradient>
    <linearGradient id="beczkaG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a6a44"/><stop offset=".5" stop-color="#6b4f30"/><stop offset="1" stop-color="#4a3420"/></linearGradient>
    <linearGradient id="niebG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a8ae0"/><stop offset=".5" stop-color="#1f66c0"/><stop offset="1" stop-color="#174a8a"/></linearGradient>
    <linearGradient id="kafle" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e8eef2"/><stop offset="1" stop-color="#c8d4dc"/></linearGradient>
    <radialGradient id="szamboG" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#9aa0a6"/><stop offset="1" stop-color="#5a6066"/></radialGradient>
'''

def g(pid, x, y, s, inner, extra=''):
    return f'<g id="{pid}W" transform="translate({x},{y}) scale({s})"{extra}>{inner}</g>'

# ---------- postacie w letnich ciuchach (stopy w 0,0, przodem w prawo) ----------
def tee(col):
    return (f'<path d="M-70 -312 Q-84 -230 -72 -150 L72 -150 Q84 -230 70 -312 Q0 -330 -70 -312 Z" fill="{col}"/>'
            f'<path d="M-22 -318 Q0 -300 22 -318" fill="none" stroke-width="4"/>')

def nogi_lato(spodenki, buty="#2a2a2a", pose="stand"):
    if pose == "sit":
        return (f'<path d="M-34 -106 L70 -100" stroke-width="50"/><path d="M-34 -106 L70 -100" stroke="{spodenki}" stroke-width="40"/>'
                f'<path d="M70 -100 L76 -34" stroke-width="40"/><path d="M70 -100 L76 -34" stroke="{SKIN}" stroke-width="30"/>'
                f'<path d="M52 -40 Q46 -2 66 0 H112 Q116 -22 98 -40 Z" fill="{buty}"/>')
    noga = lambda sx, cls, o: (f'<g class="{cls}" style="transform-origin:{o}px -150px"><path d="M{o} -170 L{o + sx * 2} -30" stroke-width="44"/>'
                               f'<path d="M{o} -170 L{o + sx} -96" stroke="{spodenki}" stroke-width="40"/><path d="M{o + sx} -96 L{o + sx * 2} -34" stroke="{SKIN}" stroke-width="30"/>'
                               f'<path d="M{o - 34 if sx < 0 else o - 28} -40 Q{o - 38 if sx < 0 else o - 30} -2 {o - 16 if sx < 0 else o - 24} 0 H{o + 30 if sx < 0 else o + 40} Q{o + 34 if sx < 0 else o + 40} -22 {o + 26 if sx < 0 else o + 32} -40 Z" fill="{buty}"/></g>')
    return noga(-1, "legL", -24) + noga(1, "legR", 24)

def rece_lato(kol, pose="stand", hold=""):
    item = {
        "telefon": f'<g class="telefon"><rect x="64" y="-206" width="26" height="46" rx="5" fill="#1a1a1a" stroke-width="3"/><rect x="68" y="-200" width="18" height="32" fill="#4a8ad8" stroke="none"/></g>',
        "farba": (f'<g class="farba"><rect x="56" y="-186" width="56" height="56" rx="4" fill="#d8dce2" stroke-width="4"/><rect x="56" y="-170" width="56" height="26" fill="#1f66c0" stroke-width="3"/>'
                  f'<path d="M58 -186 Q84 -210 110 -186" fill="none" stroke-width="4"/><path d="M60 -128 Q64 -112 70 -128" fill="#1f66c0" stroke="none"/></g>'),
        "pedzel": f'<g class="pedzel"><path d="M82 -176 L140 -250" stroke="#8a5a2a" stroke-width="8"/><rect x="132" y="-284" width="22" height="34" rx="3" fill="#1f66c0" stroke-width="3" transform="rotate(38 143 -267)"/></g>',
        "waz": f'<g class="wazR"><path d="M82 -168 Q130 -120 120 -40" fill="none" stroke="#1a1a1a" stroke-width="22"/><path d="M82 -168 Q130 -120 120 -40" fill="none" stroke="#3a3f48" stroke-width="14"/></g>',
    }.get(hold, '')
    if pose == "ucho":   # telefon przy uchu
        return (f'<path d="M-62 -296 Q-86 -220 -78 -160" fill="none" stroke-width="34"/><path d="M-62 -260 Q-84 -210 -78 -160" fill="none" stroke="{SKIN}" stroke-width="24"/>'
                f'<path d="M-62 -296 Q-70 -276 -66 -258" fill="none" stroke="{kol}" stroke-width="30"/><circle cx="-78" cy="-152" r="16" fill="{SKIN}"/>'
                f'<g class="armR"><path d="M62 -296 Q120 -260 96 -360" fill="none" stroke-width="34"/><path d="M80 -280 Q118 -262 96 -360" fill="none" stroke="{SKIN}" stroke-width="24"/>'
                f'<path d="M62 -296 Q74 -290 84 -280" fill="none" stroke="{kol}" stroke-width="30"/>'
                f'<rect x="78" y="-406" width="26" height="50" rx="5" fill="#1a1a1a" stroke-width="3"/><circle cx="96" cy="-362" r="16" fill="{SKIN}"/></g>')
    if pose == "waz":    # trzyma waz oburacz przed soba (w dol do dekla)
        return (f'<path d="M-62 -296 Q-20 -230 40 -200" fill="none" stroke-width="34"/><path d="M-40 -260 Q-10 -224 40 -200" fill="none" stroke="{SKIN}" stroke-width="24"/>'
                f'<path d="M-62 -296 Q-52 -280 -42 -262" fill="none" stroke="{kol}" stroke-width="30"/>'
                f'<path d="M62 -296 Q90 -240 70 -196" fill="none" stroke-width="34"/><path d="M74 -270 Q88 -236 70 -196" fill="none" stroke="{SKIN}" stroke-width="24"/>'
                f'<path d="M62 -296 Q68 -286 74 -272" fill="none" stroke="{kol}" stroke-width="30"/>'
                f'<path d="M30 -200 Q120 -170 150 -60 L160 0" fill="none" stroke="#1a1a1a" stroke-width="26"/><path d="M30 -200 Q120 -170 150 -60 L160 0" fill="none" stroke="#3a3f48" stroke-width="18"/>'
                f'<circle cx="44" cy="-200" r="16" fill="{SKIN}"/><circle cx="70" cy="-192" r="16" fill="{SKIN}"/>')
    return (f'<path d="M-62 -296 Q-86 -220 -78 -160" fill="none" stroke-width="34"/><path d="M-70 -262 Q-86 -214 -78 -160" fill="none" stroke="{SKIN}" stroke-width="24"/>'
            f'<path d="M-62 -296 Q-70 -278 -70 -262" fill="none" stroke="{kol}" stroke-width="30"/><circle cx="-78" cy="-152" r="16" fill="{SKIN}"/>'
            f'<g class="armR" style="transform-origin:62px -296px"><path d="M62 -296 Q88 -240 82 -176" fill="none" stroke-width="34"/>'
            f'<path d="M72 -262 Q88 -224 82 -176" fill="none" stroke="{SKIN}" stroke-width="24"/><path d="M62 -296 Q70 -278 72 -262" fill="none" stroke="{kol}" stroke-width="30"/>'
            f'{item}<circle cx="82" cy="-170" r="16" fill="{SKIN}"/></g>')

def brud():
    # gowno na ubraniu i twarzy (pokazywane po gejzerze) + kawalek papieru toaletowego
    random.seed(7)
    plamy = ''.join(f'<ellipse cx="{random.randint(-70, 70)}" cy="{random.randint(-440, -40)}" rx="{random.randint(14, 34)}" ry="{random.randint(10, 26)}" fill="{BRAZ}" opacity=".92"/>' for _ in range(26))
    sciek = ''.join(f'<path d="M{x} {y} q4 30 -2 60" stroke="{BRAZ}" stroke-width="12" fill="none" opacity=".9"/>' for x, y in ((-50, -300), (10, -260), (52, -320), (-20, -420), (40, -440)))
    return (f'<g class="brud" style="display:none" stroke="none">{plamy}{sciek}'
            f'<g class="papier"><rect x="-58" y="-286" width="44" height="34" fill="#fbfbf6" stroke="{K}" stroke-width="3" transform="rotate(-14 -36 -269)"/>'
            f'<path d="M-50 -280 h28 M-50 -268 h28" stroke="#d8d8d0" stroke-width="2" transform="rotate(-14 -36 -269)"/></g></g>')

def osoba(pid, glowa, kol, spodenki, *, logo="", pose="stand", hold="", rece=None, extra_front="", brudna=False):
    dy = 56 if pose == "sit" else 0
    body = (f'{tee(kol)}{extra_front}{P.logo(logo) if logo else ""}<rect x="-18" y="-330" width="36" height="22" fill="{SKIN}" stroke-width="3"/>'
            f'{rece_lato(kol, rece or pose, hold)}{glowa}')
    return (f'<g id="{pid}" class="postac"><g class="bob" style="transform-origin:0px 0px"><g stroke="{K}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">'
            f'{nogi_lato(spodenki, pose=pose)}<g transform="translate(0,{dy})">{body}</g>{brud() if brudna else ""}</g></g></g>')

def andrzej(pid, pose="stand", hold="", rece=None, brudna=False):
    return osoba(pid, P.head("andrzej"), "#1d1d22", "#3d6a9a", logo="adosis", pose=pose, hold=hold, rece=rece, brudna=brudna)
def triwet(pid, pose="stand", hold="", rece=None):
    return osoba(pid, P.head("triwet"), "#22305a", "#4a78a8", pose=pose, hold=hold, rece=rece)

# ---------- otoczenie ----------
def chmura(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})" fill="#fff" stroke="none" opacity=".95"><ellipse cx="0" cy="0" rx="120" ry="46"/>'
            f'<ellipse cx="-70" cy="10" rx="70" ry="36"/><ellipse cx="80" cy="12" rx="80" ry="36"/><ellipse cx="10" cy="-30" rx="70" ry="44"/></g>')

def niebo():
    return f'<rect x="-400" y="-200" width="2400" height="1100" fill="url(#skyLato)"/>' + chmura(300, 200, 1.1) + chmura(900, 160, 1.4) + chmura(1400, 240, .9)

def drzewo(x, y, h, col="#3f7a35"):
    return (f'<g {OL}><path d="M{x} {y} V{y - h * .55}" stroke-width="22"/><path d="M{x} {y} V{y - h * .55}" stroke="#6b4a2a" stroke-width="14"/>'
            f'<circle cx="{x}" cy="{y - h * .7}" r="{h * .3}" fill="{col}"/><circle cx="{x - h * .2}" cy="{y - h * .58}" r="{h * .2}" fill="{col}"/>'
            f'<circle cx="{x + h * .2}" cy="{y - h * .6}" r="{h * .22}" fill="{col}"/></g>')

def tuja(x, y, w, h):
    return (f'<g {OL}><path d="M{x} {y} Q{x - 6} {y - h * .6} {x + w * .25} {y - h} Q{x + w * .5} {y - h * 1.08} {x + w * .75} {y - h} '
            f'Q{x + w + 6} {y - h * .6} {x + w} {y} Z" fill="#3e7a32"/>'
            + ''.join(f'<path d="M{x + w * f} {y - 10} Q{x + w * f - 8} {y - h * .5} {x + w * f + 4} {y - h * .9}" fill="none" stroke="#2c5a24" stroke-width="3"/>' for f in (.2, .4, .6, .8))
            + '</g>')

def dom_ze_zdjecia(x0=0):
    # kremowo-zolty dom z brazowym dachem dwuspadowym, balkon, okna w brazowych ramach, okno dachowe, komin
    X = lambda v: v + x0
    okno = lambda x, y, w, h: (f'<rect x="{X(x)}" y="{y}" width="{w}" height="{h}" fill="#7a4a2a"/><rect x="{X(x) + 8}" y="{y + 8}" width="{w - 16}" height="{h - 16}" fill="#bfe0f2"/>'
                               f'<path d="M{X(x) + w / 2} {y + 8} V{y + h - 8}" stroke-width="5"/><path d="M{X(x) + 14} {y + 14} L{X(x) + 30} {y + 30}" stroke="#fff" stroke-width="3" opacity=".7"/>')
    return f'''<g {OL}>
      <rect x="{X(1180)}" y="430" width="420" height="230" fill="#e8e4a8"/>
      <rect x="{X(1210)}" y="480" width="150" height="110" fill="#7a4a2a"/><rect x="{X(1218)}" y="488" width="134" height="94" fill="#f6f2e8"/>
      <rect x="{X(560)}" y="300" width="640" height="360" fill="#f3e6b0"/>
      <path d="M{X(520)} 330 L{X(830)} 70 L{X(1230)} 330 Z" fill="#f3e6b0"/>
      <path d="M{X(500)} 340 L{X(830)} 56 L{X(860)} 56 L{X(1260)} 360 L{X(1226)} 372 L{X(842)} 96 L{X(536)} 352 Z" fill="#7a3a24"/>
      <path d="M{X(842)} 96 L{X(1226)} 372 L{X(1280)} 372 L{X(1300)} 200 L{X(920)} 60 L{X(860)} 56 Z" fill="#8a4428"/>
      {''.join(f'<path d="M{X(880 + i * 40)} {80 + i * 26} L{X(1240 + i * 6)} {330 + i * 4}" stroke="#6a3020" stroke-width="3" fill="none"/>' for i in range(0, 1))}
      <rect x="{X(1180)}" y="96" width="36" height="96" fill="#7a3a24"/><rect x="{X(1172)}" y="88" width="52" height="16" fill="#5a2a1a"/>
      <path d="M{X(1080)} 214 L{X(1160)} 196 L{X(1170)} 230 L{X(1090)} 248 Z" fill="#bfe0f2"/>
      {okno(700, 200, 70, 96)}{okno(790, 200, 70, 96)}
      <rect x="{X(680)}" y="290" width="200" height="12" fill="#3a3f48"/>
      {''.join(f'<path d="M{X(x)} 240 V290" stroke-width="4"/>' for x in range(690, 880, 16))}<path d="M{X(680)} 240 H{X(880)}" stroke-width="6"/>
      {okno(620, 420, 70, 120)}{okno(720, 420, 70, 120)}{okno(820, 420, 70, 120)}{okno(1040, 420, 90, 110)}
      <circle cx="{X(990)}" cy="330" r="20" fill="#e8ecef"/><path d="M{X(990)} 330 L{X(1004)} 316" stroke-width="4"/>
      <path d="M{X(1200)} 330 V660" stroke="#7a4a2a" stroke-width="8"/>
    </g>'''

def plot_i_chodnik(dekiel_x=None):
    # chodnik z kostki, czarny metalowy plot, ceglany slupek, tuje, bluszcz
    kostka = ''.join(f'<path d="M{x} 690 L{x - 40} 786" stroke="#b8aca0" stroke-width="2"/>' for x in range(-200, 1900, 46))
    plot = ''.join(f'<path d="M{x} 600 V668" stroke-width="5"/><circle cx="{x}" cy="598" r="5" fill="#1a1a1a"/>' for x in range(160, 1050, 22))
    dek = (f'<g id="dekiel"><ellipse cx="{dekiel_x}" cy="740" rx="66" ry="20" fill="#5a6066" {OL}/><ellipse cx="{dekiel_x}" cy="736" rx="52" ry="14" fill="#7a8086" stroke="none"/>'
           f'<path d="M{dekiel_x - 40} 736 H{dekiel_x + 40} M{dekiel_x - 30} 728 H{dekiel_x + 30}" stroke="#4a5056" stroke-width="3"/></g>') if dekiel_x else ''
    return f'''<rect x="-400" y="668" width="2400" height="150" fill="#cfc2b0"/>{kostka}<path d="M-400 690 H2000" stroke="#a89a88" stroke-width="4"/>
      <path d="M-400 760 H2000" stroke="#c88a7a" stroke-width="10" opacity=".6"/>
      <rect x="-400" y="786" width="2400" height="200" fill="#8a8e94"/>
      <g {OL}>{tuja(150, 640, 260, 210)}{tuja(380, 640, 280, 240)}{tuja(630, 640, 260, 200)}</g>
      <g stroke="#1a1a1a" fill="none">{plot}<path d="M150 610 H1050 M150 660 H1050" stroke-width="6"/></g>
      <g {OL}><rect x="1050" y="560" width="70" height="120" fill="#8a3a2a"/>{''.join(f'<path d="M1050 {y} H1120" stroke="#6a2a1a" stroke-width="3"/>' for y in range(576, 680, 16))}
      <rect x="1042" y="548" width="86" height="18" fill="#2a3a5a"/>
      <path d="M1120 680 Q1200 560 1330 600 Q1460 560 1600 590 V680 Z" fill="#3e7a32"/></g>{dek}'''

def sh_dom():
    return niebo() + drzewo(150, 560, 300) + drzewo(1500, 470, 260) + dom_ze_zdjecia() + plot_i_chodnik(dekiel_x=1300)

def sh_sypialnia():
    return f'''<rect x="-200" y="0" width="2000" height="900" fill="#e8d8b8"/>
      <g {OL}><rect x="180" y="200" width="300" height="220" fill="#bfe0f2"/><path d="M330 200 V420 M180 310 H480" stroke-width="8"/>
      <rect x="1280" y="180" width="200" height="500" fill="#a8783e"/><circle cx="1300" cy="440" r="10" fill="#d8b04a"/>
      <rect x="-100" y="680" width="1800" height="220" fill="#b08860"/>
      <rect x="380" y="430" width="560" height="60" rx="8" fill="#8a5a2a"/><rect x="380" y="540" width="760" height="130" rx="10" fill="#8a5a2a"/>
      <path d="M440 520 Q420 470 480 460 L600 462 Q640 470 630 520 Z" fill="#fbfbf6"/>
      <path d="M560 520 Q560 480 640 482 L1110 486 Q1150 500 1140 560 L1130 600 L540 600 Z" fill="#7a9ad8"/>
      <path d="M640 500 Q800 520 1100 500" fill="none" stroke="#5a7ab8" stroke-width="4"/></g>
      <g id="aLozeW" transform="translate(530,500) rotate(-80) scale(.7)">{P.head("andrzej").replace('x="-76" y="-452"', 'x="-76" y="-81"')}</g>
      <g id="smrod" fill="none" stroke="#7aa83a" stroke-width="7" stroke-linecap="round" opacity="0">
        <path d="M1260 420 q-30 -20 0 -40 q30 -20 0 -40 q-30 -20 0 -40"/><path d="M1200 470 q-30 -20 0 -40 q30 -20 0 -40 q-30 -20 0 -40"/>
        <path d="M1140 380 q-30 -20 0 -40 q30 -20 0 -40"/></g>'''

def sh_lazienka():
    kafle = ''.join(f'<path d="M{x} 0 V700" stroke="#b8c4cc" stroke-width="3"/>' for x in range(-200, 1800, 80)) + ''.join(f'<path d="M-200 {y} H1800" stroke="#b8c4cc" stroke-width="3"/>' for y in range(0, 700, 80))
    return f'''<rect x="-200" y="0" width="2000" height="700" fill="url(#kafle)"/>{kafle}
      <rect x="-200" y="700" width="2000" height="200" fill="#9aa8b0"/>
      <g {OL}><rect x="760" y="380" width="120" height="180" rx="10" fill="#fbfbfb"/>
      <path d="M700 560 H960 Q960 660 860 680 L800 680 Q700 660 700 560 Z" fill="#fbfbfb"/><ellipse cx="830" cy="560" rx="130" ry="26" fill="#e8eef2"/>
      <rect x="800" y="680" width="60" height="40" fill="#fbfbfb"/></g>
      <g id="kupa"><ellipse cx="830" cy="556" rx="112" ry="18" fill="{BRAZ}" stroke="{K}" stroke-width="4"/>
        <path id="kupaSciek" d="M720 560 Q700 640 720 720 L960 720 Q980 640 950 560 Z" fill="{BRAZ}" opacity=".95"/>
        <ellipse id="kaluza" cx="830" cy="760" rx="160" ry="34" fill="{BRAZ}" stroke="{K}" stroke-width="4"/>
        <g id="bable"></g></g>
      <g {OL}><rect x="1260" y="160" width="230" height="560" fill="#a8783e"/></g>
      {g("aLaz", 1360, 790, .78, andrzej("aLazP"))}
      {g("tpLaz", 260, 640, 1, f'<g {OL}><rect x="0" y="0" width="90" height="70" rx="10" fill="#fbfbf6"/><circle cx="45" cy="35" r="14" fill="#d8d8d0"/></g>')}'''

def sh_telefon():
    # ekran dzielony: Andrzej (lazienka) | Triwet (podworko)
    return f'''<g><rect x="-200" y="0" width="1010" height="900" fill="url(#kafle)"/>
      {''.join(f'<path d="M{x} 0 V900" stroke="#b8c4cc" stroke-width="3"/>' for x in range(-200, 800, 90))}
      {g("aTel", 420, 1180, 1.5, andrzej("aTelP", rece="ucho"))}</g>
      <g><rect x="810" y="0" width="1000" height="900" fill="url(#skyLato)"/>{chmura(1200, 240, .8)}
      <rect x="810" y="640" width="1000" height="300" fill="#6aa84a"/>{drzewo(1500, 640, 340)}
      {g("rTel", 1160, 1180, 1.5, triwet("rTelP", rece="ucho"))}</g>
      <path d="M810 0 V900" stroke="{K}" stroke-width="14"/>'''

# ---------- traktor z beczka ----------
def beczka(bid="beczka", x=0, y=0, s=1.0, malowana=False, napis=False):
    # beczka na gnojowice na dwoch kolach; warstwa niebieska odslaniana (clipPath #malujClip)
    nieb = f'<g id="{bid}Nieb" clip-path="url(#{bid}Clip)"><rect x="-10" y="-336" width="560" height="232" rx="110" fill="url(#niebG)" {OL}/></g>'
    txt = (f'<text id="{bid}Napis" x="270" y="-196" text-anchor="middle" font-family="Arial Black, sans-serif" font-size="58" font-weight="900" '
           f'fill="#fff" stroke="{K}" stroke-width="3" paint-order="stroke" letter-spacing="3" style="{"" if napis else "display:none"}">WODA PITNA</text>')
    return f'''<g id="{bid}" transform="translate({x},{y}) scale({s})">
      <defs><clipPath id="{bid}Clip"><rect id="{bid}ClipR" x="-20" y="-350" width="{580 if malowana else 0}" height="260"/></clipPath></defs>
      <g {OL}><path d="M-10 -150 L-150 -120" stroke-width="12"/>
      <rect x="-10" y="-336" width="560" height="232" rx="110" fill="url(#beczkaG)"/>
      {''.join(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#8a4a1a" opacity=".55" stroke="none"/>' for cx, cy, rx, ry in ((120, -280, 40, 16), (360, -170, 60, 20), (440, -300, 30, 12), (220, -150, 50, 14)))}
      {nieb}
      <path d="M40 -330 V-112 M500 -330 V-112" stroke-width="4" opacity=".6"/>
      <rect x="250" y="-360" width="60" height="30" rx="6" fill="#4a4f57"/>
      <path d="M540 -170 H600 Q620 -170 620 -150 V-110" fill="none" stroke="#1a1a1a" stroke-width="20"/><path d="M540 -170 H600 Q620 -170 620 -150 V-110" fill="none" stroke="#3a3f48" stroke-width="12"/>
      {S21.wheel(270, -90, 90, .48, "kB")}</g>{txt}</g>'''

def traktor(tid, x, y, s, kierowca="", beczka_svg=""):
    # Ursus (rysunek z odc. 21) -> C-360, bez Stivena; beczka doczepiona z tylu (po lewej)
    t = S21.c330(tid, driver=False).replace(">C-330<", ">C-360<")
    return f'<g id="{tid}W" transform="translate({x},{y}) scale({s})">{beczka_svg}{kierowca}{t}</g>'

def kierowca_triwet(pid):
    return g(pid, -40, -262, .8, triwet(pid + "P", pose="sit", rece="stand"))

def sh_podworko():
    stodola = f'''<g {OL}><rect x="1050" y="250" width="520" height="420" fill="#8a3a2a"/><path d="M1020 260 L1310 120 L1600 260 Z" fill="#5a5f66"/>
      <rect x="1180" y="400" width="260" height="270" fill="#6a2a1a"/><path d="M1180 400 L1440 670 M1440 400 L1180 670" stroke-width="6"/></g>'''
    return (niebo() + f'<rect x="-400" y="640" width="2400" height="300" fill="#7ab05a"/>' + stodola + drzewo(140, 650, 320)
            + traktor("trPod", 760, 700, .78, beczka_svg=beczka("bPod", -720, 0, 1.0))
            + g("aPod", 300, 770, .62, andrzej("aPodP", hold="farba")) + g("rPod", 480, 770, .62, triwet("rPodP", hold="pedzel")))

def domki_tlo(seed, y=560):
    random.seed(seed); out = ''
    for i in range(10):
        x = i * 360 - 400 + random.randint(-30, 30); w = random.randint(180, 240); h = random.randint(120, 160)
        out += (f'<g {OL}><rect x="{x}" y="{y - h}" width="{w}" height="{h}" fill="{random.choice(["#f3e6b0", "#e8e8e0", "#f2d8c0"])}"/>'
                f'<path d="M{x - 16} {y - h} L{x + w / 2} {y - h - 80} L{x + w + 16} {y - h} Z" fill="{random.choice(["#7a3a24", "#5a5f66", "#8a4428"])}"/>'
                f'<rect x="{x + 30}" y="{y - h + 40}" width="44" height="44" fill="#bfe0f2"/></g>')
    return out

def sh_jazda():
    return (niebo() + f'<g id="jazdaTlo">{domki_tlo(3)}{"".join(drzewo(x, 600, 200) for x in range(-300, 3600, 420))}</g>'
            + '<rect x="-400" y="600" width="2400" height="90" fill="#7ab05a"/><rect x="-400" y="690" width="2400" height="200" fill="#8a8e94"/>'
            + f'<g id="pasy">{"".join(f"<rect x={chr(34)}{x}{chr(34)} y={chr(34)}760{chr(34)} width={chr(34)}90{chr(34)} height={chr(34)}12{chr(34)} fill={chr(34)}#fff{chr(34)}/>" for x in range(-400, 4000, 180))}</g>'
            + traktor("trJazda", 1000, 800, .72, kierowca=kierowca_triwet("rJazda")
                      + g("aJazda", 140, -300, .62, andrzej("aJazdaP", pose="sit", rece="stand")),
                      beczka_svg=beczka("bJazda", -720, 0, 1.0, malowana=True, napis=True)))

def sh_szambo():
    return (niebo() + drzewo(1500, 470, 260) + dom_ze_zdjecia() + plot_i_chodnik(dekiel_x=1300)
            + traktor("trSz", 560, 900, .62, kierowca=kierowca_triwet("rSz"), beczka_svg=beczka("bSz", -720, 0, 1.0, malowana=True, napis=True))
            + f'<path id="wazSz" d="M760 830 Q900 900 1100 820 Q1230 760 1290 740" fill="none" stroke="#1a1a1a" stroke-width="26"/>'
            + f'<path d="M760 830 Q900 900 1100 820 Q1230 760 1290 740" fill="none" stroke="#3a3f48" stroke-width="18"/>'
            + '<g id="gejzer" style="display:none"></g>'
            + g("aSz", 1180, 770, .62, andrzej("aSzP", rece="waz", brudna=True)))

def sh_wajcha():
    gate = ''.join(f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Arial Black" font-size="64" fill="#f2f2f2">{t}</text>' for x, y, t in ((560, 330, "1"), (1040, 330, "R"), (560, 760, "2"), (800, 760, "3")))
    return f'''<rect x="-200" y="-200" width="2000" height="1300" fill="#2a2426"/>
      <path d="M-200 600 Q800 470 1800 600 V1100 H-200 Z" fill="{RED_D}" {OL}/>
      <rect x="440" y="380" width="720" height="300" rx="30" fill="#1a1a1a" {OL}/>
      <path d="M560 420 V640 M560 530 H1040 M1040 420 V530 M800 530 V640" stroke="#6a6e76" stroke-width="34" stroke-linecap="round"/>
      <path d="M560 420 V640 M560 530 H1040 M1040 420 V530 M800 530 V640" stroke="#0a0a0a" stroke-width="22" stroke-linecap="round"/>
      {gate}
      <g id="wajcha" style="transform-origin:800px 900px;transform:rotate(-14deg)">
        <path d="M800 900 L800 470" stroke="{K}" stroke-width="40" stroke-linecap="round"/><path d="M800 900 L800 470" stroke="#9aa3ad" stroke-width="26" stroke-linecap="round"/>
        <circle cx="800" cy="440" r="70" fill="#1a1a1a" {OL}/><circle cx="782" cy="420" r="20" fill="#4a4a4a" stroke="none"/>
        <g {OL}><path d="M720 400 Q700 470 760 500 L860 500 Q900 470 880 400 Q800 360 720 400 Z" fill="{SKIN}"/>
        <path d="M740 420 h120 M738 448 h124" stroke="#c8865a" stroke-width="4"/></g></g>'''

def sh_pusto():
    # POV z dna szamba: okrag nieba, nad krawedzia dwie glowy zagladaja do srodka
    return f'''<rect x="-200" y="-200" width="2000" height="1300" fill="#3a3e44"/>
      {''.join(f'<circle cx="800" cy="450" r="{r}" fill="none" stroke="#2a2e34" stroke-width="10"/>' for r in range(420, 900, 70))}
      <circle cx="800" cy="450" r="300" fill="url(#skyLato)" {OL}/>{chmura(720, 360, .5)}
      <g id="aPusto" transform="translate(690,360) rotate(180)">{P.head("andrzej").replace('x="-76" y="-452"', 'x="-76" y="-90"')}</g>
      <g id="rPusto" transform="translate(920,380) rotate(200)">{P.head("triwet").replace('x="-76" y="-452"', 'x="-76" y="-90"')}</g>
      <circle cx="800" cy="450" r="300" fill="none" stroke="#5a6066" stroke-width="24"/>'''

def kosciol(x, y, s=1.0):
    return f'''<g transform="translate({x},{y}) scale({s})" {OL}>
      <rect x="-60" y="-420" width="120" height="420" fill="#e8e4dc"/><path d="M-80 -420 L0 -560 L80 -420 Z" fill="#5a3a2a"/>
      <path d="M0 -560 V-620 M-20 -600 H20" stroke="#d8b04a" stroke-width="8"/>
      <rect x="60" y="-240" width="300" height="240" fill="#ece8e0"/><path d="M40 -240 L210 -340 L380 -240 Z" fill="#5a3a2a"/>
      <rect x="-26" y="-340" width="52" height="80" rx="26" fill="#ffd96a"/>
      {''.join(f'<rect x="{xx}" y="-190" width="44" height="90" rx="22" fill="#ffd96a"/>' for xx in (110, 188, 266))}</g>'''

def sh_kosciol():
    return (niebo() + kosciol(1100, 620, .9) + '<rect x="-400" y="620" width="2400" height="80" fill="#7ab05a"/><rect x="-400" y="700" width="2400" height="200" fill="#8a8e94"/>'
            + traktor("trKos", -900, 820, .62, kierowca=kierowca_triwet("rKos") + g("aKos", 140, -300, .62, andrzej("aKosP", pose="sit", rece="stand")),
                      beczka_svg=beczka("bKos", -720, 0, 1.0, malowana=True, napis=True)))

def sklep(x, y, s=1.0):
    return f'''<g transform="translate({x},{y}) scale({s})" {OL}>
      <rect x="0" y="-220" width="360" height="220" fill="#f2efe6"/><path d="M-12 -220 H372 L360 -250 H0 Z" fill="#6b7078"/>
      <rect x="40" y="-200" width="280" height="50" fill="#c81e1e"/><text x="180" y="-163" text-anchor="middle" font-family="Arial Black" font-size="34" fill="#fff" stroke="none">SKLEP</text>
      <rect x="40" y="-130" width="120" height="130" fill="#7aa8c8"/><rect x="200" y="-130" width="120" height="90" fill="#bfe0f2"/></g>'''

def sh_narew():
    fale = ''.join(f'<path d="M{x} {y} q20 -8 40 0" fill="none" stroke="#bfe0f2" stroke-width="4"/>' for x, y in ((300, 700), (520, 740), (760, 690), (980, 760), (1220, 720), (1420, 750)))
    return (niebo() + '<rect x="-400" y="430" width="2400" height="90" fill="#7ab05a"/>' + kosciol(260, 470, .45) + sklep(560, 470, .5)
            + ''.join(drzewo(x, 470, 160) for x in (60, 820, 1020, 1500))
            + f'<rect x="-400" y="510" width="2400" height="400" fill="url(#woda)"/>{fale}'
            + '<g id="brazWoda"><ellipse cx="560" cy="700" rx="10" ry="4" fill="#6b4a1e" opacity=".9"/></g>'
            + f'<path d="M1000 600 Q1300 560 1700 620 V900 H1000 Z" fill="#7ab05a" {OL}/>'
            + traktor("trNar", 1560, 760, .58, kierowca=kierowca_triwet("rNar"), beczka_svg=beczka("bNar", -720, 0, 1.0, malowana=True, napis=True))
            + f'<path d="M990 700 Q760 640 600 700" fill="none" stroke="#1a1a1a" stroke-width="20"/><path d="M990 700 Q760 640 600 700" fill="none" stroke="#3a3f48" stroke-width="13"/>'
            + g("aNar", 1060, 720, .5, andrzej("aNarP", rece="stand"))
            + f'''<g id="karas" style="display:none"><g transform="translate(700,700)" {OL}><path d="M-60 0 Q0 -50 60 0 Q0 50 -60 0 Z" fill="#c8a03a"/>
               <path d="M60 0 L100 -30 L100 30 Z" fill="#c8a03a"/><circle cx="-34" cy="-8" r="7" fill="#fff"/><circle cx="-34" cy="-8" r="3" fill="{K}"/>
               <path d="M-58 6 Q-48 14 -40 6" fill="none" stroke-width="3"/></g></g>''')

SHOTS = [("shDom", sh_dom()), ("shSypialnia", sh_sypialnia()), ("shLazienka", sh_lazienka()), ("shTelefon", sh_telefon()),
         ("shPodworko", sh_podworko()), ("shJazda", sh_jazda()), ("shSzambo", sh_szambo()), ("shWajcha", sh_wajcha()),
         ("shPusto", sh_pusto()), ("shKosciol", sh_kosciol()), ("shNarew", sh_narew())]

WHO_JS = '''  const who = {
    a: { el: "aLazP", vPitch: 0.8, vRate: 1.15 },
    r: { el: "rTelP", vPitch: 0.95, vRate: 1.05 }
  };
'''

SHOTS_SVG = '\n'.join(f'    <g class="shot" id="{i}" style="display:none">{svg}</g>' for i, svg in SHOTS)
