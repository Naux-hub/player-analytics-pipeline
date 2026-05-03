import streamlit as st
import duckdb
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Player Analytics Dashboard", layout="wide")

st.title("🕹️ Player Analytics Dashboard")
st.markdown("### Project: Analyzing Player Monetization & Lifecycle")

con = duckdb.connect('ecommerce.db')

# --- DATA LOADING ---
df_orders = con.execute("SELECT * FROM fct_orders").df()
df_retention = con.execute("SELECT * FROM mart_retention").df()

# Säkerställ att datum-kolumnerna är i rätt format
df_orders['purchased_at'] = pd.to_datetime(df_orders['purchased_at'])
df_retention['first_login_at'] = pd.to_datetime(df_retention['first_login_at'])

# --- SIDEBAR FILTER ---
st.sidebar.header("Global Filters")

# Skapa en lista på unika år + ett "All Years" alternativ
years = sorted(df_orders['purchased_at'].dt.year.unique().tolist())
years.insert(0, "All Years")

selected_year = st.sidebar.selectbox("Select Acquisition Year", years)

# --- FILTER LOGIC ---
if selected_year != "All Years":
    # Filtrera ordrar baserat på valt år
    df_orders = df_orders[df_orders['purchased_at'].dt.year == selected_year]
    # Filtrera retention baserat på när spelaren gjorde sitt FÖRSTA köp (Acquisition cohort)
    df_retention = df_retention[df_retention['first_login_at'].dt.year == selected_year]

# --- KPI RAD ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Gross Revenue", f"${df_orders['total_order_value'].sum():,.0f}")
with col2:
    st.metric("ARPPU", f"${df_orders['total_order_value'].mean():.2f}")
with col3:
    st.metric("Total Paying Players", f"{df_orders['customer_id'].nunique():,}")

st.divider()

# --- GRAFER ---
left, right = st.columns(2)

with left:
    st.subheader(f"Revenue by Player Region ({selected_year})")
    region_sales = df_orders.groupby('city')['total_order_value'].sum().nlargest(10).reset_index()
    fig = px.bar(region_sales, x='city', y='total_order_value', 
                 color_discrete_sequence=['#7f00ff'],
                 labels={'total_order_value': 'Revenue ($)', 'city': 'Region'})
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader(f"Retention: Days to 2nd Purchase ({selected_year})")
    if len(df_retention) > 0:
        fig_ret = px.histogram(df_retention, x="days_to_return", 
                               nbins=30,
                               color_discrete_sequence=['#00cc96'],
                               labels={'days_to_return': 'Days After First In-App Purchase'})
        st.plotly_chart(fig_ret, use_container_width=True)
    else:
        st.info(f"No re-engagement data found for {selected_year}.")