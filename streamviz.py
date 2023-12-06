import streamlit as st
from PIL import Image

# Set Streamlit page configuration to wide mode
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

    # Dropdown for Date selection
    selected_date = st.selectbox("Select Date", ['20220504', 'AnotherDate'])

    # Dropdown for Variable selection
    selected_variable = st.selectbox("Select Variable", ['Temperature', 'WindSpeed', 'SurfacePressure'])

    # Slider for Hour selection
    selected_hour = st.slider("Select Hour", 0, 23, format="Hour %02d")

    # File paths based on selections
    diff_path = f'plots2/DIFF_{selected_variable}_{selected_date}_Hour_{selected_hour:02d}_.png'
    hrrr_path = f'plots2/HRRR_{selected_variable}_{selected_date}_Hour_{selected_hour:02d}_.png'
    rtma_path = f'plots2/RTMA_{selected_variable}_{selected_date}_Hour_{selected_hour:02d}_.png'

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
