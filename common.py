import streamlit as st

def common():
    st.set_page_config(
		page_title = "Giri Reckitt Farewell",
		layout="wide",
        initial_sidebar_state="collapsed",
		page_icon = "🎊"
	)
    common_styles = """
		<style>
		
        /*
		.block-container {
			padding-top: 0rem;
			padding-bottom: 0rem;
		}
        */
		
		/* [data-testid="stToolbar"], */
		#MainMenu,
		footer
		{visibility: hidden; !important}
		
		</style>
		"""
    st.markdown(common_styles, unsafe_allow_html=True)
