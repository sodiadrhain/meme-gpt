from db.user import add_user

class TelegramUser:
    def __init__(self, first_name: str, last_name: str, username: str, id: int):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.id = id

    def create(self) -> bool:
        add_user(self.first_name, "self.last_name")
        print(self.id)

