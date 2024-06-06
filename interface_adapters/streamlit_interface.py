import sys
import os
import streamlit as st
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from domain.character import Character
from use_cases.use_cases import redistribute_shards, add_new_character, run_simulation

st.title("Character Upgrade Simulation")

if 'characters' not in st.session_state:
    st.session_state.characters = []
if 'new_characters_queue' not in st.session_state:
    st.session_state.new_characters_queue = []
if 'results' not in st.session_state:
    st.session_state.results = []
if 'start_date' not in st.session_state:
    st.session_state.start_date = datetime.now()

st.subheader("Add Initial Characters")
with st.form(key='add_initial_characters'):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("Daily 4 shards")
        name_4 = st.text_input("Name", key="name_4")
        star_4 = st.selectbox("Star Level", [3, 4, 5], key="star_4")
        shards_4 = st.number_input("Current Shards", min_value=0, step=1, key="shards_4")
        
    with col2:
        st.write("Daily 3 shards")
        name_3 = st.text_input("Name", key="name_3")
        star_3 = st.selectbox("Star Level", [3, 4, 5], key="star_3")
        shards_3 = st.number_input("Current Shards", min_value=0, step=1, key="shards_3")
        
    with col3:
        st.write("Daily 2 shards")
        name_2 = st.text_input("Name", key="name_2")
        star_2 = st.selectbox("Star Level", [3, 4, 5], key="star_2")
        shards_2 = st.number_input("Current Shards", min_value=0, step=1, key="shards_2")

    submit_initial = st.form_submit_button(label='Add Initial Characters')

    if submit_initial:
        if name_4 and name_3 and name_2:
            st.session_state.characters = [
                Character(name_4, star_4, shards_4, 4),
                Character(name_3, star_3, shards_3, 3),
                Character(name_2, star_2, shards_2, 2)
            ]
            redistribute_shards(st.session_state.characters)
            st.success("Initial characters added successfully.")
        else:
            st.error("Please fill in all initial character details.")

st.subheader("Add New Characters to Queue")
with st.form(key='add_new_character'):
    new_name = st.text_input("New Character Name")
    new_star = st.selectbox("New Character Star Level", [3, 4, 5], key='new_star')
    new_shards = st.number_input("New Character Current Shards", min_value=0, step=1, key='new_shards')
    new_submit_button = st.form_submit_button(label='Add New Character to Queue')

    if new_submit_button:
        st.session_state.new_characters_queue.append({'name': new_name, 'star': new_star, 'shards': new_shards})
        st.success(f"New character {new_name} will join the queue.")

if st.button('Run Simulation'):
    results = run_simulation(st.session_state.characters, st.session_state.new_characters_queue, st.session_state.start_date)
    st.session_state.results.extend(results)
    st.subheader("Simulation Results")
    for result in st.session_state.results:
        st.write(result)

    if all(c.star == 6 for c in st.session_state.characters):
        st.success("All characters have reached 6 stars.")
