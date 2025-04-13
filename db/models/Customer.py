class Customer:
    def __init__(self, id, client_name, email, is_banned, client_since):
        self.id = id
        self.client_name = client_name
        self.email = email
        self.is_banned = is_banned
        self.client_since = client_since

    def __str__(self):
        return f"Nome: {self.client_name} | Email: {self.email} | isBanned: {self.is_banned} | Since: {self.client_since})"