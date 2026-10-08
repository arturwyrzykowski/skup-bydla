  // ===== SCENARIUSZ: WODA MINERALNA =====
  const stops = [];
  const keep = f => (stops.push(f), f);
  function stopAll(){ while (stops.length) { try { stops.pop()(); } catch (e) {} } }
  const MET = "#6b6a3e";
  const show = (id, on = true) => { $(id).style.display = on ? "" : "none"; };
  function tween(ms, fn){
    return new Promise(res => { const t0 = performance.now();
      const step = now => { const k = Math.min(1, (now - t0) / ms); fn(k); if (k < 1) requestAnimationFrame(step); else res(); };
      requestAnimationFrame(step); });
  }
  // grupa "...W": translate + scale (f = -1 -> odbita, patrzy w lewo)
  const pos = {};
  const trf = p => `translate(${p.x}px,${p.y}px) scale(${p.s * p.f},${p.s})`;
  function place(id, x, y, s, f = 1){ pos[id] = { x, y, s, f }; $(id).getAnimations().forEach(a => a.cancel()); $(id).style.transform = trf(pos[id]); }
  function face(id, f){ pos[id].f = f; $(id).getAnimations().forEach(a => a.cancel()); $(id).style.transform = trf(pos[id]); }
  async function move(id, x, y, ms, easing = "linear"){
    const p = pos[id], from = trf(p);
    pos[id] = { ...p, x, y };
    await anim($(id), [{ transform: from }, { transform: trf(pos[id]) }], { duration: ms, easing });
  }
  function walk(pid, on){
    const el = $(pid); if (!el) return;
    el.querySelectorAll(".legL, .legR").forEach((l, i) => { l.getAnimations().forEach(a => a.cancel());
      if (on) l.animate([{ transform: `rotate(${i ? 14 : -14}deg)` }, { transform: `rotate(${i ? -14 : 14}deg)` }], { duration: 280, direction: "alternate", iterations: Infinity }); });
    const b = el.querySelector(".bob"); b.getAnimations().forEach(a => a.cancel());
    if (on) b.animate([{ transform: "translateY(0)" }, { transform: "translateY(-10px)" }], { duration: 140, direction: "alternate", iterations: Infinity });
  }
  async function walkTo(pid, wid, x, ms, y){ walk(pid, true); const st = every(300, sfx.krok); await move(wid, x, y ?? pos[wid].y, ms); st(); walk(pid, false); }
  function wheels(sel, on, ms = 900, dir = 1){
    document.querySelectorAll(sel).forEach(w => { w.getAnimations().forEach(a => a.cancel());
      if (on) w.animate([{ transform: "rotate(0deg)" }, { transform: `rotate(${dir * 360}deg)` }], { duration: ms, iterations: Infinity }); });
  }
  const kola = sh => `#${sh} .kR, #${sh} .kF, #${sh} .kB`;
  // muchy kraza wokol beczki
  function muchy(id){
    document.querySelectorAll(`#${id} .mucha`).forEach(m => { m.getAnimations().forEach(a => a.cancel());
      const fr = []; for (let i = 0; i <= 6; i++) fr.push({ transform: `translate(${(Math.random() - .5) * 90}px,${(Math.random() - .5) * 60}px)` });
      fr[6] = fr[0];
      m.animate(fr, { duration: 1400 + Math.random() * 900, iterations: Infinity }); });
  }
  // ---------- dzwieki odcinka ----------
  const ring = () => [0, .35].forEach(w => { tone(1320, .25, "square", .04, null, w); tone(1760, .25, "square", .03, null, w + .05); });
  const bzz = () => loop(() => { if (Math.random() < .5) tone(190 + Math.random() * 60, .25, "sawtooth", .012, 210 + Math.random() * 60); });
  const pompa = () => loop(() => { if (Math.random() < .7) noise(0.12, { freq: 180 + Math.random() * 60, q: 2, vol: 0.18 }); });
  const lanie = () => loop(() => noise(0.15, { freq: 900 + Math.random() * 300, q: .8, vol: 0.12 }));
  const gwizdek = () => { tone(2800, .7, "square", .05, 2900); tone(2830, .7, "sine", .06, 2950); };
  const slurp = () => { noise(.4, { freq: 600, q: 3, vol: .3, sweepTo: 2400 }); tone(300, .3, "sine", .2, 1200); };
  const kum = () => [0, .25].forEach(w => tone(180, .14, "square", .06, 120, w));
  const trzask = () => { [0, .05, .12, .2, .3].forEach(w => noise(.18, { freq: 1500 + Math.random() * 2500, q: 1, vol: .35, when: w })); tone(120, .4, "sine", .4, 50); };
  const ding = () => { tone(2600, .6, "sine", .12); tone(3900, .4, "sine", .05, null, .05); };
  const klakson = () => [0, .3].forEach(w => { tone(420, .22, "sawtooth", .07, null, w); tone(530, .22, "square", .04, null, w); });
  const plusk = () => noise(.3, { freq: 1800, q: 1, vol: .18, sweepTo: 500 });
  function kogut(){
    [[520, 760, 0, .16], [760, 900, .2, .16], [900, 1040, .4, .2], [1040, 640, .66, .9]].forEach(([f, f2, w, d]) => {
      tone(f, d, "sawtooth", .07, f2, w); tone(f * 2, d, "square", .015, f2 * 2, w); noise(d, { freq: f * 2, q: 3, vol: .06, when: w });
    });
  }
  function wiwat(){ for (let i = 0; i < 9; i++) { tone(500 + Math.random() * 400, .9, "sawtooth", .018, 700 + Math.random() * 500, i * .03); } noise(1.2, { freq: 1500, q: .6, vol: .2 }); }
  // wszyscy harcerze otwieraja usta (okrzyk)
  function chor(on){
    document.querySelectorAll(".dzieciak").forEach(d => { const c = d.querySelector(".mC"), o = d.querySelector(".mO");
      if (c && o) { c.style.display = on ? "none" : ""; o.style.display = on ? "" : "none"; } });
  }
  // wajcha: z 1 na R (zblizenie, jak w "Wodzie pitnej")
  async function wajcha(){
    shot("shWajcha", { x: 800, y: 560, k: 1 });
    $("wajcha").style.transform = "rotate(-27deg)";
    await crash({ x: 800, y: 500, k: 1.25 });
    await sleep(400);
    await anim($("wajcha"), [{ transform: "rotate(-27deg)" }, { transform: "rotate(-27deg) translateY(30px)", offset: .3 }, { transform: "rotate(27deg) translateY(30px)", offset: .75 }, { transform: "rotate(27deg)" }],
               { duration: 900, easing: "ease-in-out" });
    sfx.bum(); shake(10, 300);
    await sleep(600);
  }
  const oczy = (pid, wink) => { const el = $(pid); el.querySelector(".oczyN").style.display = wink ? "none" : ""; el.querySelector(".oczyW").style.display = wink ? "" : "none"; };

  // ---------- 1. telefon z plebanii ----------
  async function partTelefon(){
    shot("shTelefon", { x: 800, y: 450, k: 1 });
    $("rTelP").getAnimations().forEach(a => a.cancel()); $("aTelP").classList.remove("strach");
    await fadeIn(500);
    await caption("Plebania.", 1400);
    ring(); await sleep(900); ring();
    await sleep(700);
    await line("k", "Szczęść Boże, Andrzejku. Tu proboszcz.", 300, "kTelP");
    await line("a", "Szczęść Boże, proszę księdza.", 300, "aTelP");
    await camTo({ x: 420, y: 560, k: 1.3 }, 600);
    await line("k", "Harcerze mają obóz na łące nad rzeką, a wody nie mają. Ani się umyć, ani napić.", 300, "kTelP");
    await line("k", "Zawieźlibyście im beczkę wody? Tylko z kranu, synu. Czystej, z kranu.", 300, "kTelP");
    // Triwet nachyla sie do telefonu
    await camTo({ x: 1180, y: 520, k: 1.6 }, 500);
    const el = $("rTelP"); el.style.transformBox = "fill-box"; el.style.transformOrigin = "50% 100%";
    await anim(el, [{ transform: "rotate(0deg)" }, { transform: "rotate(-16deg) translateX(-40px)" }], { duration: 300 });
    await crash({ x: 1200, y: 470, k: 2.3 });
    await line("r", "Nie ma problemu, klecho, kurwauuu!", 200, "rTelP");
    $("aTelP").classList.add("strach");
    await camTo({ x: 1110, y: 480, k: 2.0 }, 300);
    await sleep(500);
    await camTo({ x: 420, y: 560, k: 1.5 }, 200);
    await line("k", "Halo? Coś przerywa, synu… No to z Bogiem, chłopcy!", 300, "kTelP");
    await camTo({ x: 1180, y: 500, k: 1.5 }, 300);
    anim(el, [{ transform: "rotate(-16deg) translateX(-40px)" }, { transform: "rotate(0deg)" }], { duration: 300 });
    await line("a", "Pojebało cię?", 200, "aTelP");
    $("aTelP").classList.remove("strach");
    await line("r", "No co? Załatwione.", 600, "rTelP");
    await fadeOut(500);
  }

  // ---------- 2. podworko Stivena ----------
  async function partPodworko(){
    shot("shPodworko", { x: 640, y: 520, k: 1 });
    place("uPodW", 240, 790, .62); place("rPodW", 420, 800, .62, -1); place("sPodW", 540, 800, .62, -1);
    muchy("muPod"); const bz = keep(bzz());
    await fadeIn(500);
    await caption("Podwórko u Stivena.", 1600);
    await camTo({ x: 360, y: 560, k: 1.8 }, 900);
    await line("r", "Stiven, ksiądz prosi, żeby harcerzom wodę zawieźć. Nalejemy u ciebie z kranu?", 300, "rPodP");
    await crash({ x: 250, y: 520, k: 2.6 });
    await line("u", "Z kranu?! Pojebało was? Toż to majątek będzie kosztowało!", 300, "uPodP");
    await camTo({ x: 330, y: 560, k: 1.9 }, 400);
    await line("u", "Z rzeki nabierzcie. Tylko beczkę na wodę od kogoś pożyczcie.", 300, "uPodP");
    face("uPodW", -1);
    walkTo("uPodP", "uPodW", -300, 2200);
    await sleep(900);
    face("rPodW", 1);
    await camTo({ x: 520, y: 560, k: 1.9 }, 600);
    await line("r", "Jebać. Bierzemy beczkę od szamba. Przemalowana na WODA PITNA, nikt się nie skapnie.", 300, "rPodP");
    await crash({ x: 760, y: 560, k: 2.2 });
    await sleep(1400);
    await camTo({ x: 560, y: 560, k: 1.9 }, 500);
    await line("s", "Ty to masz łeb, Triwet.", 600, "sPodP");
    await fadeOut(500); stopAll();
  }

  // ---------- 3. nad rzeka ----------
  async function partRzeka(){
    shot("shRzeka", { x: 1200, y: 520, k: 1 });
    show("zaba", false);
    const eng = silnik(1.4); keep(() => eng.stop());
    keep(pompa());
    $("wir").firstElementChild.animate([{ transform: "scale(1)", opacity: 1 }, { transform: "scale(2.4)", opacity: .2 }], { duration: 900, iterations: Infinity });
    $("wir").firstElementChild.style.transformBox = "fill-box"; $("wir").firstElementChild.style.transformOrigin = "center";
    await fadeIn(500);
    await caption("Nad rzeką.", 1500);
    await camTo({ x: 1100, y: 600, k: 1.6 }, 900);
    await line("s", "Triwet, ta woda jest jakaś zielona.", 300, "sRzP");
    await camTo({ x: 1700, y: 520, k: 2.2 }, 500);
    await line("r", "Zielona, czyli zdrowa. Same witaminy.", 300, "rRzRP");
    // zaba wciagnieta przez waz
    await camTo({ x: 920, y: 700, k: 2.6 }, 700);
    show("zaba"); kum();
    await sleep(900);
    slurp();
    await anim($("zaba"), [{ transform: "translate(0px,0px) scale(1)" }, { transform: "translate(60px,30px) scale(.2)" }], { duration: 400, easing: "ease-in" });
    show("zaba", false);
    await crash({ x: 1180, y: 560, k: 2.4 });
    await line("s", "Kurwa, żabę wciągnęło!", 200, "sRzP");
    await camTo({ x: 1700, y: 520, k: 2.2 }, 300);
    await line("r", "To białko. Też zdrowe. Wsiadaj.", 600, "rRzRP");
    await fadeOut(500); stopAll();
  }

  // ---------- 4. waska sciezka przez las ----------
  async function partLas(){
    shot("shLas", { x: 800, y: 500, k: 1 });
    const eng = silnik(1.2); keep(() => eng.stop());
    wheels(kola("shLas"), true, 800);
    place("trLasW", 560, 760, .5);
    $("trLasW").animate([{ transform: "translate(560px,760px) scale(.5) rotate(0deg)" }, { transform: "translate(560px,750px) scale(.5) rotate(-1deg)" }],
                        { duration: 260, direction: "alternate", iterations: Infinity });
    $("lasTyl").animate([{ transform: "translateX(0px)" }, { transform: "translateX(-1800px)" }], { duration: 9000, fill: "forwards" });
    $("lasPrzod").animate([{ transform: "translateX(0px)" }, { transform: "translateX(-4200px)" }], { duration: 9000, fill: "forwards" });
    await fadeIn(500);
    await caption("Skrót przez las.", 1500);
    await camTo({ x: 520, y: 520, k: 1.7 }, 1500);
    await sleep(800);
    await fadeOut(250);
    // w kabinie
    shot("shKabina", { x: 800, y: 470, k: 1 });
    show("galazUderz", false);
    $("kabLiscie").animate([{ transform: "translateX(0px)" }, { transform: "translateX(-900px)" }], { duration: 1600, iterations: Infinity });
    $("kabRW").animate([{ transform: "translate(640px,990px) scale(1.4)" }, { transform: "translate(640px,978px) scale(1.4)" }], { duration: 230, direction: "alternate", iterations: Infinity });
    await fadeIn(250);
    await sleep(500);
    await line("s", "Triwet, kurwa, ciasno tu jak w puszce!", 200, "kabSP");
    await line("r", "Nie marudź. Uważaj, gałąź!", 100, "kabRP");
    show("galazUderz"); trzask(); shake(20, 400);
    await anim($("galazUderz"), [{ transform: "translateX(1900px)" }, { transform: "translateX(-200px)" }], { duration: 450, easing: "ease-out" });
    $("kabSP").classList.add("strach");
    await sleep(500);
    await line("s", "Ała! Kurwa mać!", 500, "kabSP");
    $("kabSP").classList.remove("strach");
    await fadeOut(400); stopAll();
    wheels(kola("shLas"), false);
  }

  // ---------- 5. oboz harcerski ----------
  const HARC = [...document.querySelectorAll("#shOboz .dzieciak")].map(d => d.id.replace(/P$/, "W"));
  const pidOf = w => w.replace(/W$/, "P");
  async function partOboz(){
    shot("shOboz", { x: 1300, y: 500, k: .6 });
    show("flaszkaLot", false); show("wazOb", false); show("strumien", false);
    $("wannaWoda").setAttribute("opacity", 0); $("smrod").style.opacity = 0;
    place("trObW", -1100, 780, .5); place("oObW", 220, 800, .62);
    HARC.forEach(h => { const w = $(h).getAttribute("transform").match(/translate\(([-\d.]+),([-\d.]+)\)/); place(h, +w[1], +w[2], .4); });
    // zycie obozu: ogien, pilka, flaga, podskoki
    document.querySelectorAll("#ognisko .fl").forEach((f, i) => f.animate([{ transform: "scaleY(1)" }, { transform: `scaleY(${1.15 + i * .1}) skewX(${i % 2 ? 4 : -4}deg)` }], { duration: 180 + i * 60, direction: "alternate", iterations: Infinity }));
    keep(every(400, () => puff(1500, 640, { col: "#9a9a9a", r: 14, up: 200, dx: 40, ms: 2200, op: .5 })));
    $("pilka").animate([{ transform: "translate(-180px,300px)" }, { transform: "translate(0px,0px)", offset: .5 }, { transform: "translate(180px,300px)" }],
                       { duration: 1300, direction: "alternate", iterations: Infinity, easing: "linear" });
    $("flaga").animate([{ transform: "skewY(0deg) scaleX(1)" }, { transform: "skewY(4deg) scaleX(.94)" }], { duration: 500, direction: "alternate", iterations: Infinity });
    [5, 7, 8].forEach(i => $(`hk${i}P`).querySelector(".bob").animate([{ transform: "translateY(0)" }, { transform: "translateY(-40px)" }], { duration: 650, direction: "alternate", iterations: Infinity, delay: i * 90 }));
    muchy("muOb"); show("muOb", false);
    await fadeIn(600);
    await caption("Obóz harcerski. Łąka nad rzeką.", 2000);
    // wjazd przez brame
    const eng = silnik(1.2); keep(() => eng.stop());
    wheels(kola("shOboz"), true, 800);
    camTo({ x: 700, y: 520, k: .8 }, 4500);
    await move("trObW", 1250, 780, 6000, "ease-out");
    wheels(kola("shOboz"), false); eng.set(.7);
    // opiekun gwizdze i podchodzi
    await camTo({ x: 800, y: 560, k: 1.1 }, 700);
    gwizdek(); await sleep(700);
    await walkTo("oObP", "oObW", 1060, 2200);
    await camTo({ x: 1160, y: 520, k: 2.0 }, 600);
    await line("o", "Czuwaj! Chłopaki, bardzo dziękujemy za pomoc!", 300, "oObP");
    await line("o", "Postawcie beczkę przy wannie, tam się będą myć.", 300, "oObP");
    await line("r", "Robi się, druhu.", 300, "obRP");
    // wajcha na R i cofanie do wanny
    await wajcha();
    shot("shOboz", { x: 800, y: 540, k: 1.05 });
    face("oObW", -1);
    walkTo("oObP", "oObW", 150, 2400);
    eng.set(1.2); wheels(kola("shOboz"), true, 800, -1);
    await move("trObW", 1005, 780, 3200, "ease-in-out");
    wheels(kola("shOboz"), false); eng.set(.7);
    face("oObW", 1);
    // nalewanie
    $("wazOb").setAttribute("d", "M645 705 Q610 630 545 640 Q506 646 498 660");
    $("strumien").setAttribute("d", "M498 660 Q494 672 492 682");
    show("wazOb"); sfx.drzwi();
    await camTo({ x: 520, y: 600, k: 1.9 }, 800);
    show("strumien"); const la = keep(lanie());
    $("strumien").animate([{ strokeWidth: 10 }, { strokeWidth: 15 }], { duration: 120, direction: "alternate", iterations: Infinity });
    await tween(2600, k => $("wannaWoda").setAttribute("opacity", .95 * k));
    la(); stops.pop(); show("strumien", false);
    // smrod
    $("smrod").animate([{ opacity: 0, transform: "translateY(20px)" }, { opacity: .9, transform: "translateY(-20px)" }], { duration: 2000, fill: "forwards" });
    show("muOb"); const bz = keep(bzz());
    await sleep(1200);
    await camTo({ x: 600, y: 540, k: 1.4 }, 600);
    await line("o", "Panowie… a co tu tak śmierdzi?", 300, "oObP");
    await camTo({ x: 980, y: 520, k: 2.2 }, 500);
    await line("r", "To minerały tak pachną. Woda z siedemdziesięciu metrów pod ziemią. Najzdrowsza.", 200, "obRP");
    await line("s", "Siarka. Na wszystko pomaga.", 400, "obSP");
    await camTo({ x: 400, y: 560, k: 1.6 }, 500);
    await line("o", "Słyszeliście, harcerze? Woda mineralna!", 200, "oObP");
    // wiwat i kolejka do wanny
    await camTo({ x: 700, y: 520, k: .75 }, 600);
    chor(true); wiwat();
    await sleep(900); chor(false);
    const order = HARC.slice().sort((p, q) => pos[p].x - pos[q].x);
    const kolej = order.map((h, i) => [h, 360 - i * 58]);
    camTo({ x: 300, y: 560, k: 1.0 }, 2600);
    await Promise.all(kolej.map(([h, x], i) => sleep(i * 60).then(async () => {
      face(h, pos[h].x > x ? -1 : 1); walk(pidOf(h), true);
      await move(h, x, 830 + (i % 2) * 6, 1200 + Math.abs(pos[h].x - x) * .9);
      walk(pidOf(h), false); face(h, -1);
    })));
    // mycie twarzy: pierwszy w kolejce nachyla sie nad wanna
    await camTo({ x: 420, y: 600, k: 1.9 }, 600);
    for (let n = 0; n < 3; n++){
      const h = kolej[n][0], b = $(pidOf(h)).querySelector(".bob");
      await anim(b, [{ transform: "rotate(0deg)" }, { transform: "rotate(-28deg) translateX(-30px)" }], { duration: 300 });
      for (let j = 0; j < 5; j++){ plusk(); puff(330, 650, { col: MET, r: 9, up: 50, dx: (Math.random() - .5) * 90, ms: 600, op: .9, stroke: true }); await sleep(180); }
      await anim(b, [{ transform: "rotate(-28deg) translateX(-30px)" }, { transform: "rotate(0deg)" }], { duration: 300 });
      if (n === 0) await line("h", "Ale orzeźwia!", 100, pidOf(h));
      // odchodzi z kolejki, reszta sie przesuwa
      face(h, 1); move(h, pos[h].x + 60, 900, 600);
      kolej.slice(n + 1).forEach(([k2]) => move(k2, pos[k2].x + 58, pos[k2].y, 500));
      await sleep(550);
    }
    // flaszka w podziece
    await camTo({ x: 700, y: 540, k: 1.5 }, 600);
    await walkTo("oObP", "oObW", 820, 1700);
    await line("o", "A to dla was, za fatygę.", 200, "oObP");
    show("flaszkaLot");
    await anim($("flaszkaLot"), [{ transform: "translate(880px,640px) rotate(0deg)" }, { transform: "translate(950px,500px) rotate(-20deg)", offset: .5 }, { transform: "translate(985px,560px) rotate(0deg)" }], { duration: 700 });
    show("flaszkaLot", false); sfx.kieliszek();
    await camTo({ x: 980, y: 520, k: 2.2 }, 400);
    await line("r", "Bóg zapłać, druhu!", 300, "obRP");
    // odjazd
    $("wazOb").style.display = "none";
    eng.set(1.4); wheels(kola("shOboz"), true, 700);
    camTo({ x: 1600, y: 520, k: .9 }, 3000);
    klakson();
    await move("trObW", 3300, 780, 4200, "ease-in");
    await fadeOut(500); stopAll();
    wheels(kola("shOboz"), false);
  }

  // ---------- 6. droga obok kosciola: ksiadz kciuk w gore ----------
  async function partDroga(){
    shot("shDroga", { x: 800, y: 470, k: 1 });
    const eng = silnik(1.3); keep(() => eng.stop());
    wheels(kola("shDroga"), true, 700);
    place("trDrW", -900, 830, .5);
    const jazda = move("trDrW", 2600, 830, 11500);
    await fadeIn(400);
    await sleep(2600);
    // zblizenie na ksiedza
    shot("shKsiadzCu", { x: 800, y: 470, k: 1 });
    oczy("kCuP", false); show("blysk", false);
    await crash({ x: 880, y: 470, k: 1.15 });
    await sleep(300);
    oczy("kCuP", true); ding(); show("blysk");
    $("blysk").setAttribute("transform", "translate(950,190)");
    $("blysk").animate([{ transform: "translate(950px,190px) scale(0) rotate(0deg)" }, { transform: "translate(950px,190px) scale(1.3) rotate(90deg)" }, { transform: "translate(950px,190px) scale(0) rotate(180deg)" }], { duration: 700, fill: "forwards" });
    await line("k", "Dobra robota, chłopcy! Bóg wam zapłać!", 300, "kCuP");
    oczy("kCuP", false);
    shot("shDroga", { x: 800, y: 470, k: 1 });
    klakson();
    await line("r", "Szczęść Boże, klecho!", 300, "drRP");
    await jazda;
    await fadeOut(500); stopAll();
    wheels(kola("shDroga"), false);
  }

  // ---------- 7. nastepnego dnia rano: gazeta ----------
  async function partRano(){
    shot("shRano", { x: 800, y: 470, k: 1 });
    place("lRanoW", 1900, 790, .62, -1);
    $("lRanoP").querySelector(".gazeta").style.display = "";
    $("uRanoP").querySelector(".kubek").style.display = "";
    muchy("muRano"); const bz = keep(bzz());
    await caption("Następnego dnia rano.", 1800);
    await fadeIn(600);
    kogut();
    await sleep(1600);
    await walkTo("lRanoP", "lRanoW", 620, 3800);
    await camTo({ x: 500, y: 540, k: 1.7 }, 600);
    await line("l", "Dzień dobry, panie Stiven! Gazetka, świeżutka.", 200, "lRanoP");
    await line("u", "Dzięki.", 300, "uRanoP");
    $("lRanoP").querySelector(".gazeta").style.display = "none"; sfx.whoosh();
    await sleep(400);
    // gazeta w zblizeniu
    shot("shGazeta", { x: 800, y: 470, k: 1 });
    await camTo({ x: 800, y: 260, k: 1.6 }, 1200);
    await line("u", "Zatrucie na obozie harcerskim… Salmonella i bakterie coli w wodzie mineralnej…", 200, "uRanoP");
    await camTo({ x: 530, y: 640, k: 1.8 }, 900);
    await line("u", "Sanepid szuka niebieskiej beczki z napisem WODA PITNA…", 300, "uRanoP");
    // powolny obrot glowy na beczke na podworku
    shot("shBeczkaCu", { x: 760, y: 560, k: 1 });
    muchy("muCu");
    sfx.syrena(2400);
    await camTo({ x: 760, y: 560, k: 1.25 }, 2200);
    shot("shRano", { x: 380, y: 520, k: 2.6 });
    $("uRanoP").classList.add("strach");
    await line("u", "O ja pierdolę… Triwet!", 200, "uRanoP");
    $("uRanoP").querySelector(".kubek").style.display = "none"; sfx.chlup();
    await freeze(1500);
    await fadeOut(700); stopAll();
    $("uRanoP").classList.remove("strach");
  }

  // napis koncowy
  async function credit(){
    $("chNr").textContent = ""; $("chTitle").textContent = "SiKet produkcja";
    $("chapter").style.display = "";
    await anim($("chapter"), [{ opacity: 0 }, { opacity: 1 }], { duration: 400 });
    await sleep(2800);
    await anim($("chapter"), [{ opacity: 1 }, { opacity: 0 }], { duration: 400 });
    $("chapter").style.display = "none";
  }

  async function play(){
    $("startScreen").hidden = true; $("endScreen").hidden = true; ac();
    stopAll();
    $("fade").style.opacity = 1;
    const h = location.hash;
    if (!h) { $("fade").style.opacity = 0; await ziomkiIntro2("WODA MINERALNA", 24, 3, 1); $("fade").style.opacity = 1; }
    const parts = [["#telefon", partTelefon], ["#podworko", partPodworko], ["#rzeka", partRzeka], ["#las", partLas], ["#oboz", partOboz], ["#droga", partDroga], ["#rano", partRano]];
    let on = !h || h === "#x";
    for (const [id, fn] of parts){ if (id === h) on = true; if (on) await fn(); }
    if (!h) await ziomkiOutro();
    if (!h || h === "#x" || h === "#napis") await credit();
    $("endScreen").hidden = false; $("againBtn").focus();
  }
