# Wersja pionowa (9:16) odcinka: python3 build_pion.py miruna  ->  miruna_pion.html
# Kadr 506x900 wyciety ze sceny 1600x900 jedzie za postacia, ktora mowi;
# intro, outro, plansze i ekran z kasa pokazywane w calosci (pas 16:9 na srodku).
import re, sys

ep = sys.argv[1] if len(sys.argv) > 1 else "miruna"
s = open(f"{ep}.html", encoding="utf-8").read()

# incognito: bez nazw miejscowosci (nowe wymyslimy)
s = s.replace(">PUŁTUSK</text>", "></text>")

# strona w pionie
s = s.replace("#wrap { position:relative; width:min(100vw, calc(100vh * 16 / 9)); aspect-ratio:16 / 9; }",
              "#wrap { position:relative; width:min(100vw, calc(100vh * 9 / 16)); aspect-ratio:9 / 16; }")
s = s.replace("#stage { width:100%; height:100%; display:block; background:#9fd3ff; }",
              "#stage { width:100%; height:100%; display:block; background:#000; }")
s = s.replace('<svg id="stage" viewBox="0 0 1600 900"', '<svg id="stage" viewBox="547 0 506 900"')
s = s.replace("<title>", "<title>(pion) ", 1)
assert "aspect-ratio:9 / 16" in s and 'viewBox="547 0 506' in s

PION = r'''
<script>
// ---------- kadr pionowy ----------
(function(){
  const st = document.getElementById("stage"), W = 506.25, H = 900, FH = 1600 * 16 / 9;
  const FIT = { x: 0, y: 450 - FH / 2, w: 1600, h: FH };
  const cur = { x: 800 - W / 2, y: 0, w: W, h: H };
  let fit = 0, track = null, fx = 800;
  const lerp = (a, b, t) => a + (b - a) * t;
  function stageX(el){            // srodek elementu we wspolrzednych sceny 1600x900
    const r = el.getBoundingClientRect(), sr = st.getBoundingClientRect();
    if (!r.width) return null;
    return cur.x + ((r.left + r.width / 2) - sr.left) / sr.width * cur.w;
  }
  function frame(){
    if (track){ const x = stageX(track); if (x !== null && x > -200 && x < 1800) fx = x; }
    const cx = Math.max(0, Math.min(1600 - W, fx - W / 2));
    const t = fit ? FIT : { x: cx, y: 0, w: W, h: H };
    const k = 0.07;
    cur.x = lerp(cur.x, t.x, k); cur.y = lerp(cur.y, t.y, k);
    cur.w = lerp(cur.w, t.w, k); cur.h = lerp(cur.h, t.h, k);
    st.setAttribute("viewBox", `${cur.x.toFixed(1)} ${cur.y.toFixed(1)} ${cur.w.toFixed(1)} ${cur.h.toFixed(1)}`);
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
  const snap = () => { const t = fit ? FIT : { x: Math.max(0, Math.min(1600 - W, fx - W / 2)), y: 0, w: W, h: H }; Object.assign(cur, t); };
  const center = () => { track = null; fx = 800; };

  // kto mowi, za tym jedzie kadr
  const _say = say;
  say = function(k, ...a){
    const w = who[k];
    if (w){ fx = w.x; const el = w.el && document.getElementById(w.el); track = el || null; }
    return _say.call(this, k, ...a);
  };
  // pelny kadr: intro, outro, plansze, kasa
  const full = fn => async function(...a){ fit++; snap(); try { return await fn.apply(this, a); } finally { fit--; center(); snap(); } };
  ziomkiIntro2 = full(ziomkiIntro2);
  ziomkiOutro = full(ziomkiOutro);
  const _card = card;   // plansza: kadr na srodku, tekst wiekszy
  card = async function(...a){ center(); snap(); const t = document.getElementById("cardTxt"); t.setAttribute("font-size", "56"); return _card.apply(this, a); };
  const cash = document.getElementById("cash");
  new MutationObserver(() => { const on = cash.style.display !== "none"; if (on !== !!cash._fit){ cash._fit = on; fit += on ? 1 : -1; } })
    .observe(cash, { attributes: true, attributeFilter: ["style"] });
  // napisy "POW" mieszcza sie w kadrze
  const _pow = pow;
  pow = function(txt, x, y, o = {}){
    if (fit) return _pow.call(this, txt, x, y, o);
    let size = o.size || 110; const est = t => t.length * size * 0.56;
    if (est(txt) > W - 40) size = (W - 40) / (txt.length * 0.56);
    const half = est(txt) / 2 + 20;
    x = Math.max(cur.x + half, Math.min(cur.x + W - half, x));
    return _pow.call(this, txt, x, y, Object.assign({}, o, { size }));
  };
  // nowy start = kadr na srodku
  const _play = play;
  play = function(...a){ center(); fit = 0; snap(); return _play.apply(this, a); };
})();
</script>
'''
s = s.replace("</body>", PION + "</body>", 1)
open(f"{ep}_pion.html", "w", encoding="utf-8").write(s)
print("ok", f"{ep}_pion.html")
