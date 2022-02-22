import requests
import telegram_send
ACCESS_TOKEN = "e29aa33a40497aad8fbf83a3acce299123568d78"
projects:list = requests.get(
    "https://api.todoist.com/rest/v1/projects",
    headers={
        "Authorization": "Bearer %s" % ACCESS_TOKEN
    }).json()




mess = "Tasks for Today\n\n"
for p in projects:
    mess+=f"__*{p['name']}*__\n"
    tasks:list = requests.get(
        "https://api.todoist.com/rest/v1/tasks",
        params={"project_id": p['id']},
        headers={
            "Authorization": "Bearer %s" % ACCESS_TOKEN
        }).json()
    for task in tasks:
        mess+= "- " + task['content'] + "\n"
    mess+="\n"
telegram_send.send(messages=[mess], parse_mode="markdown")
