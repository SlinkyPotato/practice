// Test HashSet

import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class HashTest {
    public static void main(String[] args) {
       /* // Create a HashSet
        Set<String> set = new HashSet<>();
        System.out.println("cmd change test");
        set.add("Brian");
        set.add("Astrid");
        set.add("Daniel");
        set.add("Alex");
        set.add("Mama");
        set.add("Papa");
        set.add("Papa");
        System.out.println(set);*/

        Result result = JUnitCore.runClasses(test.class);
        for (Failure failure : result.getFailures()) {
           System.out.println(failure.toString());
        }
        System.out.println(result.wasSuccessful());
    }
}