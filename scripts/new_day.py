"""
new_day.py
Run this every day before logging your workout.
Creates: logs/YYYY/MM/DD/workout.ipynb
"""

import os
import sys
import json
import shutil
from datetime import datetime, timedelta

# ── optional: pass a date like  python scripts/new_day.py 2026-03-20
if len(sys.argv) > 1:
    try:
        target = datetime.strptime(sys.argv[1], "%Y-%m-%d")
    except ValueError:
        print("❌  Invalid date format. Use YYYY-MM-DD  e.g. 2026-03-20")
        sys.exit(1)
else:
    target = datetime.today()

YEAR  = target.strftime("%Y")
MONTH = target.strftime("%m")
DAY   = target.strftime("%d")
DATE  = target.strftime("%Y-%m-%d")

folder        = os.path.join("logs",   YEAR, MONTH, DAY)
assets_folder = os.path.join("assets", YEAR, MONTH, DAY)
notebook      = os.path.join(folder, "workout.ipynb")
template      = os.path.join("scripts", "template.ipynb")

# ── already exists?
if os.path.exists(notebook):
    print(f"✅  Already exists: {notebook}")
    sys.exit(0)

# ── create folders
os.makedirs(folder, exist_ok=True)
os.makedirs(assets_folder, exist_ok=True)

# ── load template and inject the date
with open(template, "r") as f:
    nb = json.load(f)

# Replace placeholder date in every cell source
for cell in nb["cells"]:
    cell["source"] = [
        line.replace("__DATE__", DATE)
        for line in cell["source"]
    ]

# ── write notebook
with open(notebook, "w") as f:
    json.dump(nb, f, indent=2)

print(f"✅  Created: {notebook}")
print(f"✅  Assets folder: {assets_folder}")
print(f"   Drop today's muscle images into: {assets_folder}")
print(f"   Open with: jupyter notebook {notebook}")
