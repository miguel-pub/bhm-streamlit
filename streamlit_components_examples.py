import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
import pydeck as pdk
import graphviz
from datetime import time, datetime
import time as tm

# Page Configuration
st.set_page_config(
    page_title="Streamlit Components Guide",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to",
    ["Display Elements", "Media Elements", "Data Display", "Input Widgets", 
     "Layout & Containers", "Status Elements", "Charts & Visualization", 
     "Cache & Performance", "Additional Elements", "State Management"]
)

# Main title
st.title("Streamlit Components Guide")
st.markdown("A comprehensive guide to Streamlit components with examples.")

# Create sample data for examples
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

# Display Elements
if section == "Display Elements":
    st.header("Display Elements")
    
    st.subheader("st.write()")
    st.write("st.write() is the Swiss Army knife for displaying content")
    st.write(df)  # Can display dataframes
    st.write("It can also display", "multiple arguments", 123)  # Multiple arguments
    
    st.subheader("st.text()")
    st.text("This is plain text. No formatting applied.")
    
    st.subheader("st.markdown()")
    st.markdown("You can use **bold** or *italic* text with markdown.")
    st.markdown("### This is a markdown header")
    
    st.subheader("st.latex()")
    st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k = a \frac{1-r^{n}}{1-r}
    ''')
    
    st.subheader("Headings")
    st.title("This is a title")
    st.header("This is a header")
    st.subheader("This is a subheader")
    
    st.subheader("st.caption()")
    st.caption("This is a small caption text below other elements")
    
    st.subheader("st.code()")
    st.code("""
    def hello_world():
        print("Hello, World!")
    
    # Call the function
    hello_world()
    """, language="python")
    
    st.subheader("st.metric()")
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
    col1, col2, col3 = st.columns(3)
    col1.metric("Revenue", "$6,000", "+8%")
    col2.metric("Users", "1,200", "-2%")
    col3.metric("Conversion", "4.2%", "0.5%")

# Media Elements
elif section == "Media Elements":
    st.header("Media Elements")
    
    st.subheader("st.image()")
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", 
             caption="Streamlit Logo", width=300)
    
    st.subheader("st.audio()")
    st.audio("https://www2.cs.uic.edu/~i101/SoundFiles/StarWars3.wav", format="audio/wav")
    
    st.subheader("st.video()")
    st.video("https://www.youtube.com/watch?v=B2iAodr0fOo")

# Data Display
elif section == "Data Display":
    st.header("Data Display")
    
    st.subheader("st.dataframe()")
    st.dataframe(df.style.highlight_max(axis=0))
    
    st.subheader("st.table()")
    st.table(df)
    
    st.subheader("st.json()")
    st.json({
        'name': 'John',
        'age': 30,
        'city': 'New York',
        'skills': ['Python', 'SQL', 'Streamlit']
    })
    
    st.subheader("st.expander()")
    with st.expander("Click to expand"):
        st.write("This content is hidden until you expand it.")
        st.dataframe(df)

# Input Widgets
elif section == "Input Widgets":
    st.header("Input Widgets")
    
    st.subheader("st.button()")
    if st.button("Click me"):
        st.write("Button clicked!")
    
    st.subheader("st.checkbox()")
    agree = st.checkbox("I agree")
    if agree:
        st.write("You agreed!")
    
    st.subheader("st.radio()")
    genre = st.radio(
        "What's your favorite movie genre",
        ["Comedy", "Drama", "Documentary", "Sci-Fi"]
    )
    st.write(f"You selected: {genre}")
    
    st.subheader("st.selectbox()")
    option = st.selectbox(
        "How would you like to be contacted?",
        ["Email", "Phone", "SMS"]
    )
    st.write(f"You selected: {option}")
    
    st.subheader("st.multiselect()")
    options = st.multiselect(
        "What are your favorite colors",
        ["Green", "Yellow", "Red", "Blue", "Purple"],
        ["Yellow", "Red"]
    )
    st.write(f"You selected: {options}")
    
    st.subheader("st.slider()")
    age = st.slider("How old are you?", 0, 130, 25)
    st.write(f"I'm {age} years old")
    
    st.subheader("st.select_slider()")
    size = st.select_slider(
        "Select a size",
        options=["XS", "S", "M", "L", "XL"]
    )
    st.write(f"You selected: {size}")
    
    st.subheader("st.text_input()")
    name = st.text_input("What's your name?")
    if name:
        st.write(f"Hello {name}!")
    
    st.subheader("st.text_area()")
    message = st.text_area("Tell me about yourself")
    if message:
        st.write(f"You wrote: {message}")
    
    st.subheader("st.number_input()")
    number = st.number_input("Enter a number", min_value=0, max_value=100, value=50)
    st.write(f"The number is {number}")
    
    st.subheader("st.date_input()")
    date = st.date_input("When is your birthday?")
    st.write(f"Your birthday is: {date}")
    
    st.subheader("st.time_input()")
    appointment = st.time_input("Schedule your appointment", time(12, 0))
    st.write(f"Your appointment is at: {appointment}")
    
    st.subheader("st.file_uploader()")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        st.write(f"Filename: {uploaded_file.name}")
    
    st.subheader("st.color_picker()")
    color = st.color_picker("Pick a color", "#00f900")
    st.write(f"The selected color is {color}")

# Layout & Containers
elif section == "Layout & Containers":
    st.header("Layout & Containers")
    
    st.subheader("st.sidebar")
    st.write("The sidebar is already being used for navigation in this app!")
    
    st.subheader("st.columns()")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Column 1")
        st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=100)
    with col2:
        st.header("Column 2")
        st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=100)
    with col3:
        st.header("Column 3")
        st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=100)
    
    st.subheader("st.container()")
    container = st.container()
    container.write("This is inside a container")
    st.write("This is outside the container")
    container.write("This is also inside the container but appears after the outside text")
    
    st.subheader("st.tabs()")
    tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
    with tab1:
        st.write("This is tab 1")
        st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=100)
    with tab2:
        st.write("This is tab 2")
        st.video("https://www.youtube.com/watch?v=B2iAodr0fOo")
    with tab3:
        st.write("This is tab 3")
        st.button("Click me")
    
    st.subheader("st.expander()")
    with st.expander("Click to see more"):
        st.write("Hidden content revealed!")
        st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=100)

# Status Elements
elif section == "Status Elements":
    st.header("Status Elements")
    
    st.subheader("st.progress()")
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        tm.sleep(0.01)
        progress_bar.progress(percent_complete + 1)
    st.write("Progress complete!")
    
    st.subheader("st.spinner()")
    with st.spinner("Loading..."):
        tm.sleep(1)
    st.write("Done!")
    
    st.subheader("Notification banners")
    st.error("This is an error message")
    st.warning("This is a warning message")
    st.info("This is an informational message")
    st.success("This is a success message")
    
    st.subheader("st.exception()")
    try:
        1/0
    except Exception as e:
        st.exception(e)
    
    st.subheader("st.toast()")
    if st.button("Show toast notification"):
        st.toast("This is a toast notification!")

# Charts & Visualization
elif section == "Charts & Visualization":
    st.header("Charts & Visualization")
    
    st.subheader("Simple charts")
    st.line_chart(chart_data)
    st.area_chart(chart_data)
    st.bar_chart(chart_data)
    
    st.subheader("st.pyplot()")
    fig, ax = plt.subplots()
    ax.scatter([1, 2, 3], [1, 2, 3])
    st.pyplot(fig)
    
    st.subheader("st.altair_chart()")
    chart = alt.Chart(chart_data).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
    )
    st.altair_chart(chart, use_container_width=True)
    
    st.subheader("st.plotly_chart()")
    fig = px.scatter(chart_data, x='a', y='b', size='c', color='c')
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("st.pydeck_chart()")
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'HexagonLayer',
                data=map_data,
                get_position='[lon, lat]',
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
        ],
    ))
    
    st.subheader("st.graphviz_chart()")
    graph = graphviz.Digraph()
    graph.edge('A', 'B')
    graph.edge('B', 'C')
    graph.edge('C', 'D')
    graph.edge('D', 'A')
    st.graphviz_chart(graph)
    
    st.subheader("st.map()")
    st.map(map_data)

# Cache & Performance
elif section == "Cache & Performance":
    st.header("Cache & Performance")
    
    st.subheader("st.cache_data()")
    
    @st.cache_data
    def expensive_computation(a, b):
        # This function will only be run once if the inputs don't change
        tm.sleep(2)  # Simulating an expensive computation
        return a * b
    
    a, b = st.slider("Select a value for a", 1, 10, 5), st.slider("Select a value for b", 1, 10, 5)
    result = expensive_computation(a, b)
    st.write(f"Result: {a} * {b} = {result}")
    st.write("Change the sliders and notice how the function runs instantly when using the same values again")
    
    st.subheader("st.cache_resource()")
    
    @st.cache_resource
    def get_database_connection():
        # This would normally connect to a database
        tm.sleep(2)  # Simulating connection time
        return "Database Connection Object"
    
    if st.button("Connect to database"):
        conn = get_database_connection()
        st.write(f"Connected: {conn}")
        st.write("Click again and notice it's instant")

# Additional Elements
elif section == "Additional Elements":
    st.header("Additional Elements")
    
    st.subheader("st.balloons() & st.snow()")
    if st.button("Celebrate with balloons"):
        st.balloons()
    if st.button("Let it snow"):
        st.snow()
    
    st.subheader("st.echo()")
    with st.echo():
        # This code will be displayed and then executed
        def get_square(x):
            return x * x
        
        for i in range(1, 6):
            st.write(f"{i} squared is {get_square(i)}")
    
    st.subheader("st.form()")
    with st.form("my_form"):
        st.write("Inside the form")
        name = st.text_input("Your name")
        age = st.slider("Your age", 0, 120, 25)
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write(f"Hello {name}, you are {age} years old")
    
    st.subheader("st.download_button()")
    text_contents = "This is the content of the file"
    st.download_button(
        label="Download text file",
        data=text_contents,
        file_name="example.txt",
        mime="text/plain"
    )
    
    st.subheader("st.camera_input()")
    camera_image = st.camera_input("Take a picture")
    if camera_image:
        st.image(camera_image)
        st.write(f"Image size: {camera_image.size} bytes")

# State Management
elif section == "State Management":
    st.header("State Management")
    
    st.subheader("st.session_state")
    
    # Initialize session state values if they don't exist
    if 'count' not in st.session_state:
        st.session_state.count = 0
    
    if 'text' not in st.session_state:
        st.session_state.text = ""
    
    # Display current state
    st.write(f"Count: {st.session_state.count}")
    st.write(f"Text: {st.session_state.text}")
    
    # Buttons to modify state
    if st.button("Increment Count"):
        st.session_state.count += 1
        st.experimental_rerun()
    
    # Text input that updates state
    new_text = st.text_input("Enter text to store in session state")
    if st.button("Update Text"):
        st.session_state.text = new_text
        st.experimental_rerun()
    
    # Display the full session state
    st.write("Full session state:")
    st.write(st.session_state) 