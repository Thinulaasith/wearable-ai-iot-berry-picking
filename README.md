# Backend Setup (Windows)

## InfluxDB Configuration

- Download [InfluxDB OSS 2.x for Windows](https://docs.influxdata.com/influxdb/v2/install/).
- Run `influxd.exe`.
- Open [http://localhost:8086](http://localhost:8086).
- Click **Get Started** and configure:
    - **Username:** Your choice
    - **Password:** Your choice
    - **Organization:** `Swinburne`
    - **Bucket:** `berry`
- Copy the generated API token.
- Update the backend `.env` file:

```dotenv
INFLUX_URL=http://localhost:8086
INFLUX_TOKEN=YOUR_GENERATED_TOKEN
INFLUX_ORG=Swinburne
INFLUX_BUCKET=berry
INFLUX_QUERY_MEASUREMENT=sensor_data
INFLUX_RESULT_MEASUREMENT=classification
MODEL_DIR=./models
```

---

## Backend Configuration

- Install [Python 3.10 (64-bit)](https://www.python.org/downloads/release/python-31011/).
- Install **Movella DOT PC SDK 2023.6**.
- Create and activate a virtual environment:

```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

- Install dependencies:

```powershell
pip install -r requirements.txt
```

- Run the backend:

```powershell
python app.py --serve
```

- Backend API: [http://localhost:5000](http://localhost:5000).
