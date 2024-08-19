# Simple contact list dictionary
contact_list = {
    "Ronish": "1234567890",
    "Donish": "2345678901",
    "Bonish": "3456789012",
    "Tonish": "4567890123"
}

# Function to find a contact by name
def find_contact(name):
    # Attempt to retrieve the contact's phone number from the dictionary
    phone_number = contact_list.get(name)
    
    if phone_number:
        # Return the phone number if found
        return phone_number  
    else:
        # Return a message if the contact does not exist
        return "Contact not found."  

print(find_contact("Ronish"))  
print(find_contact("Bonish"))   
