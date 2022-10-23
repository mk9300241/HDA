//Take three numbers from the user and print the greatest number

import java.util.Scanner;

public class Greatest_number {
    public static void main(String[] args){
        int a,b,c;
        Scanner scanner = new Scanner(System.in);
        a = scanner.nextInt();
        b = scanner.nextInt();
        c = scanner.nextInt();
        scanner.close();
        if (a>b && a>c) System.out.println(a);
        else if (b>c && b>a) System.out.println(b);
        else System.out.println(c);
    }
}
