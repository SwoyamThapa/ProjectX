public class test
{
   public static void main(String args[])
   {
      int target = 19;
      int maxDoubles = 2;
      int c=0;
        while(target>1 && maxDoubles>0)
        {
            if(target%2==0)
            {
                maxDoubles-=1;
                target/=2;
                c+=1;
            }
            else
            {
                target-=1;
                c+=1;
            }
        }
        System.out.println(c+(target-1));
   }
}
