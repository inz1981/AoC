
class Player:

    def __init__(self, hit_points: int, damage: int, armor: int):

        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor
        self.gold_spent = 0
        self.equipped = []

        #print(f"Player created with {self.hit_points, self.damage, self.armor}")

    def equip(self, item: dict):
        self.armor += item["armor"]
        self.damage += item["damage"]
        self.gold_spent += item["cost"]
        self.equipped.append(item)
        # print(f"Player got equipped with: {item['name']} (gold spent: {self.gold_spent})")
