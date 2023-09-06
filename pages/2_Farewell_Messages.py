import streamlit as st

from common import *
import os

import pandas as pd
import plotly.express as px
from streamlit_plotly_events import plotly_events

def get_name(file):
  file_name = os.path.basename(file)
  new_file_name = os.path.splitext(file_name)[0] # + "_Copy" + os.path.splitext(file_name)[1]
  
  return new_file_name

@st.cache_data(ttl=60*60)
def get_data():
	return pd.read_csv("./data.csv")

def get_row(df):
	return df.iloc[st.session_state["event"][0]["pointIndex"]]

def main():
	common()

	directory = "./Messages"
	people = os.listdir(directory)
	people.sort()

	df = get_data()

	if "event" in st.session_state and len(st.session_state["event"]) > 0:
		row = get_row(df)
		lat, lon = row["Lat"], row["Lon"]
	else:
		lat, lon = df.iloc[0]["Lat"], df.iloc[0]["Lon"]

	fig = px.scatter_geo(
		df,
		lat="Lat",
		lon="Lon",
		hover_name="Name",
		projection="orthographic",
		center=dict(lon=lon, lat=lat),
	)
	fig.update_geos(
		projection_rotation=dict(lon=lon, lat=lat, roll=0),
	)
	fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
	fig.update_traces(marker=dict(size=10))

	c1, c2 = st.columns([1, 1])

	with c1:
		st.session_state["event"] = plotly_events(fig, click_event=True, hover_event=False, key="idk")

	if len(st.session_state["event"])==0:
		st.info("Choose someone from the map", icon="👆")
		st.stop()

	name = get_row(df)["Name"]
	
	file_name = f"{name}.md"

	with c2:
		with open(os.path.join(directory, file_name), "r") as f:
			st.header("👋 " + name)
			with st.chat_message("human"):
				st.markdown(f.read())

main()