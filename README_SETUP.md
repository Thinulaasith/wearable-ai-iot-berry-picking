# Setup and Running Guide

## Requirements

- Node.js and npm — frontend
- Python 3.10 — Flask backend
- Python 3.11 — machine-learning classifier training
- InfluxDB
- Movella DOT PC SDK

## Install InfluxDB

- Install [InfluxDB](https://docs.influxdata.com/influxdb/v2/install/).
- Start the database server:

```powershell
influxd
```

- Open `http://localhost:8086` and create:
  - Organization: `Swinburne`
  - Bucket: `berry`
  - API token with read/write access to the bucket
- Create `backend/.env`:

```dotenv
INFLUX_URL=http://localhost:8086
INFLUX_TOKEN=YOUR_API_TOKEN
INFLUX_ORG=Swinburne
INFLUX_BUCKET=berry
INFLUX_QUERY_MEASUREMENT=sensor_data
INFLUX_RESULT_MEASUREMENT=classification
```

## Install and Run the Flask Backend

- **Python 3.10 required.**
- Install the [Movella DOT PC SDK](https://movella.my.site.com/XsensKnowledgebase/s/article/Movella-DOT-PC-SDK-Guide?language=en_US) and its Python 3.10 bindings/wheel.
- From the repository root, create the virtual environment, install `backend/requirements.txt`, and start Flask:

```powershell
cd backend
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py --serve
```

- Flask API: `http://localhost:5000`

## Install and Run the Frontend

- From the repository root, in a separate terminal:

```powershell
npm install
npm run dev
```

- Frontend: `http://localhost:5173`

## Retrain Models

- **Python 3.11 required.**
- From the repository root:

```powershell
cd classifier
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python merger.py
python main.py 2_Sensor_5_activities --architecture all --model both
```

- `merger.py`: merges raw sensor recordings into the training dataset.
- `main.py`: preprocesses the merged dataset, trains models, evaluates them, and saves the study results in `classifier/studies/`.
- Architecture options (`--architecture`):
  - `flat` — one classifier for all five activities.
  - `hierarchical` — first predicts the main activity; a second classifier distinguishes Good Picking from Bad Picking.
  - `hierarchical_with_other` — hierarchical approach with an `Other` class at the second stage.
  - `all` — trains all three architectures.
- Model options (`--model`):
  - `rf` — Random Forest.
  - `xgb` — XGBoost.
  - `both` — both algorithms.
