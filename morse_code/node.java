/*
   Maria Luiza Cartaxo Rocha de Sousa
   - Final Project -
   Building Java Programs: A Back to Basics Approach, 5th edition, chapter 17 (Binary Trees), Programming Projects section #2
   CS 211
*/

// import library
import java.util.*;

// node class
public class node {
   public node left;
   public node right;
   public String letter;
   
   // constructors
   public node(String data) {
      this.letter = "";
      this.left = null;
      this.right = null;
   }
}
