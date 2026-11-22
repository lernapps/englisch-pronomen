# Dry run of the dip rule over the sentences of audio-texte.json: nothing is written.
# python dry_run.py <texte.json>   (in the app's folder, with the Python of the audio environment)
import importlib.util, sys, json, pathlib, numpy as np, soundfile
spec = importlib.util.spec_from_file_location("la", ".agents/skills/lernapps-audio/scripts/lernapps_audio.py")
la = importlib.util.module_from_spec(spec); sys.modules["la"] = la; spec.loader.exec_module(la)
W = 240
def env(a): return np.array([np.sqrt(np.mean(a[i:i + W] ** 2)) for i in range(0, len(a) - W + 1, W)])
texts = json.load(open(sys.argv[1])); cache = {}; rows = []
for out, text in texts.items():
    w = pathlib.Path("/tmp/dry.wav"); la.synthesize("bf_emma", "en-gb", text, 1.0, w, cache)
    a, sr = soundfile.read(str(w)); a = a.astype(np.float32); n = env(a); n = n / n.max()
    last = int(np.where(n >= 0.08)[0][-1]); best = None
    for v in range(max(1, last - 40), last - 2):
        if n[v] <= 0.15 and n[v] <= n[v - 1] and n[v] <= n[v + 1] and n[v + 1:last + 1].max() >= 1.4 * n[v]: best = v
    r = {"file": out.split("/")[-1], "text": text, "last_sound_ms": (last + 1) * 10}
    if best is not None:
        cut = best * W + W // 2
        r.update(dip_ms=best * 10, stray_ms=(last - best) * 10, bump=round(float(n[best + 1:last + 1].max()), 2), energy_pct=round(100 * float(np.sum(a[cut:] ** 2) / np.sum(a ** 2)), 2))
        r["cut"] = r["stray_ms"] <= 130 and r["bump"] <= 0.30 and r["energy_pct"] <= 2
    else: r["cut"] = False
    rows.append(r)
json.dump(rows, open("dry_run.json", "w"), indent=1, ensure_ascii=False)
print(sum(r["cut"] for r in rows), "of", len(rows), "files would change")
