import pandas as pd
from datetime import datetime

def generate_plan(csv_file, daily_hours):
    df = pd.read_csv(csv_file)
    today = datetime.today()

    df["exam_date"] = pd.to_datetime(df["exam_date"])
    df["days_left"] = (df["exam_date"] - today).dt.days
    df = df[df["days_left"] > 0]

    df["weight"] = df["difficulty"] / df["days_left"]
    total_weight = df["weight"].sum()

    df["daily_hours"] = (df["weight"] / total_weight) * daily_hours
    df["daily_hours"] = df["daily_hours"].round(2)

    return df[["subject", "daily_hours", "days_left"]]
