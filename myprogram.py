PASSWORD1 = "rajesh"

def get_password():
    while True:
        password = input("Enter password: ")
        if password == PASSWORD1:
            return True
        else:
            print("Incorrect password. Please try again.")

def main():
    if get_password():
        print("Access granted. Welcome to the program!")
        # Program's main functionality goes here
    else:
        print("Access denied. Exiting program.")

if __name__ == "__main__":
    main()



print("@# welcome to max chat #@")

print("          1.registration of user")
print("          2.user's informations")
print("          3.work with max chat vertual")
print("          4.work with max chat bot")
print("          5.about the program information")
print("          6.contact list")

choice=int(input("enter the number you want :"))

def a():
    print("welcome to max chat @@new world of ai@@")
    USERID=input("enter the user id:")
    USERNAME=input("enter the user name :")
    EMAIL=input("enter the user email-id:")
    PASSWORD=input("enter the user password:")

    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='123456',database='rajesh')
    query="insert into user(USERID,USERNAME,EMAIL,PASSWORD) values({},'{}','{}','{}')"\
        .format(USERID,USERNAME,EMAIL,PASSWORD)
    mycursor=mydb.cursor()
    mycursor.execute(query)
    mydb.commit()

def b():
    import mysql.connector
    import pandas as pd
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='123456',database='rajesh')
    mycursor=mydb.cursor()
    mycursor.execute("select * from user")
    myrecords=mycursor.fetchall()
    print(myrecords)
    df=pd.DataFrame(myrecords,columns=[USERID , USERNAME, EMAIL, PASSWORD])
    print(df)

def c():
    import speech_recognition as sr
    import pyttsx3
    import openai

    openai.api_key = "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"

    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voices", voices[1].id)

    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)

    conversation = ""
    user_name = "dan"
    bot_name = "john"

    while True:
        with mic as source:
            print("\n listening...")
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
        print("no longer listening")

        try:
            user_input = r.recognize_google(audio)
        except:
            continue

        prompt = user_name + ":" + user_input + "\n" + bot_name + ":"
        conversation += prompt

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=conversation,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        response_str = response["choices"][0]["text"].replace("\n", "")
        response_str = response_str.split(
            user_name + ":", 1)[0].split(bot_name + ":", 1)[0]

        conversation += response_str + "\n"
        print(response_str)

        engine.say(response_str)
        engine.runAndWait()

def d():
    import os
    import openai

    openai.api_key = "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"

    conversation = input("enter the question :")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response['choices'][0]['text'])


def e():
    print("hey, All is here that you see is a new word Ai technology which is best and Worldwide ")
    print("we are a joint group of three people who are in imca department ")
    print("so, our project made by open ai api ")
    print("world wide this technology is one of most beautiful ")

def f():
    print("if any requirement please call or email us")
    print("toll-free-no: 7069433889,2233990844")
    print("email:maxchat.ac.in")

if choice==1:
    a()
elif choice==2:
    b()
elif choice==3:
    c()
elif choice==4:
    d()
elif choice==5:
    e()
elif choice==6:
    f()
else:
    print("*******    you entered a wrong no    ********")
