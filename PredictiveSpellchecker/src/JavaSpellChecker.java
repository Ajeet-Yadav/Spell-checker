
import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import javax.swing.JOptionPane;

class JavaSpellChecker extends GUI1  {

    private static final File DICTIONARY_WORDS = new File("c:\\hello.txt");

    boolean checkSpelling(String input)      // function defination called from PSVM()
            throws IOException {
        Set<String> words = readDictionary();     // calling another function for reading with variable words Declaration diamond <>
        for (String word : input.toLowerCase().split(" ")) {
            if (!words.contains(word)) {
                //System.out.println(word + " is not in the dictionary");
                // JOptionPane.showMessageDialog(this," is not in the dictionary");
                //  pre(input);
                return false;
            }
        }
          
        return true;
    }

    private Set<String> readDictionary()     // function defination called from checkspell()
            throws IOException {
        Set<String> words = new HashSet<>();  // ArrayList supports dynamic arrays that can grow as needed
                 
                 words.add("ajeet");  //  word hello added into dictionary manually in initialze stage
                 words.add("c:\\hello.txt");  // text file hello.txt added to words
        InputStream stream = new FileInputStream(DICTIONARY_WORDS);
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(stream, "UTF-8")); // unicode for exception handling
            String word;
           
            while ((word = reader.readLine()) != null) { // if its not dictionary word
                words.add(word);
            }
        } finally  {
            stream.close();
        }
        return words;
    } 
}