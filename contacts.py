# Name: Lam Doan
# # Date: 10/17/2024
# File Purpose: Lab07 contact module program

import json
class Contacts:
    def __init__(self, *, filename):
        self.filename = filename
        self.dic = {}
        try:
            with open(filename) as f:
                self.dic = json.load(f)
        except FileNotFoundError as e:
            print(e)
    
    def add_contact(self, *, id, first_name, last_name):
        if id in self.dic.keys():
            return "error"
        else:
            self.dic[id] = [first_name, last_name]
            sorted_contacts = dict(sorted(self.dic.items(), key = lambda contact : (contact[1][1].lower(), contact[1][0].lower())))
            with open(self.filename, "w") as f:
                json.dump(sorted_contacts, f)
            return {id : [first_name, last_name]}
    
    def modify_contact(self, *, id, first_name, last_name):
        if id not in self.dic.keys():
            return "error"
        else:
            self.dic[id] = [first_name, last_name]
            sorted_contacts = dict(sorted(self.dic.items(), key = lambda contact : (contact[1][1].lower(), contact[1][0].lower())))
            with open(self.filename, "w") as f:
                json.dump(sorted_contacts, f)
            return {id : [first_name, last_name]}
    
    def delete_contact(self, *, id):
        if id not in self.dic.keys():
            return "error"
        else:
            name = self.dic[id]
            del self.dic[id]
            with open(self.filename, "w") as f:
                json.dump(self.dic, f)
            return name
    
    def print_contact(self):
        sorted_contacts = dict(sorted(self.dic.items(), key = lambda contact : (contact[1][1].lower(), contact[1][0].lower())))
        print("     ================== CONTACT LIST(S) ==================")
        print("     Last Name             First Name            Phone")
        print("     ====================  ====================  ==========")
        for contact in sorted_contacts.items():
            print(f'     {contact[1][1]:22}{contact[1][0]:22}{contact[0]:8}')
        print()

        
    



