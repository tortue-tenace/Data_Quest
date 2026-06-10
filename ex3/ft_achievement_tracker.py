import random as rd
print("=== Tracker Achievements ===")
def gen_player_achievements():
    achievements = ["Crafting Genius", "World Savior", "Master Explorer", "Strategist", "Speed Runner",
                    "Survivor", "Treasure Hunter", "Unstoppable", "First Steps", "Collector Supreme",
                    "Untouchable", "Sharp Mind", "Boss Slayer"]
    jason = set(rd.sample(achievements, k=rd.randint(1, len(achievements))))
    louis = set(rd.sample(achievements, k=rd.randint(1, len(achievements))))
    thomas = set(rd.sample(achievements, k=rd.randint(1, len(achievements))))
    booba = set(rd.sample(achievements, k=rd.randint(1, len(achievements))))
    print(f"Player Jason: {jason}")
    print(f"Player Louis: {louis}")
    print(f"Player Thomas: {thomas}")
    print(f"Player Booba: {booba}")
    print()
    distinct_achievements = jason.union(louis, thomas, booba)
    common_achievements = jason.intersection(louis,thomas, booba)

    print(f"Common achievements: {common_achievements if common_achievements else 'None'}")
    print()
    print(f"All distinct achievements: {distinct_achievements if distinct_achievements else 'None'}")
    print()
    print(f"Only Jason has: {jason.difference(louis, thomas, booba)}")
    print(f"Only Booba has: {booba.difference(louis, thomas, jason)}")
    print(f"Only Louis has: {louis.difference(jason, thomas, booba)}")
    print(f"Only Thomas has: {thomas.difference(louis, jason, booba)}")
    all_achievements = set(achievements)
    print()
    print(f"Jason is missing: {all_achievements - jason}")
    print(f"Louis is missing: {all_achievements - louis}")
    print(f"Thomas is missing: {all_achievements - thomas}")
    print(f"Booba is missing: {all_achievements - booba}")
