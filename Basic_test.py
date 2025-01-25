import re
import urllib.parse
import tkinter as tk

def creatLink(phoneNum, msg):
    #change message to a URL format
    encoded_msg = urllib.parse.quote(msg)
    #use a format for the WhatsApp link
    link = f"https://wa.me/{phoneNum}?text={encoded_msg}"
    return link

def getPhone(inSTR):
    #change the format of the str to a phone as needed for the link
    phone = re.sub(r"\D", "", inSTR)
    if phone.startswith("0"):
        phone = "972" + phone[1:]
    return phone

def main():
    #print("***Welcome to WhatsApp link creator!***\n Please choose one of the following options:\n")
    #print("1. I want to create a link to 1 cell phone with 1 message\n2. I want to create a link to more than 1 cell phone with 1 message\n3. I want to create a link to 1 cell phone with more than 1 message")
    choice = input("Please enter your chocie: ")
    phone = input("Please enter phone num: ")
    message = input("Please type your message: ")
    phone = getPhone(phone)
    link = creatLink(phone, message)
    print("The WhatsApp link is:", link)

main()