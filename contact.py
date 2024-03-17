import phone_book_pb2

def contact():
    return phone_book_pb2.Person(
        id = 1,
        name = "Weronika",
        phone_nr = 10
    )

print(contact)