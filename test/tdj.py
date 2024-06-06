import streamlit as st
from datetime import datetime, timedelta
import os
import subprocess

# 确保PyInstaller检测到这些依赖项
import streamlit
import importlib_metadata

# 使用subprocess模块运行streamlit run命令
streamlit_path = "/Users/cfh00892977/FM/TDJ"
subprocess.run([streamlit_path, "run", "tdj.py"])

class Character:
    def __init__(self, name, star, shards, daily_shards):
        self.name = name
        self.star = star
        self.shards = shards
        self.daily_shards = daily_shards
        self.shards_needed = {3: 60, 4: 120, 5: 180, 6: 0}  # 6星不再需要碎片提升

    def receive_shards(self):
        self.shards += self.daily_shards

    def check_star_up(self, current_day, start_date):
        upgrades = []
        while self.star < 6 and self.shards >= self.shards_needed[self.star]:
            self.shards -= self.shards_needed[self.star]
            self.star += 1
            upgrade_date = start_date + timedelta(days=current_day)
            upgrades.append(f"{self.name} upgraded to {self.star} star on {upgrade_date.strftime('%Y-%m-%d')} with {self.shards} shards left")
        return upgrades

def redistribute_shards(characters):
    active_characters = [c for c in characters if c.star < 6]
    if len(active_characters) >= 2:
        active_characters[0].daily_shards = 4
        active_characters[1].daily_shards = 3
        if len(active_characters) > 2:
            for i in range(2, len(active_characters)):
                active_characters[i].daily_shards = 2

def add_new_character(characters, name, star, shards):
    new_character = Character(name, star, shards, 2)  # 初始每日領2片
    characters.append(new_character)
    redistribute_shards(characters)
    st.success(f"{name} added to the queue.")

# Streamlit UI
st.title("Character Upgrade Simulation")

# Initialization
if 'characters' not in st.session_state:
    st.session_state.characters = []
if 'new_characters_queue' not in st.session_state:
    st.session_state.new_characters_queue = []
if 'results' not in st.session_state:
    st.session_state.results = []
if 'start_date' not in st.session_state:
    st.session_state.start_date = datetime.now()

# Add initial characters form
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

# Add new characters to the queue
st.subheader("Add New Characters to Queue")
with st.form(key='add_new_character'):
    new_name = st.text_input("New Character Name")
    new_star = st.selectbox("New Character Star Level", [3, 4, 5], key='new_star')
    new_shards = st.number_input("New Character Current Shards", min_value=0, step=1, key='new_shards')
    new_submit_button = st.form_submit_button(label='Add New Character to Queue')

    if new_submit_button:
        st.session_state.new_characters_queue.append({'name': new_name, 'star': new_star, 'shards': new_shards})
        st.success(f"New character {new_name} will join the queue.")

# Simulation
if st.button('Run Simulation'):
    current_day = 0

    while any(c.star < 6 for c in st.session_state.characters) or st.session_state.new_characters_queue:
        current_day += 1
        for character in st.session_state.characters:
            if character.star < 6:
                character.receive_shards()
                upgrades = character.check_star_up(current_day, st.session_state.start_date)
                if upgrades:
                    st.session_state.results.extend(upgrades)
                    redistribute_shards(st.session_state.characters)

        # Check if there is any empty slot to add new characters
        active_characters_count = sum(1 for c in st.session_state.characters if c.star < 6)
        if active_characters_count < 3 and st.session_state.new_characters_queue:
            new_character_info = st.session_state.new_characters_queue.pop(0)
            add_new_character(st.session_state.characters, new_character_info['name'], new_character_info['star'], new_character_info['shards'])

    # Display results
    st.subheader("Simulation Results")
    for result in st.session_state.results:
        st.write(result)

    if all(c.star == 6 for c in st.session_state.characters):
        st.success("All characters have reached 6 stars.")

# ---------------------------------------------------
# from datetime import datetime, timedelta

# class Character:
#     def __init__(self, name, star, shards, daily_shards):
#         self.name = name
#         self.star = star
#         self.shards = shards
#         self.daily_shards = daily_shards
#         self.shards_needed = {3: 60, 4: 120, 5: 180, 6: 0}  # 6星不再需要碎片提升

#     def receive_shards(self):
#         self.shards += self.daily_shards

#     def check_star_up(self, current_day):
#         upgraded = False
#         while self.star < 6 and self.shards >= self.shards_needed[self.star]:
#             self.shards -= self.shards_needed[self.star]
#             self.star += 1
#             upgrade_date = start_date + timedelta(days=current_day)
#             print(f"{self.name} upgraded to {self.star} star on {upgrade_date.strftime('%Y-%m-%d')} with {self.shards} shards left")
#             upgraded = True
#         return upgraded

