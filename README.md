This repository holds the solutions for the Security-1 course’s first mandatory exercise at the IT-University of Copenhagen in March 2021

# ElGamal Encryption:
The ElGamal encryption scheme is based on the Diffie-Hellman key-exchange/key-agreement algorithm, where “the purpose of the algorithm is to enable two users to securely reach agreement about a shared secret that can be used as a secret key for subsequent symmetric encryption of messages.” (Stallings & Brown, 2018).

# Hash Competition:
The file hashed.lst contains 861 hashed passwords and is using SHA224. Hashcat was used together with the RockYou wordlist, which contains 32 million passwords from the 2009 data breach. 677 passwords were cracked and are stored in the kka.txt file. The following commands were used:

hashcat -m 1300 -a 0 hashed.lst rockyou2.txt

hashcat -m 1300 -a 0 hashed.lst rockyou2.txt -r /usr/local/Cellar/hashcat/6.1.1/share/doc/hashcat/rules/best64.rule
