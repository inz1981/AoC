import random
import re
from game.boss import Boss
from game.player import Player


def read_input_file(path):
    with open(path) as f:
        content = f.read()
    hit_points, damage = re.findall(
        r"Hit Points: (\d+)\nDamage: (\d+)", content
    ).pop()
    return int(hit_points), int(damage)


def apply_active_spells(player: Player, boss: Boss):

    for spell in player.active_spells:
        spell["turns"] -= 1
        if spell["name"] == "Shield":
            # print(f"Shield increasing armor by 7 for {spell['turns']} turns.")
            player.armor = spell["armor"]
        elif spell["name"] == "Recharge":
            # print(f"{spell['name']} provides {spell['mana']} mana; its timer is now "
            #       f"{spell['turns']}.")
            player.mana += spell["mana"]
        else:
            raise NotImplementedError("Unknown Spell!")

        if not spell["turns"]:
            # print(f"{spell['name']} wears off.")
            player.active_spells.remove(spell)
            if spell["name"] == "Shield":
                player.armor = 0

    for spell in boss.active_spells:
        spell["turns"] -= 1
        if spell["name"] == "Poison":
            # print(f"{spell['name']} deals {spell['damage']} damage; its timer "
            #       f"is now {spell['turns']}.")
            boss.hit_points -= spell['damage']
        else:
            raise NotImplementedError("Unknown Spell!")

        if not spell["turns"]:
            # print(f"{spell['name']} wears off.")
            boss.active_spells.remove(spell)


def battle(player: Player, boss: Boss) -> bool:
    player_turn = True
    while player.hit_points > 0 and boss.hit_points > 0:
        # print("-- Boss turn --") if not player_turn else print("-- Player turn --")
        # print(f"- Player has {player.hit_points} hit points, {player.armor} armor, "
        #       f"{player.mana} mana")
        # print(f"- Boss has {boss.hit_points} hit points")

        apply_active_spells(player, boss)

        if player_turn:
            active_spells = [spell["name"] for spell in player.active_spells] + \
                            [spell["name"] for spell in boss.active_spells]
            spell = player.cast_spell(active_spells)

            if player.mana < spell["cost"]:
                print(f"Cannot cast spell, no mana left!")
                return False
            else:
                player.mana -= spell["cost"]
                player.mana_spent += spell["cost"]

            if spell["damage"]:
                if spell["turns"]:
                    #print(f"Player casts {spell['name']}.")
                    boss.apply_spell(spell)
                else:
                    if spell["heals"]:
                        player.hit_points += spell["heals"]
                    #print(f"Player casts {spell['name']}, "
                    #      f"dealing {spell['damage']} damage.")
                    boss.hit_points -= spell["damage"]
            else:
                #print(f"Player casts {spell['name']}.")
                player.apply_spell(spell)
            player_turn = False
        else:
            damage_dealt = boss.damage - player.armor
            if damage_dealt <= 0:
                damage_dealt = 1
            player.hit_points -= damage_dealt
            #print(f"Boss attacks for {damage_dealt} damage!")
            player_turn = True

        player.boss_hp = boss.hit_points

    if player.hit_points <= 0:
        return False
    else:
        return True


def battle_fixed(player: Player, boss: Boss) -> bool:
    spell_list = ['Shield', 'Recharge', 'Poison', 'Drain', 'Recharge',
                  'Magic Missile', 'Poison', 'Drain', 'Recharge',
                  'Magic Missile', 'Magic Missile', 'Magic Missile', 'Shield',
                  'Drain', 'Drain', 'Poison', 'Drain']
    player_turn = True
    while player.hit_points > 0 and boss.hit_points > 0:
        print("-- Boss turn --") if not player_turn else print("-- Player turn --")
        print(f"- Player has {player.hit_points} hit points, {player.armor} armor, "
              f"{player.mana} mana")
        print(f"- Boss has {boss.hit_points} hit points")

        apply_active_spells(player, boss)

        if player_turn:
            active_spells = [spell["name"] for spell in player.active_spells] + \
                            [spell["name"] for spell in boss.active_spells]
            # spell = player.cast_spell(active_spells)
            spell_name = spell_list.pop(0)
            for spell in player.get_spells():
                if spell['name'] == spell_name:
                    break

            if player.mana < spell["cost"]:
                print(f"Cannot cast spell, no mana left!")
                return False
            else:
                player.mana -= spell["cost"]
                player.mana_spent += spell["cost"]

            if spell["damage"]:
                if spell["turns"]:
                    print(f"Player casts {spell['name']}.")
                    boss.apply_spell(spell)
                else:
                    if spell["heals"]:
                        player.hit_points += spell["heals"]
                    print(f"Player casts {spell['name']}, "
                          f"dealing {spell['damage']} damage.")
                    boss.hit_points -= spell["damage"]
            else:
                print(f"Player casts {spell['name']}.")
                player.apply_spell(spell)
            player_turn = False
        else:
            damage_dealt = boss.damage - player.armor
            if damage_dealt <= 0:
                damage_dealt = 1
            player.hit_points -= damage_dealt
            print(f"Boss attacks for {damage_dealt} damage!")
            player_turn = True

    if player.hit_points <= 0:
        return False
    else:
        return True


def part_1(path: str) -> int:
    wins, _ = simulate_all_fights(path)

    result = []
    lowest_mana = 100000
    for pl in wins:
        if pl.mana_spent < lowest_mana:
            result = [pl]
            lowest_mana = pl.mana_spent
        elif pl.mana_spent == lowest_mana:
            result.append(pl)
    return min([l.mana_spent for l in wins])


def part__1(path: str) -> int:
    wins, _ = simulate_fixed_fight(path)

    result = []
    lowest_mana = 100000
    for pl in wins:
        if pl.mana_spent < lowest_mana:
            result = [pl]
            lowest_mana = pl.mana_spent
        elif pl.mana_spent == lowest_mana:
            result.append(pl)
    return min([l.mana_spent for l in wins])


def part_2(path: str) -> int:
    #_, losses = simulate_all_fights(path)
    #return max([l.gold_spent for l in losses])
    return 1


def simulate_all_fights(path: str):
    boss_hit_points, boss_damage = read_input_file(path)

    wins = []
    losses = []
    for x in range(1, 1000000):
        boss = Boss(boss_hit_points, boss_damage)
        player = Player(50, 0, 500)

        wins.append(player) if battle(player, boss) else losses.append(player)

    return wins, losses


def simulate_fixed_fight(path: str):
    boss_hit_points, boss_damage = read_input_file(path)

    wins = []
    losses = []
    boss = Boss(boss_hit_points, boss_damage)
    player = Player(50, 0, 500)

    wins.append(player) if battle_fixed(player, boss) else losses.append(player)

    return wins, losses


if __name__ == '__main__':
    print("----- part 1 -----")
    filepath = "22_input.txt"
    # ans = part_1(filepath)
    ans = part_1(filepath)
    print(f"answer: {ans}")

    print("----- part 2 -----")
    filepath = "22_input.txt"
    ans = part_2(filepath)
    print(f"answer: {ans}")
