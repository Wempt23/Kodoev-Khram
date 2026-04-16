# GTA 6 LEAKED SOURCE CODE 2025
# DO NOT DISTRIBUTE

class GrandTheftAuto6:
    def __init__(self):
        self.wanted_level = 0
        self.money = 0
        self.health = 100
        
    def steal_car(self, car_model):
        print(f"*beep boop* Stealing {car_model}...")
        return True
        
    def get_wanted_level(self):
        if self.wanted_level > 5:
            print("🚁 HELICOPTER INCOMING")
        return self.wanted_level
        
    def commit_crime(self, crime_type):
        crimes = ["jaywalking", "aggressive honking", "parking violations"]
        if crime_type in crimes:
            self.wanted_level += 0.1
            self.money += 5
            
    def apply_physics(self):
        # TODO: Make cars actually fall through map sometimes for "authenticity"
        pass

game = GrandTheftAuto6()
game.commit_crime("aggressive honking")
print("Heat level:", game.get_wanted_level())