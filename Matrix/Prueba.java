//@{}[]|\&<>
import java.io.*;

public class Prueba{
	public static void main(String args[]){
		try{
			InputStreamReader isr=new InputStreamReader(System.in);
			BufferedReader br=new BufferedReader(isr);
			System.out.println("Hola mundo");
			String op=br.readLine();
			System.out.println(op);
		} catch(IOException e) {
			System.out.println("IOException");
		}
	}
}
