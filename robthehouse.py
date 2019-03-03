__author__ = 'stathis'

def rob(nums):
    if len(nums) == 0:  return 0
    if len(nums) <= 2:  return max(nums)
    max_money = [0] * len(nums)
    max_money[0] = nums[0]
    max_money[1] = max(nums[0], nums[1])
    print(max_money)
    for house in range(2, len(nums)):
        print("nums",nums[house])
        print("max_money[house-1]",max_money[house-1])
        print(" max_money[house-2]+nums", max_money[house-2]+nums[house])
        max_money[house] = max(max_money[house-1], max_money[house-2]+nums[house])
        print("after",max_money[house])
    return max_money[-1]

if __name__ == "__main__":
    H=[[0,10], [1,5], [2,7],
    [3,6],[4,5],[5,2],[6,3],
    [7,5],[8,4],[9,1]]

    H_money = [i[1] for i in H]
    print(H_money)
    print(sorted(H_money))
    print("sum of money robbed from dp:", rob(H_money))
