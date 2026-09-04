import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from database.database import init_db
from ui.dashboard import render as dashboard
from ui.tasks import render_tasks, render_add
from ui.ai_features import render as ai, render_planner, render_productivity

st.set_page_config(page_title="AI To-Do", page_icon="✅", layout="wide")
init_db()

def main():
    st.sidebar.title("✅ AI To-Do")
    page=st.sidebar.radio("Navigation",["Dashboard","My Tasks","Add Task","AI Assistant","Daily Planner","Productivity"])
    st.sidebar.caption("Smart task management with optional AI")
    if page=="Dashboard": dashboard()
    elif page=="My Tasks": render_tasks()
    elif page=="Add Task": render_add()
    elif page=="AI Assistant": ai()
    elif page=="Daily Planner": render_planner()
    else: render_productivity()
if __name__=="__main__": main()
