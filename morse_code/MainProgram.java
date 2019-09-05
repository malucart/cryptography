/*
   Maria Luiza Cartaxo Rocha de Sousa
   - Final Project -
   Building Java Programs: A Back to Basics Approach, 5th edition, chapter 17 (Binary Trees), Programming Projects section #2
   CS 211
   
   tree.png is from here: https://imgur.com/gallery/qGkz4
*/

// import libraries
import java.util.*;
import java.io.*; // file class

// Main class
public class MainProgram {
   public static void main(String[] args) {
      
      // variables
      boolean stop = false;
      Scanner input = new Scanner(System.in);
      binarytree bt = new binarytree();
      bt.createMorseTree();
      
      while (!stop) { 
      // initialization
      System.out.println();
      System.out.println("          -- Hey! --          ");
      System.out.println(" -- 1 to see morse to alphabet"); 
      System.out.println(" -- 2 to see alphabet to morse");
      System.out.println(" -- 0 to finish the program - ");
      int options = input.nextInt();
      
      // options
      switch (options) {
      
         case 0: 
         
             // finish the program
             System.out.println("Bye-bye!");
             stop = true;
             
             break;
             
         case 1:
         
             // morse to alphabet
             try {
               // necessary code to read the txt file
               BufferedReader morse_file = new BufferedReader(new FileReader("morse.txt"));
               BufferedReader text_file = new BufferedReader(new FileReader("text.txt"));
            
               String morse_code = morse_file.readLine(); // creating string to save the txt
               
               System.out.println("Morse code: " + morse_code); // reading the morse code file
               System.out.println("Morse decode: ");
               bt.decodeMorse(morse_code);  // translation to English
               
               // necessary code to read the txt file (with "try")
               } catch(IOException e) {
                  System.out.println("Exception error: " + e);
                 }

            break;
            
         case 2:
         
            // alphabet to morse
            try {
               // necessary code to read the txt file
               BufferedReader morse_file = new BufferedReader(new FileReader("morse.txt"));
               BufferedReader text_file = new BufferedReader(new FileReader("text.txt"));
               
               String text = text_file.readLine(); // creating string to save the txt

               System.out.println("English to encode: " + text); // reading the English file
               bt.encodeMorse(text); // translation to morse code
               
               // necessary code to read the txt file (with "try")
               } catch(IOException e) {
                  System.out.println("Exception error: " + e);
                 }
            
            break;
             
        } 
      } 
   }
}
