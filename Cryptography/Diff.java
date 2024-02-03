import java.math.BigInteger;

public class Diff {
    public static void main(String[] args) {
        BigInteger p = new BigInteger("00fb2e8473c499d184d806e6b5df7f621b",16);
        BigInteger a = new BigInteger("2");
        BigInteger a_PrivKey = new BigInteger("2ca50afea541f0d90f68e0efc85c2686",16);
        BigInteger b_PrivKey = new BigInteger("6e146d3b2149f41450713e5c83d21e70",16);

        // Alice computes g^a mod p to send to Bob
        BigInteger a_PubKey = new BigInteger(a.modPow(a_PrivKey, p).toString());

        // Bob computes g^a mod p to send to Alice
        BigInteger b_PubKey = new BigInteger(a.modPow(b_PrivKey, p).toString());;

        // Alice computes shared from Bob
        BigInteger a_sharedKey = new BigInteger(b_PubKey.modPow(a_PrivKey, p).toString());

        // Bob computes shared from Alice
        BigInteger b_sharedKey = new BigInteger(a_PubKey.modPow(b_PrivKey, p).toString());

        System.out.println("Bit count of prime p: " + p.bitLength());

        System.out.println("Shared key A : " + a_sharedKey.toString(16));
        System.out.println("Shared key B : " + b_sharedKey.toString(16));
    }
}