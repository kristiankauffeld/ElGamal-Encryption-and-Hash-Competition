def modInverse(a, m) :
    a = a % m;
    for x in range(1, m) :
        if ((a * x) % m == 1) :
            return x
    return 1

g = 666
p = 6661
PK_bob = 2227


#Assignment (a):
print("Assignment part 1:")

m = 2000
y = 5
PK_alice = pow(g, y, p)


shared_secret_key = pow(PK_bob, y, p) #Alice's calculation of the shared_secret_key

c = (shared_secret_key * m) % p #encryption of the message into ciphertext

print("Sending g^y:", PK_alice, "and c:", c)

gxy_1 = modInverse(shared_secret_key,p)
message_reconstructed = (c * gxy_1) %p
print("Bob recovers the secret =",message_reconstructed) #bob decrypts the message
print("")
print("-------------")
print("")

#Assignment (b):
print("Assignment part 2")
for i in range(1,6662):
    if(pow(g,i,p) == PK_bob):
        x = i
        print("Haha! I found bobs private key, it is x =",i)
        break

#Eve can calculate g^xy since g^y is given from alice
eve_gxy = pow(PK_alice,x,p)
#again get multiplicative inverse
eve_gxy_1 = modInverse(eve_gxy,p)
message_intercepted = (c*eve_gxy_1)%p
print("I found Alice's message =",message_intercepted)
print("")
print("-------------")
print("")


#Assignment (c):
print("Assignment part 3")
print("I am mallory!, I see the ciphertext and will multiply it to make the number seem bigger!")
c = c*2 #We intercept just the ciphertext and multiply this by 2 to get 4000.
gxy_1 = modInverse(shared_secret_key,p)
message_reconstructed = (c * gxy_1) %p
print("Bob recovers the secret",message_reconstructed)
print("")
print("-------------")


