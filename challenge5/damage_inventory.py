class DamageInventorySwitch:
    def __init__(self):
        self.damage_inventory = {
            "REAR END" : 0,
            "FRONT END" : 0,
            "MINOR DENT/SCRATCHES" : 0,
            "UNDERCARRIAGE" : 0,
            "MISC" : 0,

        }

    def get_inventory_from_list(self, damage_type_list):
        for damage_type in damage_type_list:
            # print(damage_type)
            self.switch(damage_type)
        return self.damage_inventory


    def switch(self, damage_type):
        damage_string = str(damage_type).strip()
        if damage_string.upper() in self.damage_inventory.keys():
            self.damage_inventory[damage_string] +=1
        else:
            self.damage_inventory["MISC"] += 1