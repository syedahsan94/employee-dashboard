Here is the complete code for your **Streamlit Employee Performance Dashboard**. You can copy and paste this into a file named `employee_dashboard.py`:

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to clean and process the data
def clean_data(df):
    df = df.dropna(subset=['Employee'])
    df = df.reset_index(drop=True)

    # Convert columns to appropriate data types
    cols_to_convert = [
        'Total Time', 'Earned Mins', 'ACTUAL MIN', 'INDIRECT MIN',
        'BREAKS', 'LUNCH', 'ADJUST', 'EVENT', 'GAP MIN', 'EP%', 'UTIL%'
    ]
    for col in cols_to_convert:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

# Function to plot EP% and UTIL% per employee
def plot_metrics(df):
    fig, ax = plt.subplots(2, 1, figsize=(10, 8))

    # Plot EP%
    ax[0].bar(df['Employee'], df['EP%'], color='skyblue')
    ax[0].set_title('EP% per Employee')
    ax[0].set_xlabel('Employee')
    ax[0].set_ylabel('EP%')
    ax[0].tick_params(axis='x', rotation=90)

    # Plot UTIL%
    ax[1].bar(df['Employee'], df['UTIL%'], color='lightgreen')
    ax[1].set_title('UTIL% per Employee')
    ax[1].set_xlabel('Employee')
    ax[1].set_ylabel('UTIL%')
    ax[1].tick_params(axis='x', rotation=90)

    plt.tight_layout()
    st.pyplot(fig)

# Streamlit app
st.title('Employee Performance Dashboard')

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df = clean_data(df)

    st.subheader('Cleaned Data')
    st.dataframe(df)

    st.subheader('Performance Metrics')
    plot_metrics(df)

    st.subheader('Download Cleaned Data')
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name='cleaned_employee_performance.csv',
        mime='text/csv'
    )
```

Let me know if you'd like help saving this file or deploying it online!
