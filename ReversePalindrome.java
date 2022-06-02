//Author @brycekickbush
class Solution {
    public boolean isPalindrome(int x) {
        int temp = 0; //Will become reverse of x
        int num = x;
        while(num > 0){ //While number given (ex 25252) is greater than 0
            int lastNum = num % 10; //Gets the digit of the number
            num = num/10; //Divides number by 10 (ex 25252 -> 2525)
            temp = (10 * temp) + lastNum; //Builds new int that is the original, but backwards
        }
        if(temp == x){ //Checks if reversed int matches original int
            return(true);
        }else{
            return(false);
        }
    }
}
