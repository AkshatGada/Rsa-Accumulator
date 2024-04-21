# # This file is used to generate a proof for the RSAAccumulator smart contract
# import sys
# import secrets
# from main import setup, add, prove_membership, verify_membership
# from helpfunctions import hash_to_prime


# def to_padded_num_str(num, length_in_bytes):
#     length_in_hex_str = length_in_bytes * 2 + 2
#     num_str = format(num, '#0' + str(length_in_hex_str) + 'x')
#     return num_str


# n, A0, S = setup()

# print("n",n)
# print("A0",A0)
# print("S",S)

# x_values = [secrets.randbelow(pow(2,256)) for _ in range(2)]

# for x in x_values: 
#   print("x",x)
#   A1 = add(A0, S, x, n)
#   print("A1",A1)
#   nonce = S[x]
#   proof = prove_membership(A0, S, x, n)
#   print("proof",proof)
#   #prime, nonce = hash_to_prime(x=x, nonce=nonce)
#   result = verify_membership(A1,x,nonce,proof,n)
#   print("result",result)



# print(to_padded_num_str(n, 384) )
# print(to_padded_num_str(proof, 384)) 
# print(to_padded_num_str(prime, 32) )
# print(to_padded_num_str(A1, 384))
# sys.stdout.flush()






import sys
import secrets
from main import setup, add, prove_membership, verify_membership , batch_add , create_all_membership_witnesses
from helpfunctions import hash_to_prime


def to_padded_num_str(num, length_in_bytes):
    length_in_hex_str = length_in_bytes * 2 + 2
    num_str = format(num, '#0' + str(length_in_hex_str) + 'x')
    return num_str


n, A0, S = setup()

print("n",n)
print("A0",A0)
print("S",S)

x_values = [secrets.randbelow(pow(2, 256)) for _ in range(1000)]
A1_values = []

print(x_values)
print(S)
A1 = batch_add(A0,S,x_values,n)
print("A1",A1)
print(S)
witness = create_all_membership_witnesses(A0,S,n)
print(witness)

for i in range(1000) : 
 nonce = S[x_values[i]]
 result = verify_membership(A1,x_values[i],nonce,witness[i],n)
 print(result)


# for x in x_values: 
#     print("x", x)
#     A1 = add(A0, S, x, n)
#     A1_values.append(A1)  # Append the computed A1 value to the list
#     print("A1", A1)
#     nonce = S[x]
#     proof = prove_membership(A0, S, x, n)
#     print("proof", proof)
#     prime, nonce = hash_to_prime(x=x, nonce=nonce)
#     result = verify_membership(A1, x, nonce, proof, n)
#     print("result", result)
#     print(S)

# Now A1_values is a list containing all the computed A1 values
# print("A1 values:", A1_values)












