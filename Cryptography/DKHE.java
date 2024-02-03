import java.math.BigInteger;

public class DKHE {
    public static void main(String[] args){
        BigInteger p = new BigInteger("00fb2e8473c499d184d806e6b5df7f621b",16);
        BigInteger a = new BigInteger("2");
        BigInteger a_kpriv = new BigInteger("2ca50afea541f0d90f68e0efc85c2686",16);    
        BigInteger b_kpriv = new BigInteger("6e146d3b2149f41450713e5c83d21e70",16);
        BigInteger a_kpub = new BigInteger(a.modPow(a_kpriv,p).toString());
        BigInteger b_kpub = new BigInteger(a.modPow(b_kpriv,p).toString());
        BigInteger a_kmix = new BigInteger(b_kpub.modPow(a_kpriv,p).toString());
        BigInteger b_kmix = new BigInteger(a_kpub.modPow(b_kpriv,p).toString());
        System.out.println("Bit count of p: " + p.bitLength());
        System.out.println("Shared key A : " + a_kmix.toString(16));
        System.out.println("Shared key B : " + b_kmix.toString(16));
    }
}	
