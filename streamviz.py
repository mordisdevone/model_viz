import streamlit as st
from PIL import Image
import pandas as pd

# Assuming urls_df is accessible or loaded here
# urls_df = pd.read_csv('your_urls_data.csv')

st.set_page_config(layout="wide")

def load_image(image_path):
    try:
        image = Image.open(image_path)
        return image
    except FileNotFoundError:
        st.error(f"File not found: {image_path}")
        return None

def app():
    st.title('Weather Data Visualization')

    urls_df = pd.read_csv('urls_df.csv')
    # Dropdown for Date selection

    # Dropdown for Date selection (use HRRR Date as start date)
    available_dates = sorted(urls_df['HRRR Date'].unique())
    selected_date = st.selectbox("Select Date", available_dates)

    # Dropdown for Variable selection
    # Assuming the variable is consistent across the DataFrame, otherwise adjust
    selected_variable = st.selectbox("Select Variable", ['Temperature', 'WindSpeed', 'SurfacePressure'])

    # Slider for Hour selection (0 to 36 hours)
    selected_hour = st.slider("Select Hour", 0, 36)

    # Function to get plot names from the DataFrame
    def get_plot_names(date, hour):
        # Retrieve the row for the selected date and hour
        row = urls_df[(urls_df['HRRR Date'] == date) & (urls_df['HRRR F Value'] == hour)].iloc[0]
        return row['Diff Plot Name'], row['HRRR Plot Name'], row['RTMA Plot Name']

    diff_plot_name, hrrr_plot_name, rtma_plot_name = get_plot_names(selected_date, selected_hour)

    # Construct file paths for the plots
    diff_path = f'plotsFIN/{diff_plot_name}.png'
    hrrr_path = f'plotsFIN/{hrrr_plot_name}.png'
    rtma_path = f'plotsFIN/{rtma_plot_name}.png'

    # Load and display images
    col1, col2, col3 = st.columns([1,1,1])  # Equal width columns
    with col1:
        st.image(load_image(diff_path), caption='Difference Plot', use_column_width=True)
    with col2:
        st.image(load_image(hrrr_path), caption='HRRR Plot', use_column_width=True)
    with col3:
        st.image(load_image(rtma_path), caption='RTMA Plot', use_column_width=True)

if __name__ == "__main__":
    app()
