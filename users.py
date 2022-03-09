from mysqlconnection import connectToMySQL


class User:

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def muestraUsuarios(cls):
        query = "SELECT * FROM usuarios_cr.usuarios;"
        results = connectToMySQL("usuarios_cr").query_db(query)
        users = []
        for u in results:
            users.append(cls(u))
        return users

    @classmethod
    def guardar(cls,data):

        query= "INSERT INTO usuarios_cr.usuarios (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s)"
        result = connectToMySQL("usuarios_cr").query_db(query,data)
        return result