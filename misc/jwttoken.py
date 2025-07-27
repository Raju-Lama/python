payload = jwt.decode(token, self.secret, algorithms="HS256")

username = payload['username']
flag = self.db_lookup(username, "flag")