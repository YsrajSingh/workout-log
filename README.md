# 🏋️ workout-log

Personal workout log — exercises, sets, reps & weights tracked in Jupyter notebooks. Dashboard coming soon.

---

## 📁 Structure

```
workout-log/
├── README.md
├── logs/
│   └── YYYY/
│       └── MM/
│           └── DD/
│               ├── workout.ipynb   ← fill this in
│               ├── workout.json    ← auto-generated
│               └── workout.md      ← auto-generated
├── assets/
│   └── YYYY/
│       └── MM/
│           └── DD/
│               ├── chest.png       ← drop muscle images here
│               ├── biceps.png
│               └── ...
├── scripts/
│   ├── new_day.py                 ← creates today's folders (logs + assets)
│   └── template.ipynb             ← base template (don't edit)
└── dashboard/                     ← UI (coming soon)
```

---

## 🚀 How to Log a Workout

### 1. Create today's session
```bash
python scripts/new_day.py
```
This creates `logs/YYYY/MM/DD/` and copies the blank template notebook into it.

### 2. Open the notebook
```bash
jupyter notebook logs/YYYY/MM/DD/workout.ipynb
```

### 3. Fill in your exercises
Each exercise is a Python dict. Follow the structure in the template. Add as many exercises as needed.

### 4. Run the last cell
The last cell auto-generates:
- `workout.json` — structured data for the dashboard
- `workout.md` — readable markdown summary

### 5. Commit & push
```bash
git add .
git commit -m "log: 2026-03-18 — chest + triceps"
git push
```

---

## 📊 Tracked Fields

| Field | Description |
|---|---|
| `exercise` | Name of the exercise |
| `muscle_group` | Primary muscle targeted |
| `category` | `strength`, `cardio`, `flexibility` |
| `sets` | List of `{ set, reps, weight_kg }` |
| `cardio` | `{ duration_min, distance_km, calories }` (for cardio only) |
| `notes` | How it felt, form notes, anything |

---

## 🔍 Querying Later (Dashboard)

The JSON files are the source of truth for the dashboard. Example queries it will support:

- Bench press weight progression over last 3 months
- All bicep exercises in March
- Total km run last week
- Calories burned per day this month
- Max weight per exercise all time

---

## 💪 Muscle Images

Each day has its own assets folder at `assets/YYYY/MM/DD/` — created automatically by `new_day.py`.

Drop that day's muscle images into the matching folder. Name them by muscle group:

| Filename | Muscle |
|---|---|
| `chest.png` | Chest |
| `back.png` | Back |
| `shoulders.png` | Shoulders |
| `biceps.png` | Biceps |
| `triceps.png` | Triceps |
| `legs.png` | Legs |
| `core.png` | Core |
| `cardio.png` | Cardio |

Any `.png`, `.jpg`, `.jpeg`, or `.webp` format works. The notebook auto-detects and displays the image based on `muscle_group`.
