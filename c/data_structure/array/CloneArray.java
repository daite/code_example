class CloneArray {
    public static void main(String[] args) 
    {
        int[] a = {1, 2, 3, 4, 5};
        int[] b = a.clone();
        b[3] = -1;

        System.out.print("int[]a = ");
        for(int i=0; i<a.length; i++)
        {
            System.out.print(" " + a[i]);
        }
        System.out.print("\nint[]b = ");
        for(int i=0; i<a.length; i++)
        {
            System.out.print(" " + b[i]);
        }
    }
}