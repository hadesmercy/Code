import java.sql.Date;
import java.time.*;


class t{
    public static int a = 0;
}


public class test {
    public static void main(String[] args) {
        int x = new Integer("10");
        LocalDate h = LocalDate.now();
        int i = h.getDayOfMonth();
        System.out.println(h.hashCode());
        System.out.println(h.plusDays(20).hashCode());
        System.out.println(h.hashCode());
        final String q = new String("hEe");
        System.out.println(q.hashCode());
        System.out.println(q);
        q.toLowerCase();
        System.out.println(q);
        System.out.println(q.hashCode());
        t here = new t();
        t there = new t();
        System.out.println(here.a);
        here.a++;
        System.out.println(there.a);

    }
}