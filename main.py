import ai as aistory
import badwords

running = True

while(running):
    userInput = input(">: ")

    if badwords.checkForBadwords(userInput):
        print("A bad word was detected. Try again...")
        continue

    if userInput.lower() == "quit":
        running = False
    else:
        res = aistory.getNewAIMessage(userInput)
        print(res)


