import phone_book_pb2

def contact(num, imie, numer):
    return phone_book_pb2.Person(
        id = num,
        name = imie,
        phone_nr = numer

    )

imiona = ['Weronika', 'Jakub', 'Poldek', 'Iwona', 'Jarek', 'Zoja']
numery = [101, 102, 103, 104, 105, 106]
indexy = []
index = 0
for imie in imiona:
    index += 1
    indexy.append(index)
phone_book = []
for item in range(len(indexy)):
    osoba = contact(indexy[item], imiona[item], numery[item])
    phone_book.append(osoba)
    
print(phone_book)