// Proby nowego intra serii "ZIOMKI" w stylu komiksowych kadrow (Andrzej, Triwet, SYKET).
// Uzycie: await ziomkiIntro2("TYTUL", nr, wariant)  wariant = 1 | 2 | 3
(function(){
  const NS = "http://www.w3.org/2000/svg";
  const wait = ms => new Promise(r => setTimeout(r, ms));
  const ctx = () => (typeof ac === "function") ? ac() : (window._ziCtx = window._ziCtx || new (window.AudioContext || window.webkitAudioContext)());

  // ---------- dzwiek ----------
  function noiseAt(t, dur, { type = "highpass", freq = 6000, q = 1, vol = 0.2, to } = {}){
    const a = ctx(), len = Math.floor(a.sampleRate * dur), buf = a.createBuffer(1, len, a.sampleRate), d = buf.getChannelData(0);
    for (let i = 0; i < len; i++) d[i] = Math.random() * 2 - 1;
    const s = a.createBufferSource(); s.buffer = buf;
    const f = a.createBiquadFilter(); f.type = type; f.frequency.setValueAtTime(freq, t); f.Q.value = q;
    if (to) f.frequency.exponentialRampToValueAtTime(to, t + dur * 0.9);
    const g = a.createGain(); g.gain.setValueAtTime(vol, t); g.gain.exponentialRampToValueAtTime(0.001, t + dur);
    s.connect(f); f.connect(g); g.connect(a.destination); s.start(t); s.stop(t + dur);
  }
  function osc(t, dur, f0, f1, type, vol){
    const a = ctx(), o = a.createOscillator(), g = a.createGain();
    o.type = type; o.frequency.setValueAtTime(f0, t); if (f1) o.frequency.exponentialRampToValueAtTime(f1, t + dur);
    g.gain.setValueAtTime(vol, t); g.gain.exponentialRampToValueAtTime(0.001, t + dur);
    o.connect(g); g.connect(a.destination); o.start(t); o.stop(t + dur + 0.02);
  }
  const kick = t => osc(t, 0.3, 150, 40, "sine", 0.8);
  const snare = t => { noiseAt(t, 0.18, { freq: 1800, vol: 0.45 }); osc(t, 0.12, 190, 0, "sine", 0.25); };
  const hat = t => noiseAt(t, 0.04, { freq: 8000, vol: 0.12 });
  const clap = t => [0, 0.012, 0.024].forEach(d => noiseAt(t + d, 0.12, { type: "bandpass", freq: 1200, q: 1.5, vol: 0.35 }));
  function bass(t, f, dur){
    const a = ctx(), o = a.createOscillator(), lp = a.createBiquadFilter(), g = a.createGain();
    o.type = "sawtooth"; o.frequency.value = f; lp.type = "lowpass"; lp.frequency.value = 400;
    g.gain.setValueAtTime(0.18, t); g.gain.exponentialRampToValueAtTime(0.001, t + dur);
    o.connect(lp); lp.connect(g); g.connect(a.destination); o.start(t); o.stop(t + dur);
  }
  function scratch(t, n){
    for (let i = 0; i < n; i++){
      const t0 = t + i * 0.11, up = i % 2 === 0;
      noiseAt(t0, 0.1, { type: "bandpass", freq: up ? 500 : 3200, q: 6, vol: 0.55, to: up ? 3200 : 500 });
      osc(t0, 0.1, up ? 180 : 700, up ? 700 : 180, "sawtooth", 0.07);
    }
  }
  let curve = null;
  function guitar(t, f, dur, vol = 0.13){
    const a = ctx();
    if (!curve){ curve = new Float32Array(1024); for (let i = 0; i < 1024; i++) curve[i] = Math.tanh((i / 512 - 1) * 6); }
    const ws = a.createWaveShaper(); ws.curve = curve;
    const lp = a.createBiquadFilter(); lp.type = "lowpass"; lp.frequency.value = 2600;
    const g = a.createGain(); g.gain.setValueAtTime(0.0001, t); g.gain.linearRampToValueAtTime(vol, t + 0.01); g.gain.exponentialRampToValueAtTime(0.001, t + dur);
    [f, f * 1.5, f * 2].forEach(fr => { const o = a.createOscillator(); o.type = "sawtooth"; o.frequency.value = fr; o.detune.value = Math.random() * 8 - 4; o.connect(ws); o.start(t); o.stop(t + dur + 0.02); });
    ws.connect(lp); lp.connect(g); g.connect(a.destination);
  }
  const boom = t => { osc(t, 0.9, 90, 30, "sine", 0.9); noiseAt(t, 0.8, { type: "lowpass", freq: 900, vol: 0.6, to: 120 }); };
  const swoosh = (t, d = 0.35) => noiseAt(t, d, { type: "bandpass", freq: 600, q: 0.8, vol: 0.35, to: 4000 });
  const glint = t => { osc(t, 0.35, 2400, 0, "sine", 0.08); osc(t + 0.06, 0.3, 3600, 0, "sine", 0.05); };
  const paper = t => noiseAt(t, 0.25, { type: "highpass", freq: 3000, vol: 0.18, to: 9000 });
  // wspolny bit: 2 takty, tempo 92
  function beat2(T, beat, { bassLine = [[0, 55], [1.5, 65], [2, 49], [3, 58]], riff = true } = {}){
    for (let bar = 0; bar < 2; bar++){
      const b0 = T + bar * 4 * beat;
      [0, 2, 2.5].forEach(x => kick(b0 + x * beat));
      [1, 3].forEach(x => (bar ? clap : snare)(b0 + x * beat));
      for (let e = 0; e < 8; e++) hat(b0 + e * beat / 2);
      bassLine.forEach(([x, f]) => bass(b0 + x * beat, f, beat * 0.9));
      if (riff) [[0, 82.4, 0.5], [0.5, 82.4, 0.5], [1, 98, 0.5], [2, 110, 0.5], [2.5, 110, 0.5], [3, bar ? 123.5 : 98, 0.9]].forEach(([x, f, d]) => guitar(b0 + x * beat, f, d * beat));
    }
  }


  // ================= PODKLADY MUZYCZNE (do wersji 3) =================
  const N = n => 440 * Math.pow(2, (n - 69) / 12);   // nr nuty MIDI -> Hz
  function lead(t, f, dur, { type = "square", vol = 0.07, vib = 0, cut = 3000, glideTo } = {}){
    const a = ctx(), o = a.createOscillator(), lp = a.createBiquadFilter(), g = a.createGain();
    o.type = type; o.frequency.setValueAtTime(f, t); if (glideTo) o.frequency.exponentialRampToValueAtTime(glideTo, t + dur);
    if (vib){ const l = a.createOscillator(), lg = a.createGain(); l.frequency.value = 6; lg.gain.value = vib; l.connect(lg); lg.connect(o.frequency); l.start(t); l.stop(t + dur + 0.05); }
    lp.type = "lowpass"; lp.frequency.value = cut;
    g.gain.setValueAtTime(0.0001, t); g.gain.linearRampToValueAtTime(vol, t + 0.01); g.gain.setValueAtTime(vol, t + dur * 0.7); g.gain.exponentialRampToValueAtTime(0.001, t + dur);
    o.connect(lp); lp.connect(g); g.connect(a.destination); o.start(t); o.stop(t + dur + 0.02);
  }
  const crash = t => noiseAt(t, 1.2, { freq: 5000, vol: 0.18 });
  const openHat = t => noiseAt(t, 0.15, { freq: 7000, vol: 0.14 });
  function acid(t, f, dur, open){
    const a = ctx(), o = a.createOscillator(), lp = a.createBiquadFilter(), g = a.createGain();
    o.type = "sawtooth"; o.frequency.value = f; lp.type = "lowpass"; lp.Q.value = 14;
    lp.frequency.setValueAtTime(open, t); lp.frequency.exponentialRampToValueAtTime(200, t + dur);
    g.gain.setValueAtTime(0.12, t); g.gain.exponentialRampToValueAtTime(0.001, t + dur);
    o.connect(lp); lp.connect(g); g.connect(a.destination); o.start(t); o.stop(t + dur + 0.02);
  }
  const loop = (T, dur, bpm, fn) => { const b = 60 / bpm; for (let i = 0; T + i * b < T + dur; i++) fn(T + i * b, i, b); };
  const MUSIC = {
    // 1. hip-hop + przesterowana gitara (jak dotad)
    1: (T, dur) => { const beat = 60 / 92; beat2(T, beat, { riff: false });
      [[0, 82.4], [0.75, 82.4], [1.5, 110], [2.5, 98], [3, 123.5], [4.5, 82.4], [5.5, 110], [6, 146.8], [7, 164.8]].forEach(([x, f]) => guitar(T + x * beat, f, beat * 0.7, 0.15)); },
    // 2. disco polo: stopa na cztery, hi-hat na "i", skaczacy bas, tandetny klawisz
    2: (T, dur) => { const mel = [69, 72, 76, 74, 72, 71, 69, 64, 69, 72, 76, 79, 77, 76, 74, 72];
      loop(T, dur, 128, (t, i, b) => { kick(t); openHat(t + b / 2); if (i % 2) clap(t);
        const root = [45, 45, 41, 43][Math.floor(i / 4) % 4]; bass(t, N(root), b * 0.45); bass(t + b / 2, N(root + 12), b * 0.45);
        lead(t, N(mel[i % 16]), b * 0.45, { type: "sawtooth", vol: 0.05, vib: 6, cut: 2500 }); lead(t + b / 2, N(mel[i % 16] + 12), b * 0.3, { type: "square", vol: 0.025 }); }); },
    // 3. 8-bit jak z Pegasusa
    3: (T, dur) => { const arp = [0, 4, 7, 12], roots = [60, 60, 65, 67];
      loop(T, dur, 150, (t, i, b) => { const r = roots[Math.floor(i / 4) % 4];
        for (let k = 0; k < 4; k++) lead(t + k * b / 4, N(r + arp[k] + 12), b / 4 * 0.9, { type: "square", vol: 0.045 });
        lead(t, N(r - 12), b * 0.9, { type: "triangle", vol: 0.2 });
        if (i % 2 === 0) noiseAt(t, 0.05, { type: "lowpass", freq: 300, vol: 0.4 }); else noiseAt(t, 0.08, { freq: 2500, vol: 0.25 }); });
      lead(T + dur - 0.9, N(84), 0.8, { type: "square", vol: 0.05, glideTo: N(96) }); },
    // 4. punk rock: szybka perkusja, power-chordy
    4: (T, dur) => { crash(T);
      loop(T, dur, 180, (t, i, b) => { kick(t); snare(t + b / 2); hat(t); hat(t + b / 2);
        const r = [40, 40, 43, 45, 40, 40, 47, 45][Math.floor(i / 2) % 8]; guitar(t, N(r), b * 0.48, 0.16); guitar(t + b / 2, N(r), b * 0.48, 0.16); });
      crash(T + dur * 0.5); },
    // 5. techno / rave z kwasnym basem
    5: (T, dur) => { const seq = [36, 36, 48, 36, 39, 36, 46, 36];
      loop(T, dur, 135, (t, i, b) => { kick(t); openHat(t + b / 2); if (i % 2) clap(t);
        for (let k = 0; k < 2; k++) acid(t + k * b / 2, N(seq[(i * 2 + k) % 8]), b * 0.45, 600 + 3000 * ((i * 2 + k) / (dur / b * 2))); }); },
    // 6. trap: 808 z poslizgiem, rolki hi-hatu
    6: (T, dur) => { const b = 60 / 140;
      [0, 2.5, 4, 6.5, 8, 10.5].forEach((x, k) => { if (x * b < dur){ kick(T + x * b); lead(T + x * b, N([33, 33, 31, 36, 33, 28][k]), b * 2.2, { type: "sine", vol: 0.45, cut: 400, glideTo: N([33, 33, 31, 36, 33, 28][k]) * 0.94 }); } });
      [2, 6, 10].forEach(x => x * b < dur && (snare(T + x * b), clap(T + x * b)));
      for (let x = 0; x * b < dur; x += 0.5){ hat(T + x * b); if (Math.floor(x) % 4 === 3) [1, 2].forEach(k => hat(T + x * b + k * b / 6)); }
      [0, 4, 8].forEach(x => lead(T + x * b, N(81), b * 1.5, { type: "triangle", vol: 0.05, vib: 4 })); },
    // 7. fanfara superbohaterow: tympany i "blacha"
    7: (T, dur) => { const b = 60 / 110;
      const brass = (t, notes, d) => notes.forEach(n => lead(t, N(n), d, { type: "sawtooth", vol: 0.045, vib: 3, cut: 1800 }));
      [[0, [55, 62, 67], 0.5], [0.75, [55, 62, 67], 0.25], [1, [60, 64, 72], 1.5], [3, [58, 65, 70], 0.5], [3.5, [60, 67, 72], 0.5], [4, [62, 69, 74], 2.5]].forEach(([x, n, d]) => brass(T + x * b, n, d * b));
      [0, 1, 3, 4, 4.25, 4.5, 4.75].forEach(x => osc(T + x * b, 0.5, 70, 50, "sine", 0.7));
      crash(T + 4 * b); for (let x = 0; x < 9; x++) snare(T + 6 * b + x * b / 6); boom(T + 7.5 * b); }
  };
  window.ziomkiMusic = MUSIC;
  window.ziomkiMusicNames = { 1: "Hip-hop z gitarą", 2: "Disco polo", 3: "8-bit (Pegasus)", 4: "Punk rock", 5: "Techno / rave", 6: "Trap", 7: "Fanfara superbohaterów" };

  // ---------- grafika ----------
  const CH = [
    { name: "ANDRZEJ", img: "andrzej.svg", w: 300, h: 320, shirt: "#1c1c1c", bg: "#ffd23f", ray: "#ffb13b", fx: "ZIUU!" },
    { name: "TRIWET",  img: "triwet.svg",  w: 300, h: 320, shirt: "#1f2a44", bg: "#4ab8e8", ray: "#2a8ec8", fx: "BACH!" },
    { name: "SYKET",   img: "syket.svg",   w: 300, h: 320, shirt: "#c81e2a", bg: "#ff5a5a", ray: "#d83a3a", fx: "ŁUP!" }
  ];
  const IMPACT = "Impact, 'Arial Black', sans-serif", COMIC = "'Comic Sans MS','Chalkboard SE',sans-serif";
  function rays(cx, cy, n, col, r = 1400){
    let s = "";
    for (let i = 0; i < n; i++){ const a0 = i * 2 * Math.PI / n, a1 = a0 + Math.PI / n;
      s += `<polygon points="${cx},${cy} ${cx + r * Math.cos(a0)},${cy + r * Math.sin(a0)} ${cx + r * Math.cos(a1)},${cy + r * Math.sin(a1)}" fill="${col}"/>`; }
    return s;
  }
  // popiersie: glowa z PNG + ramiona w koszulce; (cx, cy) = srodek glowy, k = skala
  function bust(c, cx, cy, k, cls = ""){
    const hw = c.w * k, hh = c.h * k;
    return `<g class="bust ${cls}" style="transform-origin:${cx}px ${cy + hh * 0.5}px">
      <path d="M${cx - hw * 0.95} ${cy + hh * 1.6} Q${cx - hw * 0.95} ${cy + hh * 0.55} ${cx} ${cy + hh * 0.5} Q${cx + hw * 0.95} ${cy + hh * 0.55} ${cx + hw * 0.95} ${cy + hh * 1.6} Z" fill="${c.shirt}" stroke="#141414" stroke-width="6"/>
      <path d="M${cx - hw * 0.18} ${cy + hh * 0.5} Q${cx} ${cy + hh * 0.62} ${cx + hw * 0.18} ${cy + hh * 0.5}" fill="none" stroke="#141414" stroke-width="5"/>
      <image href="${c.img}" x="${cx - hw / 2}" y="${cy - hh / 2}" width="${hw}" height="${hh}"/></g>`;
  }
  const dots = id => `<pattern id="${id}" width="18" height="18" patternUnits="userSpaceOnUse"><circle cx="9" cy="9" r="4" fill="#000" opacity="0.18"/></pattern>`;
  function caption(x, y, txt, size = 54, fill = "#fff6b0"){
    const w = txt.length * size * 0.74 + 50;
    return `<g class="cap"><rect x="${x - w / 2}" y="${y - size * 0.9}" width="${w}" height="${size * 1.25}" fill="${fill}" stroke="#141414" stroke-width="6"/>
      <text x="${x}" y="${y + size * 0.12}" text-anchor="middle" font-family="${COMIC}" font-weight="700" font-size="${size}" fill="#141414">${txt}</text></g>`;
  }
  function logo(cx, cy, size = 190){
    return `<text x="${cx}" y="${cy}" text-anchor="middle" font-family="${IMPACT}" font-size="${size}" fill="#ffd23f" stroke="#000" stroke-width="10" paint-order="stroke" letter-spacing="10">ZIOMKI</text>`;
  }
  function burst(cx, cy, r1, r2, n, fill){
    let p = [];
    for (let i = 0; i < n * 2; i++){ const r = i % 2 ? r1 : r2, a = i * Math.PI / n; p.push(`${(cx + r * Math.cos(a)).toFixed(1)},${(cy + r * Math.sin(a) * 0.72).toFixed(1)}`); }
    return `<polygon points="${p.join(" ")}" fill="${fill}" stroke="#141414" stroke-width="8"/>`;
  }
  const titleSize = (t, max = 100, w = 1100) => Math.min(max, Math.floor(w / (t.length * 0.5)));
  const A = (el, kf, o) => el.animate(kf, Object.assign({ fill: "both" }, o));

  // ================= WERSJA 1: trzy skosne kadry, rozbijaja sie, logo z hukiem =================
  async function v1(g, title, num){
    const P = [[[30, 30], [560, 30], [480, 870], [30, 870]], [[580, 30], [1060, 30], [1000, 870], [500, 870]], [[1080, 30], [1570, 30], [1570, 870], [1020, 870]]];
    const C = [[290, 380], [790, 380], [1300, 380]];
    let html = `<rect width="1600" height="900" fill="#141414"/><defs>${dots("d1")}`;
    P.forEach((p, i) => html += `<clipPath id="cp1_${i}"><polygon points="${p.map(q => q.join(",")).join(" ")}"/></clipPath>`);
    html += `</defs>`;
    P.forEach((p, i) => { const c = CH[i], [cx, cy] = C[i];
      html += `<g class="pan" style="transform-origin:${cx}px 450px"><g clip-path="url(#cp1_${i})">
        <rect width="1600" height="900" fill="${c.bg}"/>${rays(cx, cy, 18, c.ray)}<rect width="1600" height="900" fill="url(#d1)"/>
        ${bust(c, cx, cy, 1.15)}
        <text class="fx" x="${cx}" y="150" text-anchor="middle" font-family="${IMPACT}" font-size="90" fill="#fff" stroke="#141414" stroke-width="7" paint-order="stroke" transform="rotate(-10 ${cx} 150)">${c.fx}</text>
        </g><polygon points="${p.map(q => q.join(",")).join(" ")}" fill="none" stroke="#141414" stroke-width="12"/>
        ${caption(cx - 10, 800, c.name)}</g>`; });
    html += `<g class="lg" style="transform-origin:800px 400px">${burst(800, 400, 300, 470, 14, "#ff3c3c")}${burst(800, 400, 240, 360, 14, "#ffd23f")}${logo(800, 470)}</g>
      <g class="tt" style="transform-origin:800px 700px">${caption(800, 730, title, titleSize(title, 70, 1300), "#fff")}
      <text x="800" y="830" text-anchor="middle" font-family="${COMIC}" font-weight="700" font-size="40" fill="#fff" stroke="#141414" stroke-width="5" paint-order="stroke">odcinek ${num}</text></g>`;
    g.innerHTML = html;
    const pans = [...g.querySelectorAll(".pan")], lg = g.querySelector(".lg"), tt = g.querySelector(".tt");
    pans.forEach(p => p.style.opacity = 0); lg.style.opacity = 0; tt.style.opacity = 0;
    const a = ctx(), beat = 60 / 92, T = a.currentTime + 0.1;
    beat2(T, beat);
    pans.forEach((p, i) => { const d = (T + i * beat - a.currentTime) * 1000;
      A(p, [{ opacity: 0, transform: "scale(0.2) rotate(-12deg)" }, { opacity: 1, transform: "scale(1.08) rotate(2deg)", offset: 0.7 }, { opacity: 1, transform: "scale(1) rotate(0deg)" }], { duration: 320, delay: d, easing: "ease-out" });
      A(p.querySelector(".bust"), [{ transform: "translateY(260px)" }, { transform: "translateY(-20px)", offset: 0.7 }, { transform: "translateY(0)" }], { duration: 450, delay: d + 120 });
      A(p.querySelector(".fx"), [{ opacity: 0 }, { opacity: 1 }], { duration: 80, delay: d + 300 });
      p.querySelector(".bust").animate([{ transform: "translateY(0)" }, { transform: "translateY(-12px)" }], { duration: beat * 500, direction: "alternate", iterations: 12, delay: d + 600 });
    });
    scratch(T + 3 * beat, 4);
    // rozbicie kadrow
    const t4 = (T + 4 * beat - a.currentTime) * 1000;
    boom(T + 4 * beat);
    pans.forEach((p, i) => A(p, [{ transform: "translate(0,0) rotate(0deg)", opacity: 1 }, { transform: `translate(${(i - 1) * 900}px,${i === 1 ? -1100 : 300}px) rotate(${(i - 1) * 50 + 20}deg)`, opacity: 1 }], { duration: 600, delay: t4, easing: "ease-in" }));
    A(lg, [{ opacity: 0, transform: "scale(3) rotate(20deg)" }, { opacity: 1, transform: "scale(0.9) rotate(-4deg)", offset: 0.6 }, { opacity: 1, transform: "scale(1) rotate(0deg)" }], { duration: 450, delay: t4 + 100, easing: "ease-in" });
    A(g.querySelector("rect"), [{ fill: "#141414" }, { fill: "#fff" }, { fill: "#141414" }], { duration: 300, delay: t4 + 120 });
    scratch(T + 5.25 * beat, 4);
    A(tt, [{ opacity: 0, transform: "scale(0.3)" }, { opacity: 1, transform: "scale(1.1)" }, { opacity: 1, transform: "scale(1)" }], { duration: 400, delay: (T + 5.5 * beat - a.currentTime) * 1000 });
    lg.animate([{ transform: "scale(1)" }, { transform: "scale(1.05)" }], { duration: beat * 500, direction: "alternate", iterations: 6, delay: t4 + 600 });
    await wait(8 * beat * 1000 + 300);
  }

  // ================= WERSJA 2: strona komiksu z dymkami, zoom na duzy kadr z logo =================
  async function v2(g, title, num){
    const lines = ["Siema.", "No co?", "Spokojnie."];
    let html = `<rect width="1600" height="900" fill="#141414"/><defs>${dots("d2")}<clipPath id="cp2_3"><rect x="40" y="480" width="1520" height="380"/></clipPath>`;
    for (let i = 0; i < 3; i++) html += `<clipPath id="cp2_${i}"><rect x="${40 + i * 515}" y="40" width="490" height="410"/></clipPath>`;
    html += `</defs><g class="page" style="transform-origin:800px 450px"><rect x="10" y="10" width="1580" height="880" fill="#f8f3e6"/>`;
    CH.forEach((c, i) => { const x = 40 + i * 515, cx = x + 245;
      html += `<g class="pan"><g clip-path="url(#cp2_${i})"><rect x="${x}" y="40" width="490" height="410" fill="${c.bg}"/>${rays(cx, 300, 16, c.ray)}<rect x="${x}" y="40" width="490" height="410" fill="url(#d2)"/>
        ${bust(c, cx, 300, 0.75)}</g>
        <rect x="${x}" y="40" width="490" height="410" fill="none" stroke="#141414" stroke-width="8"/>
        <g class="bub">${caption(x + 110, 105, c.name, 30, "#fff6b0")}
          <g transform="translate(${x + 330},110)"><ellipse rx="130" ry="56" fill="#fff" stroke="#141414" stroke-width="5"/><path d="M-30 46 L-60 100 L10 52" fill="#fff" stroke="#141414" stroke-width="5"/><path d="M-26 44 L6 48" stroke="#fff" stroke-width="8"/>
          <text y="14" text-anchor="middle" font-family="${COMIC}" font-weight="700" font-size="40" fill="#141414">${lines[i]}</text></g></g></g>`; });
    html += `<g class="pan big"><g clip-path="url(#cp2_3)"><rect x="40" y="480" width="1520" height="380" fill="#ff5a5a"/>${rays(800, 670, 30, "#d83a3a", 1200)}<rect x="40" y="480" width="1520" height="380" fill="url(#d2)"/>
        <g class="zl" style="transform-origin:800px 640px">${logo(800, 700, 200)}</g></g>
        <rect x="40" y="480" width="1520" height="380" fill="none" stroke="#141414" stroke-width="8"/></g></g>
      <g class="tt" style="transform-origin:800px 760px">${caption(800, 790, title, titleSize(title, 64, 1300), "#fff6b0")}
        <text x="800" y="860" text-anchor="middle" font-family="${COMIC}" font-weight="700" font-size="34" fill="#fff" stroke="#141414" stroke-width="5" paint-order="stroke">odcinek ${num}</text></g>`;
    g.innerHTML = html;
    const page = g.querySelector(".page"), pans = [...g.querySelectorAll(".pan")], tt = g.querySelector(".tt");
    pans.forEach(p => p.style.opacity = 0); tt.style.opacity = 0;
    const a = ctx(), beat = 60 / 92, T = a.currentTime + 0.1, at = b => (T + b * beat - a.currentTime) * 1000;
    beat2(T, beat, { bassLine: [[0, 49], [1, 49], [1.5, 58], [2, 44], [3, 52]] });
    paper(T);
    A(page, [{ transform: "translateX(1700px) rotate(8deg)" }, { transform: "translateX(0) rotate(0deg)" }], { duration: 450, easing: "ease-out" });
    for (let i = 0; i < 3; i++){
      A(pans[i], [{ opacity: 0, transform: "translateY(-40px)" }, { opacity: 1, transform: "translateY(0)" }], { duration: 200, delay: at(0.5 + i * 1.1) });
      A(pans[i].querySelector(".bub"), [{ opacity: 0 }, { opacity: 1 }], { duration: 100, delay: at(1 + i * 1.1) });
      A(pans[i].querySelector(".bust"), [{ transform: "scale(0.6)" }, { transform: "scale(1.06)" }, { transform: "scale(1)" }], { duration: 300, delay: at(0.5 + i * 1.1) });
    }
    scratch(T + 3.25 * beat, 4);
    // duzy kadr + zoom na niego
    A(pans[3], [{ opacity: 0 }, { opacity: 1 }], { duration: 100, delay: at(4) });
    boom(T + 4 * beat);
    A(pans[3].querySelector(".zl"), [{ transform: "scale(4)", opacity: 0 }, { transform: "scale(0.92)", opacity: 1, offset: 0.7 }, { transform: "scale(1)", opacity: 1 }], { duration: 400, delay: at(4) });
    A(page, [{ transform: "translate(0,0) scale(1)" }, { transform: "translate(0,-300px) scale(1.35)" }], { duration: 700, delay: at(4.6), easing: "ease-in-out" });
    scratch(T + 5.25 * beat, 4);
    A(tt, [{ opacity: 0, transform: "scale(0.3) rotate(-6deg)" }, { opacity: 1, transform: "scale(1.1) rotate(2deg)" }, { opacity: 1, transform: "scale(1) rotate(0deg)" }], { duration: 400, delay: at(5.8) });
    await wait(8 * beat * 1000 + 300);
  }

  // ================= WERSJA 3: paski pop-art ze smugami, blysk okularow, paski sie rozjezdzaja =================
  async function v3(g, title, num, music = 1){
    const S = [[0, 300], [300, 300], [600, 300]];
    let html = `<rect width="1600" height="900" fill="#141414"/>
      <g class="back">${rays(800, 430, 24, "#2b0a0a", 1600)}${burst(800, 420, 330, 470, 16, "#ff3c3c")}${logo(800, 490, 210)}</g>
      <g class="tt" style="transform-origin:800px 700px">${caption(800, 730, title, titleSize(title, 70, 1300), "#fff")}
        <text x="800" y="830" text-anchor="middle" font-family="${COMIC}" font-weight="700" font-size="40" fill="#fff" stroke="#141414" stroke-width="5" paint-order="stroke">odcinek ${num}</text></g><defs>${dots("d3")}`;
    S.forEach(([y, h], i) => html += `<clipPath id="cp3_${i}"><polygon points="0,${y + (i ? 20 : 0)} 1600,${y - (i ? 20 : 0)} 1600,${y + h - (i < 2 ? 20 : 0)} 0,${y + h + (i < 2 ? 20 : 0)}"/></clipPath>`);
    html += `</defs>`;
    S.forEach(([y, h], i) => { const c = CH[i], left = i !== 1, hx = left ? 330 : 1270, cy = y + 150;
      let speed = ""; for (let k = 0; k < 9; k++){ const yy = y + 30 + k * 30; speed += `<path d="M${left ? 700 + k * 40 : 0} ${yy} H${left ? 1600 : 900 - k * 40}" stroke="#fff" stroke-width="${4 + (k % 3) * 3}" opacity="0.5"/>`; }
      html += `<g class="strip" style="transform-origin:800px ${cy}px"><g clip-path="url(#cp3_${i})">
        <rect y="${y - 30}" width="1600" height="${h + 60}" fill="${c.bg}"/><rect y="${y - 30}" width="1600" height="${h + 60}" fill="url(#d3)"/>
        <g class="spd">${speed}</g>
        ${bust(c, hx, cy + 20, 0.62)}
        <text class="nm" x="${left ? 1000 : 600}" y="${cy + 40}" text-anchor="middle" font-family="${IMPACT}" font-size="150" fill="#fff" stroke="#141414" stroke-width="9" paint-order="stroke" letter-spacing="6">${c.name}</text>
        <path class="gl" d="M0 -34 L8 -8 L34 0 L8 8 L0 34 L-8 8 L-34 0 L-8 -8 Z" fill="#fff" stroke="#ffd23f" stroke-width="3" style="transform:translate(${hx + (left ? 30 : -10)}px,${cy + 5}px) scale(0)"/>
        </g><path d="M0 ${y + h + (i < 2 ? 20 : 0)} L1600 ${y + h - (i < 2 ? 20 : 0)}" stroke="#141414" stroke-width="12"/></g>`; });
    g.innerHTML = html;
    const strips = [...g.querySelectorAll(".strip")], back = g.querySelector(".back"), tt = g.querySelector(".tt");
    strips.forEach(s => s.style.opacity = 0); back.style.opacity = 0; tt.style.opacity = 0;
    const a = ctx(), beat = 60 / 92, T = a.currentTime + 0.1, at = b => (T + b * beat - a.currentTime) * 1000;
    (MUSIC[music] || MUSIC[1])(T, 8 * beat + 0.3);
    strips.forEach((s, i) => { const left = i !== 1, d = at(i * 1.15);
      swoosh(T + i * 1.15 * beat);
      A(s, [{ opacity: 1, transform: `translateX(${left ? -1700 : 1700}px)` }, { opacity: 1, transform: `translateX(${left ? 40 : -40}px)`, offset: 0.8 }, { opacity: 1, transform: "translateX(0)" }], { duration: 380, delay: d, easing: "ease-out" });
      A(s.querySelector(".nm"), [{ transform: "scale(1.6)", opacity: 0 }, { transform: "scale(1)", opacity: 1 }], { duration: 250, delay: d + 300 });
      s.querySelector(".spd").animate([{ transform: "translateX(0)" }, { transform: `translateX(${left ? -120 : 120}px)` }], { duration: 300, iterations: 20, delay: d });
      const gl = s.querySelector(".gl"), tr = gl.style.transform.replace(" scale(0)", "");
      A(gl, [{ transform: `${tr} scale(0) rotate(0deg)` }, { transform: `${tr} scale(1.2) rotate(90deg)` }, { transform: `${tr} scale(0) rotate(180deg)` }], { duration: 450, delay: d + 450 });
      glint(T + i * 1.15 * beat + 0.45);
    });
    if (music === 1) scratch(T + 3.5 * beat, 4);
    // paski sie rozjezdzaja, za nimi logo
    const t4 = at(4.2);
    swoosh(T + 4.2 * beat, 0.5); boom(T + 4.4 * beat);
    A(back, [{ opacity: 0, transform: "scale(0.6)" }, { opacity: 1, transform: "scale(1)" }], { duration: 300, delay: t4 + 150 });
    strips.forEach((s, i) => A(s, [{ transform: "translate(0,0) scale(1)" }, { transform: i === 1 ? "translate(0,0) scale(2.5)" : `translate(0,${i ? 700 : -700}px) scale(1)`, opacity: i === 1 ? 0 : 1 }], { duration: 450, delay: t4, easing: "ease-in" }));
    A(tt, [{ opacity: 0, transform: "translateY(200px)" }, { opacity: 1, transform: "translateY(-15px)" }, { opacity: 1, transform: "translateY(0)" }], { duration: 400, delay: at(5.6) });
    back.animate([{ transform: "rotate(-2deg)" }, { transform: "rotate(2deg)" }], { duration: beat * 1000, direction: "alternate", iterations: 4, delay: t4 + 500 });
    await wait(8 * beat * 1000 + 300);
  }


  // ================= ZAKONCZENIE: dyskoteka z disco polo =================
  window.ziomkiOutro = async function(){
    const stage = document.getElementById("stage");
    const g = document.createElementNS(NS, "g"); stage.appendChild(g);
    const cols = ["#ff3c8a", "#ffd23f", "#3cc8ff", "#7cff5a", "#b45aff"];
    let rr = ""; for (let i = 0; i < 20; i++){ const a0 = i * Math.PI / 10, a1 = a0 + Math.PI / 20;
      rr += `<polygon points="800,120 ${800 + 1800 * Math.cos(a0)},${120 + 1800 * Math.sin(a0)} ${800 + 1800 * Math.cos(a1)},${120 + 1800 * Math.sin(a1)}" fill="${cols[i % 5]}" opacity="0.22"/>`; }
    let ball = ""; for (let y = -3; y <= 3; y++) for (let x = -3; x <= 3; x++) if (x * x + y * y <= 10) ball += `<rect x="${800 + x * 17 - 8}" y="${120 + y * 17 - 8}" width="15" height="15" fill="${(x + y) % 2 ? "#dfe3e8" : "#9aa3ad"}"/>`;
    const busts = CH.map((c, i) => bust(c, 400 + i * 400, 520, 0.55, "d" + i)).join("");
    g.innerHTML = `<rect width="1600" height="900" fill="#0b0618"/>
      <g class="rays" style="transform-origin:800px 120px">${rr}</g>
      <rect y="760" width="1600" height="140" fill="#1a1030"/>
      ${[0, 1, 2, 3, 4, 5, 6, 7].map(i => `<rect class="tile" x="${i * 200}" y="760" width="200" height="140" fill="${cols[i % 5]}" opacity="0.15"/>`).join("")}
      <path d="M800 0 V70" stroke="#ccc" stroke-width="4"/>
      <g class="ball" style="transform-origin:800px 120px"><circle cx="800" cy="120" r="62" fill="#b8bec6" stroke="#141414" stroke-width="5"/>${ball}</g>
      <g class="dancers">${busts}</g>
      <g class="kon" style="transform-origin:800px 330px"><text x="800" y="380" text-anchor="middle" font-family="${IMPACT}" font-size="190" fill="#ff3c8a" stroke="#000" stroke-width="10" paint-order="stroke" letter-spacing="8">KONIEC</text></g>
      <g class="zl" style="transform-origin:800px 840px">${logo(800, 870, 110)}</g>`;
    const rays = g.querySelector(".rays"), kon = g.querySelector(".kon"), zl = g.querySelector(".zl");
    const a = ctx(), b = 60 / 128, T = a.currentTime + 0.1, dur = 16 * b;
    MUSIC[2](T, dur);
    lead(T + dur, N(57), 0.9, { type: "sawtooth", vol: 0.05, vib: 6 }); lead(T + dur, N(64), 0.9, { type: "sawtooth", vol: 0.04 }); lead(T + dur, N(69), 0.9, { type: "square", vol: 0.03 }); crash(T + dur);
    A(g, [{ opacity: 0 }, { opacity: 1 }], { duration: 300 });
    rays.animate([{ transform: "rotate(0deg)" }, { transform: "rotate(360deg)" }], { duration: 9000, iterations: Infinity });
    g.querySelector(".ball").animate([{ transform: "rotate(0deg)" }, { transform: "rotate(360deg)" }], { duration: 3000, iterations: Infinity });
    g.querySelectorAll(".tile").forEach((t, i) => t.animate([{ opacity: 0.08 }, { opacity: 0.6 }], { duration: b * 1000, direction: "alternate", iterations: Infinity, delay: (i % 2) * b * 1000 }));
    g.querySelectorAll(".bust").forEach((d, i) => d.animate([{ transform: "translateY(0) rotate(-6deg)" }, { transform: "translateY(-34px) rotate(6deg)" }], { duration: b * 1000, direction: "alternate", iterations: Infinity, easing: "ease-in-out", delay: i * b * 330 }));
    A(kon, [{ transform: "scale(0) rotate(-20deg)" }, { transform: "scale(1.15) rotate(4deg)" }, { transform: "scale(1) rotate(0deg)" }], { duration: 500 });
    kon.animate([{ transform: "scale(1)" }, { transform: "scale(1.08)" }], { duration: b * 500, direction: "alternate", iterations: Infinity, delay: 500 });
    A(zl, [{ transform: "translateY(200px)" }, { transform: "translateY(0)" }], { duration: 500, delay: b * 4000, easing: "ease-out" });
    await wait(dur * 1000 + 1200);
    await g.animate([{ opacity: 1 }, { opacity: 0 }], { duration: 500, fill: "forwards" }).finished.catch(() => {});
    g.getAnimations({ subtree: true }).forEach(x => x.cancel());
    g.remove();
  };

  window.ziomkiIntro2 = async function(title, num, variant = 1, music = 1){
    const stage = document.getElementById("stage");
    const g = document.createElementNS(NS, "g"); stage.appendChild(g);
    await [v1, v2, v3][variant - 1](g, title, num, music);
    await g.animate([{ opacity: 1 }, { opacity: 0 }], { duration: 500, fill: "forwards" }).finished.catch(() => {});
    g.getAnimations({ subtree: true }).forEach(x => x.cancel());
    g.remove();
  };
})();
