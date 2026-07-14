import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 AI Stats Dashboard")

# File Upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Raw Data")
    st.write(df)

    # Column selection
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns

    if len(numeric_columns) > 0:
        column = st.selectbox("Select column to analyze", numeric_columns, index=0)

        # Slider filter
        min_val = int(df[column].min())
        max_val = int(df[column].max())

        selected_range = st.slider(
            "Select range",
            min_val, max_val, (min_val, max_val)
        )

        filtered_df = df[
            (df[column] >= selected_range[0]) &
            (df[column] <= selected_range[1])
        ]

        st.subheader("🔍 Filtered Data")
        st.write(filtered_df)

        # Chart
        st.subheader("📈 Chart")
        fig, ax = plt.subplots()
        ax.hist(filtered_df[column])
        st.pyplot(fig)

    else:
        st.warning("No numeric columns found!")