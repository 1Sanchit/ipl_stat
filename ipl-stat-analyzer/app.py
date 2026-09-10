import streamlit as st

st.set_page_config(
    page_title="IPL Statistics Analyzer",
    page_icon="🏏",
    layout="wide"
)

st.title("🏏 IPL Statistics Analyzer")

st.sidebar.title("🏏 Navigation")

st.sidebar.success("Choose a page from the sidebar.")

st.markdown("""
## Welcome



### Features

- 📊 Dashboard
- 👤 Player Analysis
- 🏆 Team Analysis
- 📈 Visualizations
- 🥇 Records
- 🔍 Linear Search
- 🔢 Quick Sort

Use the **Pages** section in the left sidebar to open each module.
""")