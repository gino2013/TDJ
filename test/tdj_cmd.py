from datetime import datetime, timedelta

class Character:
    def __init__(self, name, star, shards, daily_shards):
        self.name = name
        self.star = star
        self.shards = shards
        self.daily_shards = daily_shards
        self.shards_needed = {3: 60, 4: 120, 5: 180, 6: 0}  # 6星不再需要碎片提升

    def receive_shards(self):
        self.shards += self.daily_shards

    def check_star_up(self, current_day):
        upgraded = False
        while self.star < 6 and self.shards >= self.shards_needed[self.star]:
            self.shards -= self.shards_needed[self.star]
            self.star += 1
            upgrade_date = start_date + timedelta(days=current_day)
            print(f"{self.name} upgraded to {self.star} star on {upgrade_date.strftime('%Y-%m-%d')} with {self.shards} shards left")
            upgraded = True
        return upgraded

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
    print(f"{name} added to the queue.")

# # Initialization with the provided test case
# characters = [
#     Character('安逸', 4, 82, 4),   # 每天領4片
#     Character('劍聖', 5, 26, 3),   # 每天領3片
#     Character('蕭昊', 3, 30, 2)    # 每天領2片
# ]

# current_day = 0
# start_date = datetime.now()

# # List of new characters to be added
# new_characters_queue = [
#     {'name': '銀瑪', 'star': 4, 'shards': 0},
#     {'name': '諸葛艾', 'star': 4, 'shards': 43}
# ]

# Initialization with the provided test case
characters = [
    Character('紫楓', 5, 78, 4),   # 每天領4片
    Character('任斷離', 5, 54, 3),   # 每天領3片
    Character('安逸', 4, 36, 2)    # 每天領2片
]

current_day = 0
start_date = datetime.now()

# List of new characters to be added
new_characters_queue = [
    {'name': '月孛', 'star': 5, 'shards': 4},
    {'name': '玄羽', 'star': 5, 'shards': 15}
]

# Main loop
while any(c.star < 6 for c in characters) or new_characters_queue:
    current_day += 1
    for character in characters:
        if character.star < 6:
            character.receive_shards()
            if character.check_star_up(current_day):
                redistribute_shards(characters)
    
    # Check if there is any empty slot to add new characters
    active_characters_count = sum(1 for c in characters if c.star < 6)
    if active_characters_count < 3 and new_characters_queue:
        new_character_info = new_characters_queue.pop(0)
        add_new_character(characters, new_character_info['name'], new_character_info['star'], new_character_info['shards'])

print("All characters have reached 6 stars.")
