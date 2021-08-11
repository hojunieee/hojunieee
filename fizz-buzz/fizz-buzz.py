class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        nums = list()
        for i in range(1,n+1):
            nums.append(str(i))
        
        for i in range(len(nums)):
            if int(nums[i])%3 ==0 and int(nums[i])%5==0:
                nums[i] = "FizzBuzz"
            elif int(nums[i])%3 ==0:
                nums[i] = "Fizz"
            elif int(nums[i])%5==0:
                nums[i] = "Buzz"
        return nums