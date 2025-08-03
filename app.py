import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
sample_data = {
    "iso_code": ["MYS"] * 5,
    "continent": ["Asia"] * 5,
    "location": ["Malaysia"] * 5,
    "date": pd.date_range(start="2021-08-01", periods=5).strftime("%Y-%m-%d"),
    "total_cases": [1000000, 1010000, 1025000, 1040000, 1055000],
    "new_cases": [10000, 10000, 15000, 15000, 15000],
    "total_deaths": [8000, 8050, 8100, 8150, 8200],
    "new_deaths": [50, 50, 50, 50, 50]
}

# Create DataFrame and save to CSV
df_malaysia = pd.DataFrame(sample_data)
df_malaysia.to_csv("owid-covid-malaysia.csv", index=False)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("owid-covid-malaysia.csv")
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()

# Display success and preview
st.success("Data loaded successfully!")
st.dataframe(df.head())

# Plot total cases over time
st.subheader("COVID-19 Confirmed Cases Over Time in Malaysia")
fig, ax = plt.subplots()
ax.plot(df["date"], df["total_cases"], label="Total Confirmed Cases", color='blue')
ax.set_xlabel("Date")
ax.set_ylabel("Cases")
ax.legend()
st.pyplot(fig)

# Show latest stats
st.subheader("Latest COVID-19 Stats for Malaysia")
latest = df.iloc[-1]
st.metric("Total Confirmed Cases", f"{latest['total_cases']:,}")
st.metric("Total Deaths", f"{latest['total_deaths']:,}")
st.metric("New Cases (latest)", f"{latest['new_cases']:,}")
st.metric("New Deaths (latest)", f"{latest['new_deaths']:,}")
