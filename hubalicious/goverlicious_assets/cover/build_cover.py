import json, html as htmlmod, os

HERE = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(HERE, "countries_data.json")))

order = ["uk","usa","germany","france","japan","italy","canada","russia","eu"]

def svg_for(key):
    c = data[key]
    vb = c["viewbox"]
    if c["mode"] == "single-d":
        path_el = f'<path d="{c["d"]}" class="cland"/>'
    else:
        parts = "".join(f'<path d="{p}" class="cland"/>' for p in c["paths"])
        path_el = parts
    return f'<svg viewBox="{vb}" preserveAspectRatio="xMidYMid meet" class="cmap">{path_el}</svg>'

cards = ""
for key in order:
    c = data[key]
    cards += f'''<div class="ccard">
  <div class="cmap-wrap">{svg_for(key)}</div>
  <div class="clabel">{c["flag"]} {htmlmod.escape(c["label"])}</div>
</div>
'''

# page: 1260.95996 x 810 pt -> inches
PAGE_W_IN = 1260.95996/72
PAGE_H_IN = 810/72
TRIM_BLEED_IN = 8.625
SPINE_IN = PAGE_W_IN - 2*TRIM_BLEED_IN

html_out = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Goverlicious Vol. 1 — Cover</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet">
<style>
@page {{ size: {PAGE_W_IN:.6f}in {PAGE_H_IN:.6f}in; margin: 0; }}
:root {{
  --bg: #0a0a0a; --bg2: #111111; --text: #e8e0d0; --muted: #6a6460;
  --accent: #c8a84a; --accent-light: #e8c46a; --accent-faint: rgba(200,168,74,0.08);
  --border: rgba(200,168,74,0.18);
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
html, body {{ width: {PAGE_W_IN:.6f}in; height: {PAGE_H_IN:.6f}in; background: var(--bg); }}
body {{
  background: var(--bg);
  background-image: repeating-linear-gradient(135deg, rgba(255,255,255,0.012) 0 2px, transparent 2px 14px);
  color: var(--text);
  font-family: 'JetBrains Mono', monospace;
  display: flex;
  overflow: hidden;
}}
.back, .front {{ width: {TRIM_BLEED_IN:.6f}in; height: 100%; padding: 0.55in 0.6in; display: flex; flex-direction: column; }}
.spine {{ width: {SPINE_IN:.6f}in; height: 100%; display: flex; align-items: center; justify-content: center; border-left: 1px solid var(--border); border-right: 1px solid var(--border); background: var(--bg2); }}
.spine-text {{ writing-mode: vertical-rl; transform: rotate(180deg); font-family: 'Playfair Display', serif; font-weight: 900; font-size: 0.17in; letter-spacing: 0.05em; color: var(--accent-light); white-space: nowrap; }}
.spine-text em {{ color: var(--text); font-style: italic; }}
.spine-sub {{ writing-mode: vertical-rl; transform: rotate(180deg); font-size: 0.08in; letter-spacing: 0.18em; color: var(--muted); text-transform: uppercase; margin-top: 0.15in; }}

.back-headline {{ font-family: 'Playfair Display', serif; font-style: italic; font-weight: 700; font-size: 0.26in; line-height: 1.25; color: var(--text); margin-bottom: 0.3in; max-width: 5in; }}
.back-copy {{ font-size: 0.1in; line-height: 1.75; color: var(--text); opacity: 0.85; max-width: 5in; }}
.back-copy p {{ margin-bottom: 0.18in; }}
.back-copy b {{ color: var(--accent-light); font-weight: 600; }}
.back-countries {{ margin-top: 0.3in; font-size: 0.075in; letter-spacing: 0.1em; color: var(--muted); text-transform: uppercase; line-height: 1.8; max-width: 5in; }}
.back-footer {{ margin-top: auto; font-size: 0.07in; letter-spacing: 0.06em; color: var(--muted); border-top: 1px solid var(--border); padding-top: 0.15in; }}

.front-tag {{ font-size: 0.08in; letter-spacing: 0.22em; color: var(--muted); text-transform: uppercase; margin-bottom: 0.2in; }}
.front-title {{ font-family: 'Playfair Display', serif; font-weight: 900; font-size: 0.85in; line-height: 0.95; color: var(--text); }}
.front-title em {{ font-style: italic; color: var(--accent-light); font-weight: 700; }}
.front-sub {{ font-family: 'Playfair Display', serif; font-weight: 700; font-size: 0.19in; margin-top: 0.12in; color: var(--text); }}
.front-tagline {{ font-size: 0.1in; color: var(--muted); margin-top: 0.08in; max-width: 4.6in; line-height: 1.5; }}

.grid {{ margin-top: 0.3in; display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.14in; }}
.ccard {{
  background: rgba(255,255,255,0.035);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1px solid var(--border);
  border-radius: 0.06in;
  padding: 0.12in 0.1in 0.1in;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  box-shadow: 0 0.02in 0.08in rgba(0,0,0,0.3), inset 0 0 0.3in rgba(200,168,74,0.03);
}}
.cmap-wrap {{ width: 100%; height: 0.72in; display: flex; align-items: center; justify-content: center; }}
.cmap {{ width: 100%; height: 100%; }}
.cland {{ fill: var(--accent-faint); stroke: var(--accent-light); stroke-width: 1.1; stroke-opacity: 0.85; }}
.clabel {{ margin-top: 0.08in; font-size: 0.065in; letter-spacing: 0.05em; text-transform: uppercase; color: var(--muted); text-align: center; }}

.front-footer {{ margin-top: auto; display: flex; justify-content: space-between; align-items: baseline; border-top: 1px solid var(--border); padding-top: 0.15in; font-size: 0.075in; letter-spacing: 0.08em; color: var(--muted); text-transform: uppercase; }}
.front-footer .vol {{ font-family: 'Playfair Display', serif; font-weight: 900; font-size: 0.15in; color: var(--accent-light); text-transform: none; letter-spacing: 0; }}
</style>
</head>
<body>

<div class="back">
  <div class="back-headline">Every country publishes an org chart.<br>Almost none of them are true.</div>
  <div class="back-copy">
    <p>Who really runs Britain, America, Germany, France, Japan, Italy, Canada, Russia and the European Union? Not just presidents and parliaments — but coalition committees that appear in no constitution, elite schools that staff whole governments, media barons, security clans, family fortunes, lobbyists and foreign powers.</p>
    <p><b>Goverlicious</b> draws two maps of every country: the <b>formal map</b> of who officially holds power, and the <b>shadow map</b> of who actually shapes decisions — then opens a dossier on every node, with key facts and a power score.</p>
    <p>Nine infographic chapters. Over 200 power centres. One question: <i>does the org chart tell the truth?</i></p>
  </div>
  <div class="back-countries">United Kingdom &middot; United States &middot; Germany &middot; France &middot; Japan &middot; Italy &middot;<br>Canada &middot; Russia &middot; European Union</div>
  <div class="back-footer">DATA AS OF OCTOBER 2026 &middot; COMPANION TO THE FREE ONLINE ATLAS AT<br>QUARTERWHARFS.COM</div>
</div>

<div class="spine">
  <div style="display:flex; flex-direction:column; align-items:center;">
    <div class="spine-text">Gover<em>licious</em></div>
    <div class="spine-sub">Vol. 1</div>
  </div>
</div>

<div class="front">
  <div class="front-tag">Quarter Wharfs &middot; Volume 1</div>
  <div class="front-title">Gover<em>licious</em></div>
  <div class="front-sub">Who actually runs the world?</div>
  <div class="front-tagline">The G7, Russia &amp; the EU — formal power and shadow power, mapped.</div>
  <div class="grid">
{cards}  </div>
  <div class="front-footer"><span>An Infographic Atlas</span><span class="vol">Vol. 1</span></div>
</div>

</body>
</html>
'''

out_path = os.path.join(HERE, "cover.html")
open(out_path, "w", encoding="utf-8").write(html_out)
print("Wrote", out_path, len(html_out), "bytes")
print(f"Page: {PAGE_W_IN:.4f}in x {PAGE_H_IN:.4f}in, spine {SPINE_IN:.4f}in")
