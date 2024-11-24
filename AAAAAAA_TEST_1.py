nums1 = [3, 2, 1, 0, 4]


    def canJump(nums : int):
        zero_index = []
        for index in range(len(nums)):
            if nums[index] == 0:
                zero_index.append(index)
        print(zero_index)
        test1 = 0
        for element in zero_index:
            test2 = 0
            for takenvalue in range(1, element+1):
                if nums[element-takenvalue] == takenvalue:
                    continue
                elif nums[element-takenvalue] > takenvalue:
                    test2 += 1
            if test2 > 0:
                test1 += 1
            else:
                continue
        if test1 == len(zero_index):
            return True
        else:
            return False








print(canJump(nums1))
