from contact import Contact
from contact_list import Contact_List

def main():
    contact_list = Contact_List()

    contact_list.add_contact(Contact("John Brown", "brown@onet.pl", "555234000"))
    contact_list.add_contact(Contact("Anna May", "am@o2.pl", "232000199"))
    contact_list.add_contact(Contact("George Small", "smallg@google.pl", "222999100"))
    contact_list.add_contact(Contact("Paola Big", "bigpaola@poczta.pl", "100200300"))

    print("Contact List:")
    contact_list.display_contacts()

if __name__ == "__main__":
    main()
