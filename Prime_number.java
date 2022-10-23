import java.util.Scanner;
public class Prime_number {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        //System.out.print("Enter the first number : ");
        //int start = s.nextInt();
        //System.out.print("Enter the second number : ");
        //int end = s.nextInt();
        //System.out.println("List of prime numbers between " + start + " and " + end);
        for (int i = 1; i <= 10; i++) {
            if (isPrime(i)) {
                System.out.println(i);
            }
        }
    }
    public static boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
