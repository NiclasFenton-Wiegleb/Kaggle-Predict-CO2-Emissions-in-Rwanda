#Dependencies

import pandas as pd
import joblib

def load_data():
    #Loads and cleans training data

    df = pd.read_csv("train.csv")

    coordinates = []

    for row in range(len(df.index)):
        x = df["latitude"][row]
        y = df["longitude"][row]

        coordinates.append((x,y))

    df["coordinates"] = coordinates

    df.drop(["latitude", "longitude"], axis=1, inplace=True)

    year_week = []

    for row in range(len(df.index)):

        year = df["year"][row]
        week = df["week_no"][row]

        year_week.append("".join([str(year), str(week), "Mon"]))
    
    df["year_week"] = year_week


    df["year_week"] = pd.to_datetime(df["year_week"], format= "%Y%W%a")
    df["year_week"] = df["year_week"].dt.to_period("W")
    df.set_index(pd.PeriodIndex(df["year_week"], freq="W"),drop=True, inplace= True)
    df.drop("year_week", axis= 1, inplace=True)

    return df

def load_data_drop_2020():
    #Loads and cleans training data, dropping most of 2020 outlier data

    df = pd.read_csv("train.csv")

    coordinates = []

    for row in range(len(df.index)):
        x = df["latitude"][row]
        y = df["longitude"][row]

        coordinates.append((x,y))

    df["coordinates"] = coordinates

    df.drop(["latitude", "longitude"], axis=1, inplace=True)

    year_week = []

    for row in range(len(df.index)):

        year = df["year"][row]
        week = df["week_no"][row]

        year_week.append("".join([str(year), str(week), "Mon"]))
    
    df["year_week"] = year_week
    df["year_week"] = pd.to_datetime(df["year_week"], format= "%Y%W%a")

    for loc in df["coordinates"].unique():

        df_loc = df[df["coordinates"]== loc]
        df_loc = df_loc[df_loc["year"]==2020]

        df.drop(df_loc.index, inplace=True)

    df["year_week"] = df["year_week"].dt.to_period("W")
    df.set_index(pd.PeriodIndex(df["year_week"], freq="W"),drop=True, inplace= True)
    df.drop("year_week", axis= 1, inplace=True)

    return df

def save_model(forecaster, file_path):
    #Save trained model to directory

    model_filename = f"{file_path}.sav"
    joblib.dump(forecaster, model_filename)


if __name__ == "__main__":

    df = load_data_drop_2020()

    print(df["year"].unique)