import pigpio
import time
import threading

#ways to make faster
# make header smaller(small)
# change sleep from .1 to .01 or .05(large)
# change from word to bits back to word back to bits back to word
# gets bits from users then send to broadcast which sends those to users

pi = pigpio.pi()

# should just be like hey nics we are on
pi.write(27,1)

pi.write(25,1)

pi.write(23,1)

pi.write(21,1)

# these need to always be running
def receivePort1():
    data = []
    while True:
        #Port 1
        stri = ""
        rem = pi.read(26)
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
            readPort1()
        time.sleep(0.1)

def receivePort2():
    data = []
    while True:
        #Port 2
        stri = ""
        rem = pi.read(24)
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
            readPort2()
        time.sleep(0.1)

def receivePort3():
    data = []
    while True:
        #Port 3
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
            readPort3()
        time.sleep(0.1)

def receivePort4():
    data = []
    while True:
        #Port 4
        stri = ""
        rem = pi.read(20)
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
            #print("sent to readPort4")
            readPort4()
        time.sleep(0.1)

def readPort1():
    header = ""
    stri = ""
    word = "1 "
    bin = 128
    count = 0
    count2 = 0
    time.sleep(0.1)
    for x in range(8):
        stri += str(pi.read(26))
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
            stri += str(pi.read(26))
            time.sleep(0.1)
        print(stri)
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
    broadcast(word)

def readPort2():
    header = ""
    stri = ""
    word = "2 "
    bin = 128
    count = 0
    count2 = 0
    time.sleep(0.1)
    for x in range(8):
        stri += str(pi.read(24))
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
            stri += str(pi.read(24))
            time.sleep(0.1)
        print(stri)
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
    broadcast(word)

def readPort3():
    header = ""
    stri = ""
    word = "3 "
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
        print(stri)
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
    broadcast(word)

def readPort4():
    header = ""
    stri = ""
    word = "4 "
    bin = 128
    count = 0
    count2 = 0
    time.sleep(0.1)
    for x in range(8):
        stri += str(pi.read(20))
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
            stri += str(pi.read(20))
            time.sleep(0.1)
        print(stri)
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
    #print(word)
    broadcast(word)

    # add a number at beginning to signigy it came from port 4 or user 4

def broadcast(word):
    #rem.append(word)
    #maybe dont need array because there should only be one message at a time
    print(word)

    if(word[0] == '1'):
        print("worked")
        send = word
        length = len(send)
        header = 11010
        for x in str(header):
            pi.write(25,int(x))
            pi.write(23,int(x))
            pi.write(21,int(x))
            time.sleep(0.1)
        length = bin(int(length))
        length = length.replace('0b', '')
        num = 00000000
        length = int(length) ^ num
        length = format(length, '#08')
        for x in length:
            pi.write(25, int(x))
            pi.write(23, int(x))
            pi.write(21, int(x))
            time.sleep(0.1)
        for x in str(send):
            rem = ord(x)
            send = bin(int(rem))
            send = send.replace('0b', '')
            num = 00000000
            send = int(send) ^ num
            send = format(send, '#08')
            print("Send: " + str(send))
            for x in send:
                pi.write(25, int(x))
                pi.write(23, int(x))
                pi.write(21, int(x))
                time.sleep(0.1)

    if(word[0] == '2'):
        send = word
        length = len(send)
        header = 11010
        for x in str(header):
            pi.write(27,int(x))
            pi.write(23,int(x))
            pi.write(21,int(x))
            time.sleep(0.1)
        length = bin(int(length))
        length = length.replace('0b', '')
        num = 00000000
        length = int(length) ^ num
        length = format(length, '#08')
        for x in length:
            pi.write(27, int(x))
            pi.write(23, int(x))
            pi.write(21, int(x))
            time.sleep(0.1)
        for x in str(send):
            rem = ord(x)
            send = bin(int(rem))
            send = send.replace('0b', '')
            num = 00000000
            send = int(send) ^ num
            send = format(send, '#08')
            for x in send:
                pi.write(27, int(x))
                pi.write(23, int(x))
                pi.write(21, int(x))
                time.sleep(0.1)


    if(word[0] == '3'):
        send = word
        length = len(send)
        header = 11010
        for x in str(header):
            pi.write(27,int(x))
            pi.write(25,int(x))
            pi.write(21,int(x))
            time.sleep(0.1)
        length = bin(int(length))
        length = length.replace('0b', '')
        num = 00000000
        length = int(length) ^ num
        length = format(length, '#08')
        for x in length:
            pi.write(27, int(x))
            pi.write(25, int(x))
            pi.write(21, int(x))
            time.sleep(0.1)
        for x in str(send):
            rem = ord(x)
            send = bin(int(rem))
            send = send.replace('0b', '')
            num = 00000000
            send = int(send) ^ num
            send = format(send, '#08')
            for x in send:
                pi.write(27, int(x))
                pi.write(25, int(x))
                pi.write(21, int(x))
                time.sleep(0.1)


    if(word[0] == '4'):
        send = word
       # print(send)
        length = len(send)
        header = 11010
        for x in str(header):
            pi.write(27,int(x))
            pi.write(25,int(x))
            pi.write(23,int(x))
            time.sleep(0.1)
        length = bin(int(length))
        length = length.replace('0b', '')
        num = 00000000
        length = int(length) ^ num
        length = format(length, '#08')
        for x in length:
            pi.write(27, int(x))
            pi.write(25, int(x))
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
                pi.write(27, int(x))
                pi.write(25, int(x))
                pi.write(23, int(x))
                time.sleep(0.1)


if __name__ =="__main__":
    # creating thread
    t1 = threading.Thread(target=receivePort1, args=())
    t2 = threading.Thread(target=receivePort2, args=())
    t3 = threading.Thread(target=receivePort3, args=())
    t4 = threading.Thread(target=receivePort4, args=())

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
    # starting thread 3
    t3.start()
    # starting thread 4
    t4.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
    # wait until thread 3 is completely executed
    t3.join()
    # wait until thread 4 is completely executed
    t4.join()

    # both threads completely executed
    print("Done!")
