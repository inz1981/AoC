
class Boss:

    def __init__(self, hit_points: int, damage: int):

        self.hit_points = hit_points
        self.damage = damage
        self.active_spells = []

        # print(f"Boss created with {self.hit_points, self.damage}")

    def apply_spell(self, spell: dict):
        self.active_spells.append(spell)
