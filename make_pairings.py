import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# initialize Firebase Admin SDK
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)

# create Firestore client
db = firestore.client()


def get_emails():
    # retrieve all documents from the collection
    docs = db.collection("users").get()

    # loop through each document and get the value of the field
    email_dict = {}
    for doc in docs:
        doc_data = doc.to_dict()
        email = doc_data.get("email")
        name = doc_data.get("name")
        if email and name:
            email_dict[email] = name

    return email_dict

    
def make_pairings(emails_and_names):
    
    # Step 1
    email_dict = dict(emails_and_names)
    
    # Step 2
    people_list = list(email_dict.items())
    
    # Step 3
    odd_person = ""
    if len(people_list) % 2 != 0:
        odd_person = people_list.pop()
    
    # Step 4
    list1, list2 = [], []
    while people_list:
        list1.append(people_list.pop(0))
        if people_list:
            list2.append(people_list.pop(0))
    
    # Step 5
    if odd_person:
        list1.append(odd_person)
    
    # Step 6
    paired_people = []
    for person1, person2 in zip(list1, list2 + [list1[0]]):
        paired_people.append((person1[0], person1[1], person2[0], person2[1]))
    
    return paired_people