# def redistribute_shards(characters):
#     active_characters = [c for c in characters if c.star < 6]
#     if len(active_characters) >= 2:
#         active_characters[0].daily_shards = 4
#         active_characters[1].daily_shards = 3
#         if len(active_characters) > 2:
#             for i in range(2, len(active_characters)):
#                 active_characters[i].daily_shards = 2

# def add_new_character(characters, name, star, shards):
#     new_character = Character(name, star, shards, 2)  # 初始每日領2片
#     characters.append(new_character)
#     redistribute_shards(characters)
#     print(f"{name} added to the queue.")

# # # Initialization with the provided test case
# # characters = [
# #     Character('安逸', 4, 82, 4),   # 每天領4片
# #     Character('劍聖', 5, 26, 3),   # 每天領3片
# #     Character('蕭昊', 3, 30, 2)    # 每天領2片
# # ]

# # current_day = 0
# # start_date = datetime.now()

# # # List of new characters to be added
# # new_characters_queue = [
# #     {'name': '銀瑪', 'star': 4, 'shards': 0},
# #     {'name': '諸葛艾', 'star': 4, 'shards': 43}
# # ]

# # Initialization with the provided test case
# characters = [
#     Character('紫楓', 5, 78, 4),   # 每天領4片
#     Character('任斷離', 5, 54, 3),   # 每天領3片
#     Character('安逸', 4, 36, 2)    # 每天領2片
# ]

# current_day = 0
# start_date = datetime.now()

# # List of new characters to be added
# new_characters_queue = [
#     {'name': '月孛', 'star': 5, 'shards': 4},
#     {'name': '玄羽', 'star': 5, 'shards': 15}
# ]

# # Main loop
# while any(c.star < 6 for c in characters) or new_characters_queue:
#     current_day += 1
#     for character in characters:
#         if character.star < 6:
#             character.receive_shards()
#             if character.check_star_up(current_day):
#                 redistribute_shards(characters)
    
#     # Check if there is any empty slot to add new characters
#     active_characters_count = sum(1 for c in characters if c.star < 6)
#     if active_characters_count < 3 and new_characters_queue:
#         new_character_info = new_characters_queue.pop(0)
#         add_new_character(characters, new_character_info['name'], new_character_info['star'], new_character_info['shards'])

# print("All characters have reached 6 stars.")


# ---------------------------------------------------
# from collections import deque

# # 定義升級所需碎片數量
# level_up_requirements = {
#     4: 60,
#     5: 120,
#     6: 180
# }

# def calculate_level_up_dates(characters):
#     # 創建一個佇列來存放每個角色的資訊
#     queue = deque(characters)
    
#     # 定義每天可獲得的碎片數量循環
#     daily_fragments_cycle = deque([4, 3, 2])
    
#     # 初始化字典來儲存每個角色升級日期
#     level_up_dates = {char['name']: {} for char in characters}
    
#     # 初始化當前日期
#     current_date = 1
    
#     while queue:
#         for _ in range(len(queue)):
#             # 取出當前角色
#             current_char = queue.popleft()
#             name = current_char['name']
#             current_level = current_char['level']
#             current_fragments = current_char['fragments']
            
#             # 計算升級到下一個星級所需的碎片數量
#             next_level = current_level + 1
#             if next_level == 7:
#                 continue
            
#             fragments_needed = level_up_requirements[next_level] - current_fragments
            
#             # 每日獲得的碎片數量
#             daily_fragments_count = daily_fragments_cycle.popleft()
            
#             # 計算升級所需天數
#             days_needed = (fragments_needed + daily_fragments_count - 1) // daily_fragments_count
            
#             # 記錄升級日期
#             level_up_date = current_date + days_needed
#             level_up_dates[name][next_level] = level_up_date
            
#             # 更新角色資訊
#             current_char['level'] = next_level
#             current_char['fragments'] = (days_needed * daily_fragments_count + current_fragments) - level_up_requirements[next_level]
            
#             # 將角色加回佇列，如果未升到6星
#             if next_level < 6:
#                 queue.append(current_char)
            
#             # 每日碎片數量循環
#             daily_fragments_cycle.append(daily_fragments_count)
        
#         # 更新當前日期
#         current_date += 1
    
#     return level_up_dates

# characters = [
#     {'name': '安逸', 'level': 4, 'fragments': 82},
#     {'name': '劍聖', 'level': 5, 'fragments': 26},
#     {'name': '蕭昊', 'level': 3, 'fragments': 30}
# ]

# level_up_dates = calculate_level_up_dates(characters)
# print(level_up_dates)
