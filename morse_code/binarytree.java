/*
   Maria Luiza Cartaxo Rocha de Sousa
   - Final Project -
   Building Java Programs: A Back to Basics Approach, 5th edition, chapter 17 (Binary Trees), Programming Projects section #2
   CS 211
*/

// import library
import java.util.*;

// binary tree class
public class binarytree {
   private node root;
   
   // constructor
   public binarytree() {
      this.root = new node("start");
   }
   
   // morse tree which is the first call in main program
   public void createMorseTree() {
      addMorse("a",".-");
      
      addMorse("b","-...");
      
      addMorse("c","-.-.");
      
      addMorse("d","-..");
      
      addMorse("e",".");
      
      addMorse("f","..-.");
      
      addMorse("g","--.");
      
      addMorse("h","....");
      
      addMorse("i","..");
      
      addMorse("j",".---");
      
      addMorse("k","-.-");
      
      addMorse("l",".-..");
      
      addMorse("m","--");
      
      addMorse("n","-.");
      
      addMorse("o","---");
      
      addMorse("p",".--.");
      
      addMorse("q","--.-");
      
      addMorse("r",".-.");
      
      addMorse("s","...");
      
      addMorse("t","-");
      
      addMorse("u","..-");
      
      addMorse("v","...-");
      
      addMorse("w",".--");
      
      addMorse("x","-..-");
      
      addMorse("y","-.--");
      
      addMorse("z","--..");
      
      addMorse("0","-----");
      
      addMorse("1",".----");
      
      addMorse("2","..---");
      
      addMorse("3","...--");
      
      addMorse("4","....-");
      
      addMorse("5",".....");
      
      addMorse("6","-....");
      
      addMorse("7","--...");
      
      addMorse("8","---..");
      
      addMorse("9","----.");
   }
   
   // necessary method to encode morse 
   public void encodeMorse(String text) {
      String morse = "";

      for (int i = 0; i < text.length(); i++) {
         node aux = root;
         morse = morse + searchBinaryTree(aux, Character.toString(text.charAt(i)), "") + " ";
      }
      
      System.out.println("Encoded String in Morse: " + morse);
   }
   
   // necessary method to decode morse
   public void decodeMorse(String morse) {
      node aux = root;
      
      for (int i = 0; i < morse.length(); i++) {
         // three situations:
         // dash, dot and "space"
         // space means that we will have another character to be printed
         // so we just print the contents and set aux back to root
              
         if (morse.substring(i, i + 1).equals("-")) {
            // we need to create a new node if it isn't already created
            if (aux.right == null) {
               aux.right = new node("");
            }
            
            aux = aux.right;
         } else if (morse.substring(i, i + 1).equals(".")) {
            // we need to create a new node if it isn't already created
            if (aux.left == null) {
               aux.left = new node("");
            }
            
            aux = aux.left;
         } else if (morse.substring(i, i + 1).equals(" ")) {
            System.out.print(aux.letter);
            aux = root;
         } else if (morse.substring(i, i + 1).equals("$")) { // $ means " " (space)
            System.out.print(" ");
         }
      }
      
      System.out.print(aux.letter);
      
      System.out.println("");
   }
   
   private String searchBinaryTree(node aux, String letter, String morse) {
      String result = "";
      
      if (aux.letter.equals(letter)) {
         return morse;
      } else {
         if (aux.right != null) {
            result += searchBinaryTree(aux.right, letter, morse + "-"); // example: if I want letter "m", it will be 
         }                                                              // aux.right = "t", letter = "m", morse = " " + "-" = "-"
                                                                        // it didn't find "m", so again: 
                                                                        // aux.right = "m", letter = "m", morse = "-" + "-" = "--"
         if (aux.left != null) {
            result += searchBinaryTree(aux.left, letter, morse + ".");  // now it's left turn and it does the same thing to find 
         }                                                              // the letter in the left side
      }
      
      return result; 
   }
   
   // method to add morse in the tree
   private void addMorse(String letter, String morse) {
      node aux = root;
      
      for (int i = 0; i < morse.length(); i++) {
         // we will go through the tree creating the necessary nodes until we 
         // arrive the destination for our letter
          
         if (morse.substring(i, i + 1).equals("-")) { // substring() -> start in i, stop in i+1, so I just get one character
            // we need to create a new node if it isn't already created
            if (aux.right == null) {
               aux.right = new node("");
            }
            
            aux = aux.right;
         } else if (morse.substring(i, i + 1).equals(".")) {
            // we need to create a new node if it isn't already created
            if (aux.left == null) {
               aux.left = new node("");
            }
            
            aux = aux.left;
         }
      }
      
      // at this point aux will be at the right node, so we can fill it with the
      // letter
      
      aux.letter = letter;
   }
   
}
