from selenium import webdriver

class alt_tag_inventory:
    def __init__(self):
        self.inventory = {}
        print("Initializing alt_tag_inventory.")

    def inventory_element_list(self, element_list):
        for element in element_list:
            alt_tag = element.get_attribute("alt")
            tag_name = element.tag_name

            has_alt = False

            if alt_tag == None:
                has_alt = False
            elif alt_tag == "":
                has_alt = False
            else:
                has_alt = True
                # print(str(tag_name) +': ' + str(alt_tag))

            self._update_inventory(tag_name, has_alt)

    def _update_inventory(self, tag_name, has_tag):

        if tag_name in self.inventory.keys():
            if has_tag:
                self.inventory[tag_name]["with_alt"] +=1
            else:
                self.inventory[tag_name]["without_alt"] +=1
        else:
            self.inventory[tag_name] = {}

            if has_tag:
                self.inventory[tag_name]["with_alt"] = 1
                self.inventory[tag_name]["without_alt"] = 0
            else:
                self.inventory[tag_name]["with_alt"] = 0
                self.inventory[tag_name]["without_alt"] = 1

    def get_full_tag_inventory(self):
        return self.inventory

    def get_inventory_for_tag_name(self, tag_name):
        return self.inventory[tag_name]

    def get_tag_name_without_alt(self, tag_name):
        return self.inventory[tag_name]["without_alt"]

    def get_tag_name_with_alt(self, tag_name):
        return self.inventory[tag_name]["with_alt"]



