import numpy
import math
import time
#Generating prime numbers

paddingScheme = {34:" ", 35:"A",36:"B",37:"C",38:"D",39:"E",40:"F",41:"G",42:"H",43:"I",44:"J",45:"K",46:"L",
                 47:"M",48:"N",49:"O",50:"P",51:"Q",52:"R",53:"S",54:"T",55:"U",56:"V",57:"W",58:"X",59:"Y",60:"Z",
                 65:"a",76:"b",87:"c",98:"d", 9:"e", 10:"f",21:"g",32:"h",33:"i",11:"j",12:"k",31:"l",14:"m",15:"n",16:"o",17:"p",18:"q",91:"r",20:"s",21:"t",25:"u",26:"v",27:"w",28:"x",29:"y",30:"z"}
encrypted = []
class generate:
    e = 0
    n = 0
    d=0

    def genPrimes(self):
        lower = int(input("Input beginning range: "))
        upper = int(input("Input ending range: "))

        for num in range(lower,upper + 1):
           if num > 1:
               for i in range(2,num):
                   if (num % i) == 0:
                       break
               else:
                   print(num)

    #Getting the n value
    def nValue(self):
        global n,e,d
        prime1 = int(input("Enter First Prime number: "))
        prime2 = int(input("Enter Second Prime number: "))
        n = prime1*prime2
        print("The value of n = "+ str(n))

    #CALCULATING THE VALUE FOR phi(n)

        phi = numpy.lcm((prime1-1),(prime2-1))
        print("Phi(n) = "+str(phi))

    #Taking a number such that 1 < e < phi(n)

        for num in range(phi):
            if (numpy.gcd(num,(phi-1)))==1:
                if num > 70:
                    print(num)
                    if num >=102:
                       break
        e = int(input("Enter Desired Coprime: "))
    #Finding the mod inverse

        for x in range(1, phi):
            if (((float(e) % float(phi)) * (float(x) % float(phi))) % float(phi) == 1):
                print(x)
                d=x
                self.e = e
                break
            else:
                d = "Not found"

        print("Public keys are (n = "+str(n)+" e = "+str(e)+")""\nPrivate keys are (n = "+str(n)+" d = "+str(d)+")")

    #Encrypting text (HELLO WORLD)
    #From our former example, we found out that the padded text for HELLO world, is 4239464649342716913198

    def encryption(self,):
        global encrypted
        print(encrypted)
        textC = [42,39,46,46,49,34,27,16,91,31,98]

        #function for encoding the text
        strin = ""
        for padded in textC:
            pad = padded**e
            t = numpy.mod(pad,n)
            encrypted.append(t)
            strin+=str(t)

        print(encrypted)
        print("The encrypted string is: "+strin)

    def bruteforce(self):
        # print("About to decrypt")
        n = int(input("Enter N value: "))
        num = int(input("Enter e value: "))
        start_time = time.time()
        decrypted = []
        check = []
        sentence = ''
        modB = math.ceil(numpy.sqrt(n))
        print(modB)

        #Using Fermet's Factorization to find the values of p, q
        for i in range(modB,modB+2000):
            global p,q
            val = (i**2) - n
            val1 = numpy.sqrt(val)
            if val1.is_integer() == True:
                p = i + val1
                q = i - val1
                break

        phiVal = numpy.lcm(int(p - 1), int(q - 1))
        print("Phi(n) = " + str(phiVal))

        chek = False
        # for num in range(phiVal):
        #     if (numpy.gcd(num,(phiVal-1)))==1:
        for x in range(1, phiVal):
            if (((float(num) % float(phiVal)) * (float(x) % float(phiVal))) % float(phiVal) == 1):
                got = {"EncryptKey":num,"DecryptKey":x}
                print(x)
                for crypted in encrypted:
                    pad = crypted ** got["DecryptKey"]
                    t = pad % n 
                    if t in paddingScheme.keys():
                        decrypted.append(t)
                        sentence += paddingScheme[t]
                    else:
                        break

            if len(decrypted) == len(encrypted):
                chek = True
                print(decrypted, sentence)
                break

            decrypted.clear()
            check.clear()
            sentence = ""
            if chek == True:
                break




            # for padded in decrypted:
            #     pad = padded**key["EncryptKey"]
            #     t = numpy.mod(pad,n)
            #     check.append(t)
            # if len(sentence)==len(encrypted):
            #     print([decrypted,sentence])
            #     break
        # print(keys)


        # for encrypt in encrypted:
        #     expo = encrypt**d
        #     t = numpy.mod(expo, n)
        #     decrypted.append(t)
        # print("Decrypted code: "+str(decrypted))
        print("time elapsed: {:.2f}s".format(time.time() - start_time))



# for i in range(5):
# generate().genPrimes()
generate().nValue()
generate().encryption()
generate().bruteforce()

