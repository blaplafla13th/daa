public class De03_20001976 {
    public static void main(String[] args) {
        double[] a = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 };
        int length = a.length;
        System.out.println(max_element(a, length));
    }

    public static int max_element(double[] a, int length) {
        return max_element_2(a, 0, length - 1);
    }

    public static int max_element_2(double[] array, int a, int c){
        if (array.length < 3){
            return -1;
        }
        int b = (a + c)/2;
        if (array[b - 1] < array[b] && array[b] > array[b + 1])
            return b;
        else if (array[b - 1] > array[b] && array[b] > array[b + 1])
            return max_element_2(array, a, b);
        else if (array[b - 1] < array[b] && array[b] < array[b + 1])
            return max_element_2(array, b, c);
        else
            return -1;
    }
}