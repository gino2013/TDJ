from datetime import timedelta

class Character:
    def __init__(self, name, star, shards, daily_shards):
        self.name = name
        self.star = star
        self.shards = shards
        self.daily_shards = daily_shards
        self.shards_needed = {3: 60, 4: 120, 5: 180, 6: 0}

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
