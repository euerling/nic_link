import pigpio
import time
import threading

pi = pigpio.pi()

pi.write(23,1)

# need to figure out how to be reading for a message and be able to send message at the same time

data = []

def receive():
    header = ""
    stri = ""
    word = ""
    bin = 128
    count = 0
    count2 = 0
    time.sleep(0.1)
    for x in range(8):
        stri += str(pi.read(22))
        time.sleep(0.1)
    for x in stri:
        if(int(x) == 1):
            count += bin
            bin = bin / 2
        else:
            bin = bin / 2
    stri = ""
    bin = 128
    for x in range(int(count)):
        for y in range(8):
            stri += str(pi.read(22))
            time.sleep(0.1)
        for x in stri:
            if(int(x) == 1):
                count2 += bin
                bin = bin / 2
            else:
                bin = bin / 2
        word += chr(int(count2))
        stri = ""
        count2 = 0
        bin = 128
    print()
    print(word)
    print()

def user_send():
    while True:
        #dont know if this will work cause its reading from server pi so the gpio pin might not be on
        #i can turn on all 4 gpio pins and maybe check
        if(pi.read(22) == 1):
            send = input("")
            print()
            length = len(send)
            header = 11010
            for x in str(header):
                pi.write(23,int(x))
                time.sleep(0.1)
            length = bin(int(length))
            length = length.replace('0b', '')
            num = 00000000
            length = int(length) ^ num
            length = format(length, '#08')
            for x in length:
                pi.write(23, int(x))
                time.sleep(0.1)
            for x in str(send):
                rem = ord(x)
                send = bin(int(rem))
                send = send.replace('0b', '')
                num = 00000000
                send = int(send) ^ num
                send = format(send, '#08')
                for x in send:
                    pi.write(23, int(x))
                    time.sleep(0.1)

def user_receive():
    while True:
        stri = ""
        rem = pi.read(22)
        data.append(rem)
        if(len(data) == 5):
            for x in data:
                stri += str(x)
        elif(len(data) > 5):
            data.pop(0)
            for x in data:
                stri += str(x)
        #print(stri)
        if(stri == "11010"):
            receive()
        time.sleep(0.1)


if __name__ =="__main__":
    # creating thread
    t1 = threading.Thread(target=user_receive, args=())
    t2 = threading.Thread(target=user_send, args=())

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    print("Done!")
