
with open('in.txt') as file:
    lines = file.readlines()
    stripped = map(lambda s: s.strip(), lines)
    non_empty = filter(lambda s: bool(s), stripped)
    nums = list(map(lambda x: int(x), non_empty))
    
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == 2020:
                print(nums[i] * nums[j])

