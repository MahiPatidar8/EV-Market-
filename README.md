# ⚡ EV Market Insights

> Turning two large electric-vehicle datasets into a project website, an interactive dashboard page and two Tableau Public views — so EV market questions can be answered in seconds instead of by reading raw tables.

**Repository:** https://github.com/MahiPatidar8/EV-Market-

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Datasets](#-datasets)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Key Findings](#-key-findings)
- [Testing](#-testing)
- [Limitations](#-limitations)
- [Future Scope](#-future-scope)
- [Links](#-links)

---

## 🔍 Overview

EV Market Insights presents one project in four connected pieces:

| Piece | What it is |
|---|---|
| **Project website** | A showcase page with Overview, Features, Analytics and Resources sections that links everything together |
| **Dashboard page** | A filterable, in-browser dashboard built on 100,000 embedded records |
| **Tableau executive dashboard** | Published on Tableau Public, opens in any browser |
| **Tableau market story** | A guided story with the main findings, published on Tableau Public |

The website also names a Python **Flask** application (`app.py`) as the web layer of the project.

**Problem it solves:** a 200,000-row EV dataset with 36 attributes is too large to read by hand, and a Tableau workbook can only be opened by people who have Tableau. This project makes the data filterable and shareable for analysts, students and planners.

---

## ✨ Features

- **9 filters** that update every chart at once: year range, region, category, battery type, drivetrain, use case, manufacturing country and manufacturer
- **6 KPI tiles:** vehicle models, average price, average range, average rating, total annual sales and three-year resale value
- **4 summary charts** (by region, battery type, vehicle category and model year), each switchable between **12 measures** such as price, range, rating, resale value and sales
- **Price vs. range chart** on a log price scale, coloured by drivetrain, from a random sample of up to 3,000 matching vehicles
- **Sortable summary table** grouped by 8 dimensions, with a *Copy table* button and a show-all-rows option
- **Status line** (e.g. `Showing 100,000 of 100,000 vehicles`) and a clear message when no vehicle matches the filters
- **Light / dark mode** and reduced-motion support
- Works in any modern browser, on desktop or phone
- Runs as **static files** — no data server needed

---

## 📊 Datasets

| File | Rows | Columns | Notes |
|---|---|---|---|
| `compressed_data.csv` | 100,000 | 37 | Embedded in the dashboard page |
| `compressed_data-2.csv.gz` | 200,000 | 37 | Used for the report analysis and Tableau views (gzip-compressed) |

Each file has a vehicle ID plus 36 attributes, including battery capacity, range, charging speed, price, safety rating and customer rating.

The larger dataset covers **200 manufacturers, 17,980 models, 15 vehicle categories, 7 market regions, 10 manufacturing countries** and model years **2018–2026**, adding up to **1.55 billion annual sales units**.

> [!IMPORTANT]
> **About the data:** these datasets appear to be synthetic (generated), not real registration records. For example, sales totals are almost identical across regions and years. The findings in this project therefore demonstrate the analysis workflow, from Tableau analysis to a published website, and should not be treated as real EV market facts.

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Analysis | Tableau (published on Tableau Public) |
| Data | CSV and gzip-compressed CSV |
| Dashboard page | HTML, CSS, JavaScript, Chart.js 4.4.1 |
| Data in the page | Columns packed as base64 binary and read as typed arrays |
| Website | HTML, CSS, JavaScript, DM Sans & Space Grotesk fonts |
| Web application | Python, Flask (`app.py`) |
| Verification | Python, pandas, headless Chrome |
| Version control | Git & GitHub |

---

## 📁 Project Structure

```
EV-Market-/
├── index-6.html                                  # Project website (Overview, Features, Analytics, Resources)
├── EV Market Insights-2.html                     # Interactive dashboard page (100,000 embedded records)
├── app.py                                        # Flask application (web layer)
├── compressed_data.csv                           # 100,000 EV records, 37 columns
├── compressed_data-2.csv.gz                      # 200,000 EV records, 37 columns (gzip)
├── EV_Market_Performance_Market_Story.twbx       # Tableau workbook
├── EV_Market_Performance_Final_Report-3.docx     # Project report
└── README.md
```

---

## 🚀 Getting Started

### Option 1 — Open the static files (no server needed)

1. Clone the repository:
   ```bash
   git clone https://github.com/MahiPatidar8/EV-Market-.git
   cd EV-Market-
   ```
2. Open `index-6.html` in your browser to see the project website.
3. Open `EV Market Insights-2.html` to use the interactive dashboard.

> **Note:** the dashboard loads Chart.js from a CDN (`cdn.jsdelivr.net`), so an **internet connection is required** for the charts and KPI tiles to appear.

### Option 2 — Run the Flask app

```bash
pip install flask
python app.py
```

Then open the local address Flask prints in the terminal (usually `http://127.0.0.1:5000`).

### Tableau views

Open the live **EV Executive Dashboard** and **Market Story** from the Analytics section of the website, or from the links below.

---

## 📈 Key Findings

Computed from the 200,000-record dataset:

- **Market size:** 1.55 billion annual sales units across 200 manufacturers and 17,980 models; average customer rating 4.09 / 5
- **Vehicle categories:** Two-wheeler scooters lead with 174.6 million units (11.3%); electric trucks, pickup trucks and buses each sell under 13 million
- **Battery types:** NMC (524.1 M) and LFP (496.1 M) together hold about 66% of units; sodium-ion 153.3 M, solid-state 110.0 M
- **Regions:** Totals range from 217.5 M (Europe) to 224.0 M (South Asia) — a gap of only about 3%
- **Range:** Luxury sedans average 550.6 km and luxury SUVs 524.8 km, versus 105.0 km for scooters
- **Durability:** Solid-state batteries last about 2,997 cycles and lose 7.4% capacity in five years; the other four types last 1,603–2,502 cycles and lose 10.1–14.0%
- **Manufacturers:** The largest, AmpereWorks, sells 9.5 M units (about 0.6% of the market) — no manufacturer dominates

---

## ✅ Testing

Twelve checks were run on the repository's own files (2 November 2026) using Python, pandas and headless Google Chrome:

- ✅ **9 passed** — dataset loading, value ranges, filters narrowing results, multi-select totals, empty selection, website sections, mobile layout (390 px), no script errors, dashboard filter options
- ⚠️ **2 passed with a data-quality note** — one duplicate vehicle ID in the 200,000-row file; 18,996 blank cells in 5 columns of that file (the dashboard skips blanks when averaging)
- ❌ **1 failed** — the dashboard charts stay empty when `cdn.jsdelivr.net` is unreachable (`Chart is not defined`)

**Performance (single run, will vary by machine):**

| Operation | Time |
|---|---|
| Four dashboard-style aggregations, 100,000 rows | 23.2 ms |
| Four dashboard-style aggregations, 200,000 rows | 44.3 ms |
| Region + battery filter with sales total, 200,000 rows | 31.6 ms |
| Project website ready (desktop / phone) | 0.57 s / 0.35 s |
| 7.5 MB dashboard page loaded, before charts | 0.63 s |

---

## ⚠️ Limitations

- The data looks generated, so findings are **not real market facts**
- Dashboard charts need internet access because Chart.js loads from a CDN
- The dashboard uses the 100,000-row file, not the 200,000-row dataset analysed in the report
- 18,996 blank cells in the larger file mean some averages use fewer records
- Past data only — no forecasting

---

## 🔭 Future Scope

- **Real data:** load actual EV registrations and sales from official sources
- **More attributes:** use more of the 36 attributes (torque, top speed, insurance cost, warranty) to compare performance and ownership cost
- **Forecasting:** add trend lines and models projecting sales by region and category
- **Wider reach:** bundle Chart.js so the dashboard works offline, add data export and saved views, and host the Flask app on a cloud platform

---

## 🔗 Links

- **GitHub:** https://github.com/MahiPatidar8/EV-Market-
- **Tableau Executive Dashboard:** _add your Tableau Public link here_
- **Tableau Market Story:** _add your Tableau Public link here_
- **Live demo:** _add the hosted link here once the site is published_

---

## 👤 Author

**Mahi Patidar** — [@MahiPatidar8](https://github.com/MahiPatidar8) # ⚡ EV Market Insights

> Turning two large electric-vehicle datasets into a project website, an interactive dashboard page and two Tableau Public views — so EV market questions can be answered in seconds instead of by reading raw tables.

**Repository:** https://github.com/MahiPatidar8/EV-Market-

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Datasets](#-datasets)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Key Findings](#-key-findings)
- [Testing](#-testing)
- [Limitations](#-limitations)
- [Future Scope](#-future-scope)
- [Links](#-links)

---

## 🔍 Overview

EV Market Insights presents one project in four connected pieces:

| Piece | What it is |
|---|---|
| **Project website** | A showcase page with Overview, Features, Analytics and Resources sections that links everything together |
| **Dashboard page** | A filterable, in-browser dashboard built on 100,000 embedded records |
| **Tableau executive dashboard** | Published on Tableau Public, opens in any browser |
| **Tableau market story** | A guided story with the main findings, published on Tableau Public |

The website also names a Python **Flask** application (`app.py`) as the web layer of the project.

**Problem it solves:** a 200,000-row EV dataset with 36 attributes is too large to read by hand, and a Tableau workbook can only be opened by people who have Tableau. This project makes the data filterable and shareable for analysts, students and planners.

---

## ✨ Features

- **9 filters** that update every chart at once: year range, region, category, battery type, drivetrain, use case, manufacturing country and manufacturer
- **6 KPI tiles:** vehicle models, average price, average range, average rating, total annual sales and three-year resale value
- **4 summary charts** (by region, battery type, vehicle category and model year), each switchable between **12 measures** such as price, range, rating, resale value and sales
- **Price vs. range chart** on a log price scale, coloured by drivetrain, from a random sample of up to 3,000 matching vehicles
- **Sortable summary table** grouped by 8 dimensions, with a *Copy table* button and a show-all-rows option
- **Status line** (e.g. `Showing 100,000 of 100,000 vehicles`) and a clear message when no vehicle matches the filters
- **Light / dark mode** and reduced-motion support
- Works in any modern browser, on desktop or phone
- Runs as **static files** — no data server needed

---

## 📊 Datasets

| File | Rows | Columns | Notes |
|---|---|---|---|
| `compressed_data.csv` | 100,000 | 37 | Embedded in the dashboard page |
| `compressed_data-2.csv.gz` | 200,000 | 37 | Used for the report analysis and Tableau views (gzip-compressed) |

Each file has a vehicle ID plus 36 attributes, including battery capacity, range, charging speed, price, safety rating and customer rating.

The larger dataset covers **200 manufacturers, 17,980 models, 15 vehicle categories, 7 market regions, 10 manufacturing countries** and model years **2018–2026**, adding up to **1.55 billion annual sales units**.

> [!IMPORTANT]
> **About the data:** these datasets appear to be synthetic (generated), not real registration records. For example, sales totals are almost identical across regions and years. The findings in this project therefore demonstrate the analysis workflow, from Tableau analysis to a published website, and should not be treated as real EV market facts.

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Analysis | Tableau (published on Tableau Public) |
| Data | CSV and gzip-compressed CSV |
| Dashboard page | HTML, CSS, JavaScript, Chart.js 4.4.1 |
| Data in the page | Columns packed as base64 binary and read as typed arrays |
| Website | HTML, CSS, JavaScript, DM Sans & Space Grotesk fonts |
| Web application | Python, Flask (`app.py`) |
| Verification | Python, pandas, headless Chrome |
| Version control | Git & GitHub |

---

## 📁 Project Structure

```
EV-Market-/
├── index-6.html                                  # Project website (Overview, Features, Analytics, Resources)
├── EV Market Insights-2.html                     # Interactive dashboard page (100,000 embedded records)
├── app.py                                        # Flask application (web layer)
├── compressed_data.csv                           # 100,000 EV records, 37 columns
├── compressed_data-2.csv.gz                      # 200,000 EV records, 37 columns (gzip)
├── EV_Market_Performance_Market_Story.twbx       # Tableau workbook
├── EV_Market_Performance_Final_Report-3.docx     # Project report
└── README.md
```

---

## 🚀 Getting Started

### Option 1 — Open the static files (no server needed)

1. Clone the repository:
   ```bash
   git clone https://github.com/MahiPatidar8/EV-Market-.git
   cd EV-Market-
   ```
2. Open `index-6.html` in your browser to see the project website.
3. Open `EV Market Insights-2.html` to use the interactive dashboard.

> **Note:** the dashboard loads Chart.js from a CDN (`cdn.jsdelivr.net`), so an **internet connection is required** for the charts and KPI tiles to appear.

### Option 2 — Run the Flask app

```bash
pip install flask
python app.py
```

Then open the local address Flask prints in the terminal (usually `http://127.0.0.1:5000`).

### Tableau views

Open the live **EV Executive Dashboard** and **Market Story** from the Analytics section of the website, or from the links below.

---

## 📈 Key Findings

Computed from the 200,000-record dataset:

- **Market size:** 1.55 billion annual sales units across 200 manufacturers and 17,980 models; average customer rating 4.09 / 5
- **Vehicle categories:** Two-wheeler scooters lead with 174.6 million units (11.3%); electric trucks, pickup trucks and buses each sell under 13 million
- **Battery types:** NMC (524.1 M) and LFP (496.1 M) together hold about 66% of units; sodium-ion 153.3 M, solid-state 110.0 M
- **Regions:** Totals range from 217.5 M (Europe) to 224.0 M (South Asia) — a gap of only about 3%
- **Range:** Luxury sedans average 550.6 km and luxury SUVs 524.8 km, versus 105.0 km for scooters
- **Durability:** Solid-state batteries last about 2,997 cycles and lose 7.4% capacity in five years; the other four types last 1,603–2,502 cycles and lose 10.1–14.0%
- **Manufacturers:** The largest, AmpereWorks, sells 9.5 M units (about 0.6% of the market) — no manufacturer dominates

---

## ✅ Testing

Twelve checks were run on the repository's own files (2 November 2026) using Python, pandas and headless Google Chrome:

- ✅ **9 passed** — dataset loading, value ranges, filters narrowing results, multi-select totals, empty selection, website sections, mobile layout (390 px), no script errors, dashboard filter options
- ⚠️ **2 passed with a data-quality note** — one duplicate vehicle ID in the 200,000-row file; 18,996 blank cells in 5 columns of that file (the dashboard skips blanks when averaging)
- ❌ **1 failed** — the dashboard charts stay empty when `cdn.jsdelivr.net` is unreachable (`Chart is not defined`)

**Performance (single run, will vary by machine):**

| Operation | Time |
|---|---|
| Four dashboard-style aggregations, 100,000 rows | 23.2 ms |
| Four dashboard-style aggregations, 200,000 rows | 44.3 ms |
| Region + battery filter with sales total, 200,000 rows | 31.6 ms |
| Project website ready (desktop / phone) | 0.57 s / 0.35 s |
| 7.5 MB dashboard page loaded, before charts | 0.63 s |

---

## ⚠️ Limitations

- The data looks generated, so findings are **not real market facts**
- Dashboard charts need internet access because Chart.js loads from a CDN
- The dashboard uses the 100,000-row file, not the 200,000-row dataset analysed in the report
- 18,996 blank cells in the larger file mean some averages use fewer records
- Past data only — no forecasting

---

## 🔭 Future Scope

- **Real data:** load actual EV registrations and sales from official sources
- **More attributes:** use more of the 36 attributes (torque, top speed, insurance cost, warranty) to compare performance and ownership cost
- **Forecasting:** add trend lines and models projecting sales by region and category
- **Wider reach:** bundle Chart.js so the dashboard works offline, add data export and saved views, and host the Flask app on a cloud platform

---

## 🔗 Links

- **GitHub:** https://github.com/MahiPatidar8/EV-Market-
- **Tableau Executive Dashboard:** _add your Tableau Public link here_
- **Tableau Market Story:** _add your Tableau Public link here_
- **Live demo:** _add the hosted link here once the site is published_

---

## 👤 Author

**Mahi Patidar** — [@MahiPatidar8](https://github.com/MahiPatidar8)

---

_EV Market Performance Insights — Project Report, November 2026._
