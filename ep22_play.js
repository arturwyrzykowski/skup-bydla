  // ===== SCENARIUSZ: WODA PITNA =====
  const stops = [];
  const keep = f => (stops.push(f), f);
  function stopAll(){ while (stops.length) { try { stops.pop()(); } catch (e) {} } }
  const BRAZ = "#6b4a1e";

  // kola traktora i beczki w danym ujeciu
  function wheels(sel, on, ms = 900){
    document.querySelectorAll(sel).forEach(w => { w.getAnimations().forEach(a => a.cancel());
      if (on) w.animate([{ transform: "rotate(0deg)" }, { transform: "rotate(-360deg)" }], { duration: ms, iterations: Infinity }); });
  }
  // plynna zmiana atrybutu (np. szerokosc maski malowania)
  function tween(ms, fn){
    return new Promise(res => { const t0 = performance.now();
      const step = now => { const k = Math.min(1, (now - t0) / ms); fn(k); if (k < 1) requestAnimationFrame(step); else res(); };
      requestAnimationFrame(step); });
  }
  // dzwiek: dzwonek telefonu, pompa, pedzel, rzyganie, smiech
  const ring = () => [0, .35].forEach(w => { tone(1320, .25, "square", .04, null, w); tone(1760, .25, "square", .03, null, w + .05); });
  const brush = () => noise(0.18, { freq: 2600, q: 1, vol: 0.12, sweepTo: 1400 });
  const pompa = () => loop(() => { if (Math.random() < .7) noise(0.12, { freq: 180 + Math.random() * 60, q: 2, vol: 0.18 }); });
  const bulg = () => loop(() => { if (Math.random() < .35) tone(90 + Math.random() * 70, 0.18, "sine", 0.25, 50); });
  function rzyg(){ noise(1.1, { freq: 300, q: 3, vol: 0.5, sweepTo: 120 }); tone(140, 0.9, "sawtooth", 0.08, 70); }
  // wajcha: z 1 na R (zblizenie)
  async function wajcha(){
    shot("shWajcha", { x: 800, y: 560, k: 1 });
    $("wajcha").style.transform = "rotate(-27deg)";
    await crash({ x: 800, y: 500, k: 1.25 });
    await sleep(500);
    await anim($("wajcha"), [{ transform: "rotate(-27deg)" }, { transform: "rotate(-27deg) translateY(30px)", offset: .3 }, { transform: "rotate(27deg) translateY(30px)", offset: .75 }, { transform: "rotate(27deg)" }],
               { duration: 900, easing: "ease-in-out" });
    sfx.bum(); shake(10, 300);
    await sleep(700);
  }

  // ---------- 1. dom, lozko, lazienka ----------
  async function partDom(){
    shot("shDom", { x: 800, y: 450, k: 1 });
    await fadeIn(700);
    await caption("Lato. Dom Andrzeja.", 1800);
    await camTo({ x: 780, y: 280, k: 2.2 }, 2200);
    shot("shSypialnia", { x: 700, y: 470, k: 1.25 });
    $("smrod").getAnimations().forEach(a => a.cancel());
    $("smrod").animate([{ opacity: 0, transform: "translate(0px,0px)" }, { opacity: .9, transform: "translate(-500px,0px)" }], { duration: 3500, fill: "forwards", easing: "ease-out" });
    await sleep(1800);
    await crash({ x: 560, y: 470, k: 2.4 });
    await line("a", "Co tu tak, kurwa, śmierdzi?", 500, "aLozeW");
    await fadeOut(350);
    // lazienka
    shot("shLazienka", { x: 840, y: 600, k: 1.7 });
    $("aLazP").classList.add("strach");
    const b = keep(bulg());
    keep(every(260, () => { const c = document.createElementNS(NS, "circle"); c.setAttribute("cx", 740 + Math.random() * 180); c.setAttribute("cy", 556);
      c.setAttribute("r", 6 + Math.random() * 10); c.setAttribute("fill", "#8a6a2e"); c.setAttribute("stroke", "#141414"); c.setAttribute("stroke-width", 3);
      $("bable").append(c); c.animate([{ transform: "translateY(0)", opacity: 1 }, { transform: "translateY(-30px)", opacity: 0 }], { duration: 700, fill: "forwards" }).finished.then(() => c.remove()).catch(() => {}); }));
    $("kaluza").style.transformBox = "fill-box"; $("kaluza").style.transformOrigin = "center";
    $("kaluza").animate([{ transform: "scale(.4,.6)" }, { transform: "scale(2.6,1.3)" }], { duration: 6000, fill: "forwards" });
    await fadeIn(300);
    sfx.chlup();
    await sleep(1600);
    await camTo({ x: 1100, y: 520, k: 1.15 }, 900);
    await crash({ x: 1340, y: 470, k: 2.2 });
    await line("a", "O ja pierdolę… Gówno się z kibla przelewa!", 500, "aLazP");
    await camTo({ x: 830, y: 620, k: 1.6 }, 900);
    await sleep(900);
    await fadeOut(400); stopAll(); $("aLazP").classList.remove("strach");
  }

  // ---------- 2. telefon do Triweta ----------
  async function partTelefon(){
    shot("shTelefon", { x: 800, y: 450, k: 1 });
    ring(); await fadeIn(300);
    await line("a", "Triwet, szambo mi się przelewa. Przyjedź, wybierz to.", 300, "aTelP");
    await camTo({ x: 820, y: 450, k: 1 }, 200);
    await line("r", "Stary, przypał. Ludzie dzwonią na policję, że gówno na pole wylewam.", 300, "rTelP");
    await line("a", "Dobra, już do ciebie jadę. Mam pomysł.", 600, "aTelP");
    await fadeOut(500);
  }

  // ---------- 3. podworko Stivena: malowanie beczki ----------
  async function partPodworko(){
    shot("shPodworko", { x: 700, y: 470, k: 1 });
    $("aPodP").querySelector(".farba").style.display = "none";
    $("rPodP").querySelector(".pedzel").style.display = "none";
    $("bPodClipR").setAttribute("width", 0); $("bPodNapis").style.display = "none";
    await fadeIn(600);
    await caption("Podwórko u Stivena.", 1800);
    await camTo({ x: 420, y: 560, k: 1.9 }, 1200);
    // farba z kieszeni
    const f = $("aPodP").querySelector(".farba"); f.style.display = ""; sfx.whoosh();
    f.style.transformBox = "fill-box"; f.style.transformOrigin = "50% 100%";
    await anim(f, [{ transform: "scale(.1) translateY(60px)" }, { transform: "scale(1.2)", offset: .7 }, { transform: "scale(1)" }], { duration: 600 });
    await line("a", "Dawaj, malujemy beczkę na niebiesko.", 250, "aPodP");
    await line("r", "Po co?", 200, "rPodP");
    await line("a", "Zobaczysz.", 400, "aPodP");
    $("rPodP").querySelector(".pedzel").style.display = "";
    await camTo({ x: 640, y: 470, k: 1.05 }, 900);
    const arms = [...document.querySelectorAll("#aPodP .armR, #rPodP .armR")].map(a =>
      a.animate([{ transform: "rotate(-25deg)" }, { transform: "rotate(20deg)" }], { duration: 260, direction: "alternate", iterations: Infinity }));
    const br = keep(every(260, brush));
    await tween(4200, k => $("bPodClipR").setAttribute("width", 580 * k));
    arms.forEach(a => a.cancel()); br(); stops.pop();
    // napis
    await camTo({ x: 330, y: 500, k: 1.6 }, 700);
    const t = $("bPodNapis"), full = "WODA PITNA"; t.style.display = "";
    for (let i = 1; i <= full.length; i++){ t.textContent = full.slice(0, i); if (full[i - 1] !== " ") brush(); await sleep(170); }
    await sleep(1100);
    await fadeOut(500);
  }

  // ---------- 4. jazda + szambo + gejzer ----------
  async function partSzambo(){
    shot("shJazda", { x: 800, y: 480, k: 1 });
    const eng = silnik(1); keep(() => eng.stop());
    wheels("#shJazda .kR, #shJazda .kF, #shJazda .kB", true, 700);
    $("jazdaTlo").animate([{ transform: "translateX(0px)" }, { transform: "translateX(1400px)" }], { duration: 6000, fill: "forwards" });
    $("pasy").animate([{ transform: "translateX(0px)" }, { transform: "translateX(1800px)" }], { duration: 6000, fill: "forwards" });
    await fadeIn(500);
    await sleep(4800);
    await fadeOut(400);
    wheels("#shJazda .kR, #shJazda .kF, #shJazda .kB", false);
    // pod domem: waz w deklu
    shot("shSzambo", { x: 900, y: 560, k: 1.05 });
    $("aSzP").querySelector(".brud").style.display = "none";
    $("gejzer").innerHTML = ""; $("gejzer").style.display = "none";
    await fadeIn(400);
    eng.set(1.5); const p = keep(pompa());
    await camTo({ x: 1220, y: 560, k: 2.0 }, 1300);
    await sleep(600);
    await line("a", "Kurwa, ale gęste. Włącz rewers!", 300, "aSzP");
    await wajcha();
    // gejzer
    shot("shSzambo", { x: 1250, y: 520, k: 1.5 });
    $("gejzer").style.display = "";
    const kol = document.createElementNS(NS, "path");
    kol.setAttribute("d", "M1282 740 Q1268 520 1278 300 Q1270 210 1292 150 Q1300 130 1308 150 Q1330 210 1322 300 Q1332 520 1318 740 Z"); kol.setAttribute("fill", BRAZ);
    kol.setAttribute("stroke", "#3a2408"); kol.setAttribute("stroke-width", 3);
    kol.style.transformBox = "fill-box"; kol.style.transformOrigin = "50% 100%";
    $("gejzer").append(kol);
    kol.animate([{ transform: "scaleY(0)" }, { transform: "scaleY(1.08)", offset: .3 }, { transform: "scaleY(.92)" }], { duration: 1200, fill: "forwards" });
    const fal = kol.animate([{ transform: "scaleY(.92) scaleX(1)" }, { transform: "scaleY(1.02) scaleX(.9)" }], { duration: 180, delay: 1200, direction: "alternate", iterations: Infinity });
    sfx.chlup(); noise(2.5, { freq: 400, q: .7, vol: .45, sweepTo: 150 }); shake(18, 800);
    // krople lecace po luku (w gore i w dol), bez rozmywania
    function kropla(){
      const e = document.createElementNS(NS, "ellipse"), r = 6 + Math.random() * 12;
      e.setAttribute("cx", 0); e.setAttribute("cy", 0); e.setAttribute("rx", r); e.setAttribute("ry", r * .75);
      e.setAttribute("fill", Math.random() < .5 ? BRAZ : "#5a3a12"); e.setAttribute("stroke", "#2a1a08"); e.setAttribute("stroke-width", 2);
      $("fx2").append(e);
      const x0 = 1300 + (Math.random() - .5) * 30, y0 = 150 + Math.random() * 40, vx = (Math.random() < .65 ? -1 : 1) * (80 + Math.random() * 260), vy = -(60 + Math.random() * 160);
      const fr = []; for (let t = 0; t <= 1.0001; t += .125){ const tt = t * 1.4; fr.push({ transform: `translate(${x0 + vx * tt}px,${y0 + vy * tt + 420 * tt * tt}px) rotate(${t * 200}deg)` }); }
      e.animate(fr, { duration: 1100, easing: "linear", fill: "forwards" }).finished.then(() => e.remove()).catch(() => {});
    }
    const sp = keep(every(25, () => { kropla(); kropla(); }));
    await sleep(500);
    $("aSzP").querySelector(".brud").style.display = "";
    $("aSzP").classList.add("strach");
    await sleep(700);
    await line("a", "Kurwa, stop! Stop! Wyłącz to, do chuja!", 150, "aSzP");
    sp(); fal.cancel(); eng.set(1); stopAll();
    kol.animate([{ transform: "scaleY(.9)" }, { transform: "scaleY(0)" }], { duration: 500, fill: "forwards" });
    // rzyganie
    await crash({ x: 1170, y: 560, k: 2.6 });
    rzyg();
    const pk = every(60, () => puff(1205, 552, { col: "#9ac83a", r: 8 + Math.random() * 8, up: -(140 + Math.random() * 80), dx: 60 + Math.random() * 60, ms: 800, op: .95, stroke: true }));
    await sleep(1300); pk();
    // Triwet sie smieje
    await crash({ x: 520, y: 560, k: 2.6 });
    const sm = $("rSzP").querySelector(".bob").animate([{ transform: "translateY(0)" }, { transform: "translateY(-10px)" }], { duration: 140, direction: "alternate", iterations: Infinity });
    await line("r", "Ha ha ha ha ha!", 300, "rSzP");
    sm.cancel();
    // papier toaletowy na ubraniu
    await crash({ x: 1165, y: 590, k: 3.4 });
    await sleep(900);
    await camTo({ x: 1180, y: 560, k: 2.2 }, 500);
    $("aSzP").classList.remove("strach");
    await line("a", "Ja to pierdolę. Idę się umyć, a ty wyciągaj.", 500, "aSzP");
    await fadeOut(700); eng.stop(0.5);
  }

  // ---------- 5. pusto w szambie ----------
  async function partPusto(){
    shot("shPusto", { x: 800, y: 450, k: 1.1 });
    $("aPusto").style.display = "none"; $("rPusto").style.display = "none";
    await caption("Godzinę później.", 1400);
    await fadeIn(500);
    $("aPusto").style.display = ""; sfx.whoosh(); await sleep(400);
    $("rPusto").style.display = ""; sfx.whoosh(); await sleep(600);
    await line("a", "Pusteczko, aż miło.", 500, "aPusto");
    await line("r", "Teraz tego nie wyleję na łąkę, bo i tak będzie śmierdziało i ktoś zadzwoni na policję.", 300, "rPusto");
    await line("a", "Przecież my wodę wozimy. Jedziemy nabrać wody do ogrodu.", 600, "aPusto");
    await fadeOut(500);
  }

  // ---------- 6. kosciol i Narew ----------
  async function partNarew(){
    shot("shKosciol", { x: 800, y: 470, k: 1 });
    const eng = silnik(1); keep(() => eng.stop());
    wheels("#shKosciol .kR, #shKosciol .kF, #shKosciol .kB", true, 700);
    $("trKosW").animate([{ transform: "translate(-900px,820px) scale(.62)" }, { transform: "translate(2500px,820px) scale(.62)" }], { duration: 7000, fill: "forwards" });
    await fadeIn(500);
    await sleep(6400);
    await fadeOut(400);
    wheels("#shKosciol .kR, #shKosciol .kF, #shKosciol .kB", false);
    // nad rzeka
    shot("shNarew", { x: 800, y: 470, k: 1 });
    const bw = $("brazWoda").firstElementChild; bw.setAttribute("rx", 10); bw.setAttribute("ry", 4);
    $("karas").style.display = "none";
    await fadeIn(500);
    await caption("Nad rzeką.", 1600);
    eng.set(1.4); const p = keep(pompa());
    await camTo({ x: 1050, y: 560, k: 2.2 }, 1400);
    await line("a", "Triwet, nabieraj wody!", 250, "aNarP");
    await crash({ x: 1060, y: 520, k: 3.4 });
    await line("a", "…ale na rewersie, hehe.", 400, "aNarP");
    await wajcha();
    shot("shNarew", { x: 700, y: 600, k: 1.3 });
    const bw2 = $("brazWoda").firstElementChild;
    await tween(3200, k => { bw2.setAttribute("rx", 10 + 700 * k); bw2.setAttribute("ry", 4 + 150 * k); });
    await camTo({ x: 800, y: 500, k: 1 }, 800);
    await line("r", "Kurwa, żeby z tego jakiejś katastrofy ekologicznej nie było.", 300, "rNarP");
    await camTo({ x: 1050, y: 560, k: 2.2 }, 700);
    await line("a", "Przestań. Wszyscy wiedzą, że karasie jedzą gówno.", 300, "aNarP");
    // karas wyskakuje zadowolony
    await camTo({ x: 700, y: 620, k: 1.8 }, 600);
    $("karas").style.display = ""; sfx.plusk();
    await anim($("karas"), [{ transform: "translate(0px,60px) rotate(20deg)" }, { transform: "translate(60px,-140px) rotate(-10deg)", offset: .5 }, { transform: "translate(140px,60px) rotate(-40deg)" }], { duration: 1200 });
    $("karas").style.display = "none"; sfx.plusk();
    await camTo({ x: 1050, y: 560, k: 2.2 }, 700);
    await line("a", "Nabierz na koniec trochę wody, to się beczka wypłucze, i spadamy.", 700, "aNarP");
    await fadeOut(800); stopAll();
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
    if (!h) { $("fade").style.opacity = 0; await ziomkiIntro2("WODA PITNA", 22, 3, 1); $("fade").style.opacity = 1; }
    const parts = [["#dom", partDom], ["#telefon", partTelefon], ["#podworko", partPodworko], ["#szambo", partSzambo], ["#pusto", partPusto], ["#narew", partNarew]];
    let on = !h || h === "#x";
    for (const [id, fn] of parts){ if (id === h) on = true; if (on) await fn(); }
    if (!h) await ziomkiOutro();
    if (!h || h === "#x" || h === "#napis") await credit();
    $("endScreen").hidden = false; $("againBtn").focus();
  }
