from selenium import webdriver
import time

webdriver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
webdriver.get("https://web.whatsapp.com")
time.sleep(10)  # For scan the qr code
# Plese make sure that you have done the qr code scan successful.
while True:
    confirm = int(input("Press 1 to proceed if sucessfully login or press 0 for retry : "))
    if confirm == 1:
        print("Continuing...")
        name = input("type users name or no")
    elif confirm == 0:
        webdriver.close()
        exit()
    else:
        print("Sorry Please Try again")
        webdriver.close()
        exit()

    unread_chats = webdriver.find_elements_by_xpath(f'// span[@title="{name}"]')#_3q9s6#  amit- _3dulN
    # In the above line Change the xpath's class name from the current time class name by inspecting span element
    # which containing the number of unread message showing the contact card inside a green circle before opening the chat room.

    # Open each chat using loop and read message.
    for chat in unread_chats:
        chat.click()
        time.sleep(2)
        # For getting message to perform action
        conv_messages = webdriver.find_elements_by_xpath('//span[@class="i0jNr selectable-text copyable-text"]')
        senders_message = webdriver.find_elements_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[3]/div[11]/div/div/div/div[1]"]')
        # In the above line Change the xpath's class name from the current time class name by inspecting span element
        # which containing received text message of any chat room.
        for i in conv_messages:

            try:
                print(str(i.text))
            except:
                pass
        for i in senders_message:
            print(i)
