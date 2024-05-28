from pydantic import BaseModel, ConfigDict

class ItemBase(BaseModel):
    title: str
    description: str | None = None # "=" określa wartość domylślną "|" określa lub

class ItemCreate(ItemBase):
    pass #tworzymy ją aby używać przy tworzeniu przedmiotu

class Item(ItemBase): #używana kiedy chcemy wyciągnąc dane z bazy
    model_config = ConfigDict(from_atributes=True)

    id: int
    owner_id: int

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    model_config = ConfigDict(from_atributes=True)

    id: int
    is_active: bool
    items: list[Item] = []

#brak id i owner_id przy tworzeniu
#id wygenerowane będzie automatycznie
#owner_id nie jest wartością tworzoną, definiuje relację
