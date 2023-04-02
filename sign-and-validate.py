from ecdsa import SigningKey, SECP256k1

sk= SigningKey.generate(curve=SECP256k1)
print(sk)
print("\n")

vk = sk.verifying_key

print(vk)
print("\n")

signature = sk.sign(b"Not your keys, not your crypto lmao get rekt")

print("\n")
print(signature)

assert vk.verify(signature, b"Not your keys, not your crypto lmao get rekt")
print("chal gaya lmao")