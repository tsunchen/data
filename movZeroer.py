import sys


def movZeroers(nums):
	zeros = 0
	for i in range(len(nums)):
		nums[i - zeros] = nums[i]
		if nums[i] == '0':
			zeros += 1
	for i in range(zeros):
		nums[len(nums) - i - 1] = 0


if __name__ == '__main__':
    nums = ['0','fa0/1','0','fa0/3','fa0/12','0']
    movZeroers(nums)
    print (nums)
