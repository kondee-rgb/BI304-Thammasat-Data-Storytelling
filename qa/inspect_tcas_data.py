import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/data.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

tcas = d.get('faculties_tcas', {})
print("Type of faculties_tcas:", type(tcas))
if isinstance(tcas, list):
    print(f"Total items: {len(tcas)}")
    for item in tcas:
        print(item)
elif isinstance(tcas, dict):
    print("Keys:", list(tcas.keys()))
    for k, v in tcas.items():
        print(f"{k}: {v}")
