class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        le = 0
        end = len(nums) - 1

        while le < end:
            mid = le + (end - le) // 2
            leftele = mid - le + 1
            rightele = end - mid + 1

            if mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                if rightele % 2 == 1:
                    le = mid + 2
                else:
                    end = mid - 1
            elif mid > 0 and nums[mid] == nums[mid - 1]:
                if leftele % 2 == 1:
                    end = mid - 2
                else:
                    le = mid + 1
            else:
                return nums[mid]

        return nums[le]