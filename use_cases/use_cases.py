from datetime import datetime, timedelta

def redistribute_shards(characters):
    active_characters = [c for c in characters if c.star < 6]
    if len(active_characters) >= 2:
        active_characters[0].daily_shards = 4
        active_characters[1].daily_shards = 3
        if len(active_characters) > 2:
            for i in range(2, len(active_characters)):
                active_characters[i].daily_shards = 2

def add_new_character(characters, name, star, shards):
    new_character = Character(name, star, shards, 2)
    characters.append(new_character)
    redistribute_shards(characters)

def run_simulation(characters, new_characters_queue, start_date):
    current_day = 0
    results = []

    while any(c.star < 6 for c in characters) or new_characters_queue:
        current_day += 1
        for character in characters:
            if character.star < 6:
                character.receive_shards()
                upgrades = character.check_star_up(current_day, start_date)
                if upgrades:
                    results.extend(upgrades)
                    redistribute_shards(characters)

        active_characters_count = sum(1 for c in characters if c.star < 6)
        if active_characters_count < 3 and new_characters_queue:
            new_character_info = new_characters_queue.pop(0)
            add_new_character(characters, new_character_info['name'], new_character_info['star'], new_character_info['shards'])

    return results
