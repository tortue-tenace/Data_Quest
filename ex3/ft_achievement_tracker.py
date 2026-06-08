import random as rd

def gen_player_achievements():
    achievements = ["Crafting genius", "World savior", "Master Explorer", "Strategist", "Minimalist", 
                    "Infected slayer", "Collector Boss", "Don't touch me", "How i met your father"]
    jason = set(rd.sample(achievements, k=rd.randint(0,len(achievements))))
    louis = set(rd.sample(achievements, k=rd.randint(0,len(achievements))))
    thomas = set(rd.sample(achievements, k=rd.randint(0,len(achievements))))
    booba = set(rd.sample(achievements, k=rd.randint(0,len(achievements))))
    print(f"Player Jason: {jason}")
    print(f"Player Louis: {louis}")
    print(f"Player Thomas: {thomas}")
    print(f"Player Booba: {booba}")

gen_player_achievements()