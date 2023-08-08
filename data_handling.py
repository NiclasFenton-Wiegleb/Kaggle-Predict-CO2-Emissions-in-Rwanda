#Dependencies

import pandas as pd

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

def save_model(forecaster, file_path):
    #Save trained model to directory

    model_filename = f"{file_path}.sav"
    joblib.dump(forecaster, model_filename)


if __name__ == "__main__":

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

    print(df[df["coordinates"]==(-0.51, 29.29)])