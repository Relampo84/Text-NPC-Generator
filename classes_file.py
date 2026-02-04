from utils import generate_attributes
import csv

class Npc():
    def __init__(self):
        self.first_name, self.middle_name, self.gender, self.age,self.id, self.seed = generate_attributes() 
        self.show_attributes()

    def show_attributes(self):
        print(f"""\
            Name = {self.first_name} {self.middle_name}
            Gender = {self.gender}
            Age = {self.age}
            ID = {self.seed}""")
    
    def saveCsvNpc(self):
        fields = ['seed']
        new_row = {'seed':self.seed}
        with open('npc_storage.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writerow(new_row)
