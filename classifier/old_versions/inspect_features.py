import pandas as pd, pickle

TRAIN_CSV = "training_data.csv"
MODEL_PKL = "rfc_pickup_model.pkl"      

df    = pd.read_csv(TRAIN_CSV)
pipe  = pickle.load(open(MODEL_PKL, "rb"))

est = pipe
if hasattr(pipe, "steps"):
    for _, step in reversed(pipe.steps):
        if hasattr(step, "feature_importances_"):
            est = step
            break
else:
    if not hasattr(est, "feature_importances_"):
        raise AttributeError("model has no feature_importances_")

feat_names = (est.feature_names_in_        
              if hasattr(est, "feature_names_in_")
              else df.drop(columns=["action"]).columns[:est.n_features_in_])

df["class"] = df["action"].map({0:"idle", 1:"good", 2:"bad"})
means = (df[feat_names]
         .join(df["class"])
         .groupby("class")
         .mean()
         .T.round(3))

importances = pd.Series(est.feature_importances_,
                        index=feat_names,
                        name="importance")

summary = (means.join(importances)
                 .sort_values("importance", ascending=False))

pd.set_option("display.max_rows", 40)
print(summary.head(40))
summary.to_csv("feature_summary_by_class.csv")
print("\nSaved full table to feature_summary_by_class.csv")
