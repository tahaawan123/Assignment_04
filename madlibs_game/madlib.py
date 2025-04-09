def mad_libs():
    print("Let's play Mad Libs! fill in the blanks with your oen words.")

    name = input("Give me a name: ")
    place = input("Give me a place: ")
    funny_adj = input("Give me a funny adjective: ")
    random_obj = input("Give me a random object: ")
    animal = input("Give me an animal: ")
    action_verb = input("Give me an action verb: ")
    funny_exclamation = input("Give me a funny exclamation: ")


    story = f"""
    Once upon a time, there was a person named {name} who lived in {place}.
    {name} was known for their {funny_adj} sense of humor and loved to carry around a {random_obj}.
    One day, while walking through the park, {name} stumbled upon a {animal} that was {action_verb}ing.
    {name} couldn't help but shout "{funny_exclamation}!" and joined in the fun.
    They spent the whole day laughing and playing with the {animal}, creating memories that would last a lifetime.

    And from that day on, {name} always carried a {random_obj} with them, just in case they met another {animal} who was {action_verb}ing.
    The end!

    
    
    """
    print(story)

if __name__ == "__main__":
    mad_libs()