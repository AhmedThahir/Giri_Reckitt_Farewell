import streamlit as st

from common import *
import os

import pandas as pd
import plotly.express as px
from streamlit_plotly_events import plotly_events


def get_name(file):
    file_name = os.path.basename(file)
    # + "_Copy" + os.path.splitext(file_name)[1]
    new_file_name = os.path.splitext(file_name)[0]

    return new_file_name


@st.cache_data(ttl=60*60)
def get_data():
    return pd.read_csv("./data.csv")


def get_row(df, event):
    return df.iloc[event[0]["pointIndex"]]


def main():
    common()

    directory = "./Messages"
    people = os.listdir(directory)
    people.sort()

    df = get_data()

    fig = px.scatter_geo(
        df,
        lat="Lat",
        lon="Lon",
        hover_name="Name",
        projection="orthographic",
        # center = (0, 0)
    )
    fig.update_geos(
        # (meters) : higher number --> lower detail --> smoother
        resolution=110,
        bgcolor='hsla(0, 0%, 0%, 0)',

        showcountries=True, countrycolor="Grey",
        showcoastlines=True, coastlinecolor="Grey",

        showland=True, landcolor="LightYellow",
        showocean=True, oceancolor="LightBlue",
        # showlakes=True, lakecolor="LightBlue",
        # showrivers=True, rivercolor="LightBlue",
    )

    fig.update_layout(
        margin=dict(r=0, t=0, l=0, b=0),
        uirevision="foo",
        overwrite=True,
        paper_bgcolor='hsla(0, 0%, 0%, 0)',
        plot_bgcolor='hsla(0, 0%, 0%, 0)',
        modebar=dict(
            bgcolor='hsla(0, 0%, 0%, 0.5)',
            color='hsla(0, 0%, 100%, 0.5)',
        )
    )

    c1, c2 = st.columns([1, 1])

    with c1:
        event = plotly_events(fig, click_event=True,
                              hover_event=False, key="idk")

    if len(event) == 0:
        with c2:
            st.info("Choose someone from the map", icon="👈")
        st.stop()

    name = get_row(df, event)["Name"]

    file_name = f"{name}.md"

    with c2:
        with open(os.path.join(directory, file_name), "r") as f:
            st.header("👋 " + name)
            with st.chat_message("human"):
                st.markdown(f.read())


main()
