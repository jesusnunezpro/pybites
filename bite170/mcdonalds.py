import pandas as pd

data = "https://s3.us-east-2.amazonaws.com/bites-data/menu.csv"
# load the data in once, functions will use this module object
df = pd.read_csv(data)

pd.options.mode.chained_assignment = None  # ignore warnings


def get_food_most_calories(df=df):
    """Return the food "Item" string with most calories"""
    return df.loc[df["Calories"] == df.max()["Calories"]]["Item"].values[0]


def get_bodybuilder_friendly_foods(df=df, excl_drinks=False):
    """Calulate the Protein/Calories ratio of foods and return the
       5 foods with the best ratio.

       This function has a excl_drinks switch which, when turned on,
       should exclude 'Coffee & Tea' and 'Beverages' from this top 5.

       You will probably need to filter out foods with 0 calories to get the
       right results.

       Return a list of the top 5 foot Item stings."""
    if excl_drinks:
        ndf = df[df["Category"].isin(['Breakfast','Beef & Pork','Chicken & Fish', 'Salads','Snacks & Sides', 'Desserts'])]
    else:
        ndf = df
    return ndf.assign(Ratio = ndf["Protein"]/ndf["Calories"]).sort_values("Ratio", ascending=0).loc[ndf["Calories"] > 0].head(5)["Item"].values.tolist()
