import streamlit as st
from datetime import datetime, timedelta
import plotly.graph_objects as go

def calculate_marriage_percentage(birthday1, birthday2, wedding_date):
    # Convert string dates to datetime objects
    birthday1 = datetime.strptime(birthday1, "%Y-%m-%d")
    birthday2 = datetime.strptime(birthday2, "%Y-%m-%d")
    wedding_date = datetime.strptime(wedding_date, "%Y-%m-%d")

    # Calculate total days of marriage
    total_days_married = (datetime.now() - wedding_date).days

    # Calculate percentage of life married
    total_days_life1 = (datetime.now() - birthday1).days
    total_days_life2 = (datetime.now() - birthday2).days
    percentage_married1 = (total_days_married / total_days_life1) * 100
    percentage_married2 = (total_days_married / total_days_life2) * 100

    return percentage_married1, percentage_married2

# Streamlit UI
st.set_page_config(page_title="Love Calculator", page_icon="💖")

# Main headline
st.title("Love Calculator ❤️")

# Input fields
col1, col2 = st.columns(2)
with col1:
    name1 = st.text_input("One Name", "Romeo")
    birthday1 = st.date_input(f"{name1}'s Birthday", datetime.now() - timedelta(days=32*365))

with col2:
    name2 = st.text_input("Other Name", "Juliet")
    birthday2 = st.date_input(f"{name2}'s Birthday", datetime.now() - timedelta(days=28*365))

wedding_date = st.date_input("🎊 Wedding Date 🎊", datetime.now() - timedelta(days=10*365))

# Calculate and display percentage
if st.button("Calculate ❤️ Percentage"):
    percentage1, percentage2 = calculate_marriage_percentage(str(birthday1), str(birthday2), str(wedding_date))

    # Pie charts
    fig1 = go.Figure(go.Pie(
        labels=[f"{name1} Married", f"{name1} Single"],
        values=[percentage1, 100 - percentage1],
        hole=.3,
        marker=dict(colors=['#FF1744', 'lightgrey'])
    ))
    fig1.update_layout(title=f"Percentage of {name1}'s life spent married", width=400, height=300, showlegend=False)

    fig2 = go.Figure(go.Pie(
        labels=[f"{name2} Married", f"{name2} Single"],
        values=[percentage2, 100 - percentage2],
        hole=.3,
        marker=dict(colors=['#FF1744', 'lightgrey'])
    ))
    fig2.update_layout(title=f"Percentage of {name2}'s life spent married", width=400, height=300, showlegend=False)

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig1)

    with col2:
        st.plotly_chart(fig2)