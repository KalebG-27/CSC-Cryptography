def main():
        # Hardcoded prime p, a, secret for alice and bob
        p = 0x00fb2e8473c499d184d806e6b5df7f621b
        a = 2
        a_private_key = 0x2ca50afea541f0d90f68e0efc85c2686
        b_private_key = 0x6e146d3b2149f41450713e5c83d21e70
        a_Pub = pow(a, a_private_key, p)
        b_Pub = pow(a, b_private_key, p)
        alice_shared_key = pow(b_Pub, a_private_key, p)
        bob_shared_key = pow(a_Pub, b_private_key, p)
        print("Bit count of p: " + str(p.bit_length()))
        print("Shared Key A: " + hex(alice_shared_key))
        print("Shared Key B: " + hex(bob_shared_key))
main()







