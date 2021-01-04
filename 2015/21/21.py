import re
from game.boss import Boss
from game.player import Player
from game.store import Store


def read_input_file(path):
    with open(path) as f:
        content = f.read()
    hit_points, damage, armor = re.findall(
        r"Hit Points: (\d+)\nDamage: (\d+)\nArmor: (\d+)", content
    ).pop()
    return int(hit_points), int(damage), int(armor)


def battle(player: Player, boss: Boss) -> bool:
    player_turn = True
    while player.hit_points > 0 and boss.hit_points > 0:
        if player_turn:
            damage_dealt = player.damage - boss.armor
            if damage_dealt <= 0:
                damage_dealt = 1
            boss.hit_points -= damage_dealt
            # print(f"The player deals {player.damage}-{boss.armor} = {damage_dealt} "
            #       f"damage; the boss goes down to {boss.hit_points} hit points.")
            player_turn = False
        else:
            damage_dealt = boss.damage - player.armor
            if damage_dealt <= 0:
                damage_dealt = 1
            player.hit_points -= damage_dealt
            # print(f"The boss deals {boss.damage}-{player.armor} = {damage_dealt} "
            #       f"damage; the player goes down to {player.hit_points} hit points.")
            player_turn = True
    if player.hit_points <= 0:
        return False
    else:
        return True


def part_1(path: str) -> int:
    wins, _ = simulate_all_fights(path)
    return min([l.gold_spent for l in wins])


def part_2(path: str) -> int:
    _, losses = simulate_all_fights(path)
    return max([l.gold_spent for l in losses])


def simulate_all_fights(path: str):
    boss_hit_points, boss_damage, boss_armor = read_input_file(path)
    store = Store()
    weapons = store.get_weapons()
    rings = store.get_rings()
    armors = store.get_armors()

    item_combos = []
    for w in weapons:
        item_combos.append([w])
        for a in armors:
            item_combos.append([w, a])
            for r1 in rings:
                item_combos.append([w, a, r1])
                for r2 in rings:
                    if r2 == r1:
                        continue
                    item_combos.append([w, a, r1, r2])
        for r1 in rings:
            item_combos.append([w, r1])
            for r2 in rings:
                if r2 == r1:
                    continue
                item_combos.append([w, r1, r2])

    wins = []
    losses = []
    for items in item_combos:
        boss = Boss(boss_hit_points, boss_damage, boss_armor)
        player = Player(100, 0, 0)
        for item in items:
            player.equip(item)

        wins.append(player) if battle(player, boss) else losses.append(player)

    return wins, losses


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "21_input.txt"
    ans = part_1(filepath)
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "21_input.txt"
    ans = part_2(filepath)
    print(f"answer: {ans}")
