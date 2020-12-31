class User():
    def __init__(self, **data):
        self.ID = data.get("ID", 0)
        self.USERNAME = data.get("USERNAME", "")
        self.PASSWORD = data.get("PASSWORD", "")
        self.name = data.get("name", "")
        self.mobile = data.get("mobile", "")
        self.is_admin = data.get("is_admin", False)

GABO = User(ID=1,
            USERNAME="lgvaldez", 
            PASSWORD="lgvaldez", 
            name="Gabo",
            mobile=60792029,
            is_admin=True)
DANNY = User(ID=2,
             USERNAME="dannynuzgo",
             PASSWORD="dannynuzgo",
             name="Danny",
             mobile=75115006,
             is_admin=False)
OLIVER = User(ID=3,
              USERNAME="olivertiny",
              PASSWORD="olivertiny",
              name="Oliver")
USER_LIST = [GABO, DANNY, OLIVER]
