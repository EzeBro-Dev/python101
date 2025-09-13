def check_login(username, password):
    users = { "joshua": "1234", "dayo": "abcd"}
    if username in users and users[username] == password:
        return { "status": "success", "message": f"welcome {username}!" }
    return { "status": "error", "message": "invalid username or password." }

print(check_login("dayo", "abcd"))