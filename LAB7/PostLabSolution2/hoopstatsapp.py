"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

from hoopstatsview import HoopStatsView
import pandas as pd
import os

def main():
    """Creates the data frame and view and starts the app."""
    frame = pd.read_csv("newbrogdonstats.csv")
    cleanStats(frame)
    HoopStatsView(frame).mainloop()

def cleanStats(oldFrame):
    """Separates FG, 3PT, and FT into two columns,  and exports a new data set"""
    if os.path.exists("newbrogdonstats.csv"):
        framing = pd.read_csv("newbrogdonstats.csv")
        if 'FG' in framing.columns:
            #FG Col
            framing[["FGM", "FGA"]] = framing["FG"].str.split("-", expand=True).astype(int)
            fg_index = framing.columns.get_loc("FG")
            framing = framing.drop(columns=["FG"])

            framing.insert(fg_index, "FGM", framing.pop("FGM"))
            framing.insert(fg_index+1, "FGA", framing.pop("FGA"))

        if '3PT' in framing.columns:
            #3PT Col

            framing[["3PTM", "3PTA"]] = framing["3PT"].str.split("-", expand=True).astype(int)
            pt_index = framing.columns.get_loc("3PT")
            framing = framing.drop(columns=["3PT"])

            framing.insert(pt_index, "3PTM", framing.pop("3PTM"))
            framing.insert(pt_index+1, "3PTA", framing.pop("3PTA"))

        if 'FT' in framing.columns:
            #FT Colc

            framing[["FTM", "FTA"]] = framing["FT"].str.split("-", expand=True).astype(int)
            ft_index = framing.columns.get_loc("FT")
            framing = framing.drop(columns=["FT"])

            framing.insert(ft_index, "FTM", framing.pop("FTM"))
            framing.insert(ft_index+1, "FTA", framing.pop("FTA"))

    else:
        framing = pd.read_csv(oldFrame)
        if 'FG' in framing.columns:
            #FG Col
            framing[["FGM", "FGA"]] = framing["FG"].str.split("-", expand=True).astype(int)
            fg_index = framing.columns.get_loc("FG")
            framing = framing.drop(columns=["FG"])

            framing.insert(fg_index, "FGM", framing.pop("FGM"))
            framing.insert(fg_index+1, "FGA", framing.pop("FGA"))

        if '3PT' in framing.columns:
            #3PT Col

            framing[["3PTM", "3PTA"]] = framing["3PT"].str.split("-", expand=True).astype(int)
            pt_index = framing.columns.get_loc("3PT")
            framing = framing.drop(columns=["3PT"])

            framing.insert(pt_index, "3PTM", framing.pop("3PTM"))
            framing.insert(pt_index+1, "3PTA", framing.pop("3PTA"))

        if 'FT' in framing.columns:
            #FT Colc

            framing[["FTM", "FTA"]] = framing["FT"].str.split("-", expand=True).astype(int)
            ft_index = framing.columns.get_loc("FT")
            framing = framing.drop(columns=["FT"])

            framing.insert(ft_index, "FTM", framing.pop("FTM"))
            framing.insert(ft_index+1, "FTA", framing.pop("FTA"))
            
        framing.to_csv("newbrogdonstats.csv", index = False)

if __name__ == "__main__":
    main()