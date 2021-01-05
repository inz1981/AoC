import random


class Player:

    def __init__(self, hit_points: int, armor: int, mana: int):

        self.hit_points = hit_points
        self.armor = armor
        self.mana = mana
        self.mana_spent = 0
        self.active_spells = []
        self.cast_order = []
        self.boss_hp = 71

        # print(f"Player created with {self.hit_points, self.mana}")

    def apply_spell(self, spell: dict):
        self.active_spells.append(spell)

    def get_spells(self):
        spells = [
            {
                "name": "Magic Missile",
                "cost": 53,
                "damage": 4,
                "heals": 0,
                "mana": 0,
                "armor": 0,
                "turns": 0,
            },
            {
                "name": "Drain",
                "cost": 73,
                "damage": 2,
                "heals": 2,
                "mana": 0,
                "armor": 0,
                "turns": 0,
            },
            {
                "name": "Shield",
                "cost": 113,
                "damage": 0,
                "heals": 0,
                "mana": 0,
                "armor": 7,
                "turns": 6,
            },
            {
                "name": "Poison",
                "cost": 173,
                "damage": 3,
                "heals": 0,
                "mana": 0,
                "armor": 0,
                "turns": 6,
            },
            {
                "name": "Recharge",
                "cost": 229,
                "damage": 0,
                "heals": 0,
                "mana": 101,
                "armor": 0,
                "turns": 5,
            },
        ]
        return spells

    def get_spell(self, name: str):

        for spell in self.get_spells():
            if spell['name'] == name:
                return spell
        raise NotImplementedError(f"Unknown Spell: {name}")

    def cast_spell(self, active_spells: list):
        available_spells = [
            spell for spell in self.get_spells() if not spell['name'] in active_spells
        ]
        mana_ok = False
        for active in self.active_spells:
            if active['name'] == "Recharge":
                mana_ok = True

        if self.mana <= 229 + 113 and not mana_ok:
            mana_ok = False
        else:
            for available in available_spells:
                if available['name'] == "Recharge":
                    available_spells.remove(available)
                    mana_ok = True

        if mana_ok:
            spell = random.choice(available_spells)
        else:
            spell = self.get_spell("Recharge")
        self.cast_order.append(spell["name"])
        return spell

