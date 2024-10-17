# Implement swiping function (later on)
    # Create mechanism to swipe through each elements in list - aka all cats
    # If swipe right, add cat to new list
    # After go through every cat in list, new list pops up of all cats w contact info & images
# Implement object class (fields of cat name, cat breed, pic of cat, descrip, phone #, address)
# All cat objects in a list
# Swipe using 0 and 1 (for each loop reading through all of it)
    # 0 means left (no) - moves on to next cat
    # 1 means right (yes) - breaks loop and focuses in on selected cat. Then can print
    # "Success! Enter your email: "
    # Then after email is inputted (could check for correct email - like assignment we just did),
    # a message says "The shelter will be in contact with you soon."

import ibm_watsonx_ai

class Cat:
    def __init__(self, name, breed, description, phoneNumber, address):
        self.name = name
        self.breed = breed
        self.description = description
        self.phoneNumber = phoneNumber
        self.address = address
    
    def get_name(self):
        return self.name
    
    def get_breed(self):
        return self.breed
    
    def get_description(self):
        return self.description
    
    def get_phoneNumber(self):
        return self.phoneNumber
    
    def get_address(self):
        return self.address

def main():
    whiskers = Cat("Whiskers", "Siamese", "This is a super sweet kitten.", 8032359692, "Charlotte, NC")
    goldie = Cat("Goldie", "Pyranese", "This little boy was found behind a gas station.", 84650217649, "Columbia, SC")
    maxine = Cat("Maxine", "Tabby", "This sweet girl is blind, but she makes up for it with enthusiasm.", 5383586621, "Greenville, SC")
    daisy = Cat("Daisy", "Sphynx", "This little girl was abandoned by her family.", 4842940274, "Charleston, SC")
    jasper = Cat("Jasper", "Ragdoll", "These kind kitten has a sweet demeanor and loves naps.", 9385730569, "Travelers Rest, SC")
    
    allCats = [whiskers, goldie, maxine, daisy, jasper]
    wantedCats = []

    for cat in allCats:
        print("Name: " + str(cat.get_name()))
        print("Breed: " + str(cat.get_breed()))
        print("Description: " + str(cat.get_description()))
        print("Phone Number: " + str(cat.get_phoneNumber()))
        print("Address: " + str(cat.get_address()))
        print("-------------------------------")

        choice = input("Swipe left or right on " + cat.get_name() + ": ")
        choice = choice.lower()

        if choice == "right":
            wantedCats.append(cat)
    
    print("Here are your selected cats!")
    for cat in wantedCats:
        print("Name: " + cat.get_name())
        print("Phone number: " + str(cat.get_phoneNumber()))
    input("Enter your email: ")
    print("Success! The shelter(s) will be in contact with you soon.")
    
if __name__ == '__main__':
    main()






