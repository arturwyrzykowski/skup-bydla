// Wspolne intro serii "ZIOMKI": litery spadaja, glowy podskakuja, gitara sie buja,
// ~5 s bitu hip-hop ze skreczami DJ-a i przesterowana gitara. Uzycie: await ziomkiIntro("TYTUL", nr)
(function(){
  const NS = "http://www.w3.org/2000/svg";
  const wait = ms => new Promise(r => setTimeout(r, ms));
  const ctx = () => (typeof ac === "function") ? ac() : (window._ziCtx = window._ziCtx || new (window.AudioContext || window.webkitAudioContext)());

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
  function guitar(t, f, dur){
    const a = ctx();
    if (!curve){ curve = new Float32Array(1024); for (let i = 0; i < 1024; i++) curve[i] = Math.tanh((i / 512 - 1) * 6); }
    const ws = a.createWaveShaper(); ws.curve = curve;
    const lp = a.createBiquadFilter(); lp.type = "lowpass"; lp.frequency.value = 2600;
    const g = a.createGain(); g.gain.setValueAtTime(0.0001, t); g.gain.linearRampToValueAtTime(0.13, t + 0.01); g.gain.exponentialRampToValueAtTime(0.001, t + dur);
    [f, f * 1.5, f * 2].forEach(fr => { const o = a.createOscillator(); o.type = "sawtooth"; o.frequency.value = fr; o.detune.value = Math.random() * 8 - 4; o.connect(ws); o.start(t); o.stop(t + dur + 0.02); });
    ws.connect(lp); lp.connect(g); g.connect(a.destination);
  }

  function build(title, num){
    const W = { Z: 99, I: 53, O: 106, M: 125, K: 104 }, gap = 14, word = "ZIOMKI";
    let x = 800 - (word.split("").reduce((s, c) => s + W[c], 0) + gap * 5) / 2;
    const letters = word.split("").map(c => { const cx = x + W[c] / 2; x += W[c] + gap;
      return `<text class="zl" x="${cx}" y="450" text-anchor="middle" font-family="Impact, 'Arial Black', sans-serif" font-size="190" fill="#ffd23f" stroke="#000" stroke-width="8" paint-order="stroke">${c}</text>`; }).join("");
    const fs = Math.min(110, Math.floor(860 / (title.length * 0.47)));
    const g = document.createElementNS(NS, "g");
    g.innerHTML = `
      <rect width="1600" height="900" fill="#111"/>
      <polygon points="300,0 520,0 900,900 200,900" fill="#fff" opacity="0.05"/>
      <polygon points="1080,0 1300,0 1400,900 700,900" fill="#fff" opacity="0.05"/>
      <g class="zhs">
        <image href="glowa1.png" x="560" y="80" width="130" height="160"/>
        <image href="glowa2.png" x="735" y="96" width="127" height="140"/>
        <image href="glowa3.png" x="905" y="92" width="134" height="145"/>
      </g>
      <g class="zword">${letters}</g>
      <g class="zgtr" style="transform-origin:1320px 620px" stroke="#141414" stroke-width="5" stroke-linejoin="round">
        <rect x="1310" y="200" width="22" height="340" fill="#8a5a32"/>
        <path d="M1300 200 h42 l-6 -60 h-30 z" fill="#2b2b2b"/>
        <path d="M1321 530 C1290 530 1285 500 1262 505 C1240 510 1248 560 1262 590 C1230 620 1225 700 1270 740 C1300 770 1345 770 1375 740 C1415 700 1410 625 1382 595 C1395 565 1405 520 1385 510 C1365 500 1352 530 1321 530 Z" fill="#d01616"/>
        <path d="M1290 560 C1300 580 1340 580 1352 560 L1360 700 C1340 720 1300 720 1284 700 Z" fill="#f4f4f2" stroke-width="3"/>
        <rect x="1300" y="610" width="42" height="14" fill="#f4f4f2"/><rect x="1300" y="660" width="42" height="14" fill="#f4f4f2"/>
        <path d="M1316 200 V720 M1326 200 V720" stroke="#e8e8e8" stroke-width="2"/>
      </g>
      <g class="ztitle" style="transform-origin:800px 600px">
        <text x="800" y="630" text-anchor="middle" font-family="Impact, 'Arial Black', sans-serif" font-size="${fs}" fill="#fff" stroke="#000" stroke-width="6" paint-order="stroke">${title}</text>
      </g>
      <text x="800" y="720" text-anchor="middle" font-family="'Comic Sans MS', sans-serif" font-size="36" fill="#fff">odcinek ${num}</text>`;
    return g;
  }

  window.ziomkiIntro = async function(title, num){
    const stage = document.getElementById("stage");
    const g = build(title, num); stage.appendChild(g);
    const letters = [...g.querySelectorAll(".zl")], heads = [...g.querySelectorAll(".zhs image")];
    const gtr = g.querySelector(".zgtr"), ttl = g.querySelector(".ztitle");
    const anims = [];
    letters.forEach((l, k) => anims.push(l.animate(
      [{ transform: "translateY(-600px)", opacity: 0 }, { transform: "translateY(30px)", opacity: 1, offset: 0.7 }, { transform: "translateY(0)", opacity: 1 }],
      { duration: 500, delay: 120 + k * 170, fill: "both", easing: "ease-in" })));
    heads.forEach((h, k) => anims.push(h.animate([{ transform: "translateY(0)" }, { transform: "translateY(-24px)" }], { duration: 333, direction: "alternate", iterations: Infinity, delay: k * 111 })));
    anims.push(gtr.animate([{ transform: "rotate(-12deg)" }, { transform: "rotate(12deg)" }], { duration: 667, direction: "alternate", iterations: Infinity, easing: "ease-in-out" }));
    ttl.animate([{ transform: "scale(0.3)", opacity: 0 }, { transform: "scale(1.15)", opacity: 1 }, { transform: "scale(1)" }], { duration: 700, fill: "both" });

    const a = ctx(), T = a.currentTime + 0.1, beat = 60 / 90;
    for (let bar = 0; bar < 2; bar++){
      const b0 = T + bar * 4 * beat;
      [0, 2, 2.5].forEach(x => kick(b0 + x * beat));
      [1, 3].forEach(x => snare(b0 + x * beat));
      for (let e = 0; e < 8; e++) hat(b0 + e * beat / 2);
      [[0, 55], [1.5, 65], [2, 49], [3, 58]].forEach(([x, f]) => bass(b0 + x * beat, f, beat * 0.9));
      [[0, 82.4, 0.5], [0.5, 82.4, 0.5], [1, 98, 0.5], [2, 110, 0.5], [2.5, 110, 0.5], [3, bar ? 123.5 : 98, 0.9]].forEach(([x, f, d]) => guitar(b0 + x * beat, f, d * beat));
      [1.25, 3.25].forEach(x => {
        scratch(b0 + x * beat, bar === 1 && x > 3 ? 6 : 4);
        setTimeout(() => {
          ttl.animate([{ transform: "translateX(0)" }, { transform: "translateX(-26px)" }, { transform: "translateX(22px)" }, { transform: "translateX(-14px)" }, { transform: "translateX(0)" }], { duration: 440 });
          gtr.animate([{ transform: "rotate(0deg) scale(1)" }, { transform: "rotate(-25deg) scale(1.08)" }, { transform: "rotate(0deg) scale(1)" }], { duration: 440 });
        }, (b0 + x * beat - a.currentTime) * 1000);
      });
    }
    await wait(8 * beat * 1000 + 300);
    await g.animate([{ opacity: 1 }, { opacity: 0 }], { duration: 600, fill: "forwards" }).finished.catch(() => {});
    anims.forEach(x => x.cancel());
    g.remove();
  };
})();
