import json

# 如果以前存储了用户名，就加载它
# 否则，提示用户输入并存储它

filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name?")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("我们会记住你,"+username)
else:
    print("Welcome back,"+username)
