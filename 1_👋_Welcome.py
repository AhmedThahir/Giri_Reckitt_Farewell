import streamlit as st

from common import *
import time

def main():
	common()

	st.title("Hi Giri! 👋")
	st.markdown("""
	It has been a lovely few months with you. Hope you like this :) ✨
	""")

	keys = ["b1", "b2", "b3"]
	for key in keys:
		if key not in st.session_state:
			st.session_state[key] = False

	if st.button("Click here to go to the next page") or st.session_state["b1"]:
		st.session_state["b1"] = True
		st.balloons()
		time.sleep(2)
		if st.button("Hmmm, maybe it's an error. Click here.") or st.session_state["b2"]:
			st.session_state["b2"] = True
			if st.button("Okay, okay. Last time.") or st.session_state["b3"]:
				st.session_state["b3"] = True
				st.info("""
				Sike. Use the sidebar to navigate.	  
				""", icon="👈")

main()