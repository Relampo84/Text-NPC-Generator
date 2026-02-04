from classes_file import Npc
from utils import netejar, check_npc_storage, show_npc, check_seed_in_storage, negateId
import time

def start():
    netejar()
    while True:
        netejar()
        choice = input("""\
                       
What do you want to do?
    1. Generate a new NPC
    2. Call an already existing NPC  
    3. Exit the program                 

        > """
        )
        match choice:
            case "1":
                bot = Npc()
                try:
                    save = input("Do you want to save this npc (y/n)? ")
                    if save == "y":
                        bot.saveCsvNpc()
                        time.sleep(1)
                    else:
                        negateId()
                        time.sleep(1)
                except KeyboardInterrupt:
                    negateId()
                    time.sleep(1)
            case "2":
                try:
                    seed = input("Type the seed of the npc: ")
                    if check_seed_in_storage(seed):
                        name, middle_name, gender, age, id, seed = check_npc_storage(seed)
                        show_npc(name, middle_name, gender, age, id, seed)
                    else:
                        print("This npc doesn't exist.")
                except Exception:
                    print("Invalid seed")
                time.sleep(4)
            case "3":
                print("Exiting . . .")
                break
            case _:
                print("Invalid choice")
                time.sleep(2)