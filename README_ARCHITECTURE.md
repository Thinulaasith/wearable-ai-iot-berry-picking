# Repository Architecture

## Project Structure

```text
├── src/                     React frontend
├── public/                  Images and static assets
├── backend/                 Flask API and live sensor processing
│   └── models/               Models used for live classification
├── classifier/              Dataset processing, model training and evaluation
│   ├── input_datasets/       Raw sensor recordings
│   ├── merged/               Merged datasets
│   └── studies/              Trained models and evaluation results
├── package.json             Frontend dependencies and scripts
├── README_SETUP.md          Installation and execution instructions
└── README_ARCHITECTURE.md   Repository structure and component reference
```

## Frontend — `src/`

- `main.tsx` — React entry point.
- `App.tsx` — Application routes and shared layout.
- `pages/Home.tsx` — Home page.
- `pages/ManageWearables.tsx` — Sensor connection, synchronization and battery information.
- `pages/DemoMenu.tsx` — Available demonstrations.
- `pages/DemoPage.tsx` — Sensor assignment, live predictions, charts and screen/camera recording.
- `pages/ViewRecording.tsx` — Recording/dashboard page.
- `components/` — Reusable interface components, including sensor cards, body-placement selectors and charts.
- `context/SensorContext.tsx` — Shared sensor state.
- `data/demos.ts` — Demo definitions and sensor placements.
- `styles/` — Page styles.
- `public/` — Images and static assets.

## Backend — `backend/`

- `app.py` — Flask API, sensor connection, synchronization, streaming and InfluxDB writes.
- `classify.py` — Live feature extraction, model inference and classification-result storage.
- `xdpchandler.py` — Movella DOT SDK sensor event and packet handling.
- `user_settings.py` — Movella SDK settings.
- `models/berry/xgb.pkl` — Trained XGBoost model used for the Berry Picking live demo.
- `requirements.txt` — Backend Python dependencies.
- `.env` — Local InfluxDB connection settings (created during setup).

**Main API endpoints**

- Sensor management: `/connect`, `/devices`, `/sync`, `/battery`
- Available models: `/models`
- Live session: `/start-multiple`, `/stop-all`
- Live sensor stream: `/events` (also `/stream`)
- Predictions: `/classification`, `/classification/summary`

## Machine Learning — `classifier/`

- `input_datasets/` — Raw Movella sensor CSV files organised by recording session, participant and activity.
- `merger.py` — Merges synchronized dominant-wrist and dominant-leg recordings.
- `merged/2_Sensor_5_activities/` — Merged dataset for the five-activity classifier.
- `config.py` — Sensor positions, activity labels, preprocessing and training parameters.
- `preprocessing.py` — Windowing and feature extraction.
- `main.py` — Training and evaluation entry point.
- `train.py` — Flat and hierarchical model training.
- `evaluation.py` — Performance metrics, classification reports and confusion matrices.
- `studies/study_N/` — Saved models, training configuration, processed training data and evaluation results for each study.
- `requirements.txt` — Training dependencies.

**Supported architectures**

- `flat` — One model predicts all five activities.
- `hierarchical` — Stage 1 identifies the main activity; Stage 2 separates Good Picking and Bad Picking.
- `hierarchical_with_other` — Adds an `Other` class at Stage 2 with fallback to a non-picking Stage 1 prediction.

**Supported algorithms**

- `rf` — Random Forest.
- `xgb` — XGBoost.

**Final activity labels:** Bending, Idle, Good Picking, Bad Picking and Pushing.

## Data Flow

**Training**

```text
classifier/input_datasets/
    → classifier/merger.py
    → classifier/merged/
    → classifier/preprocessing.py
    → classifier/main.py (training and evaluation)
    → classifier/studies/study_N/
```

**Live classification**

```text
Movella DOT sensors
    → backend/app.py
    → InfluxDB (sensor_data)
    → backend/classify.py + saved model
    → InfluxDB (classification)
    → Flask API
    → React frontend
```

- The frontend also receives live sensor data through server-sent events.
- Session recordings are generated and downloaded from the frontend.

For installation and execution, see [README_SETUP.md](README_SETUP.md).
