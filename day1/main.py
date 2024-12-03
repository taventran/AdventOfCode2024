if __name__ == "__main__":
    # Part 1 Dist
    f = open("input.txt")
    nums1 = []
    nums2 = []
    for line in f.readlines():
        if line == "\n":
            continue
        temp = line.split("   ")
        nums1.append(int(temp[0]))
        nums2.append(int(temp[1][0:-1]))

    nums1.sort()
    nums2.sort()

    dist = []

    for i in range(len(nums1)):
        dist.append(abs(nums1[i] - nums2[i]))

    print(f" total distance: {sum(dist)}")

    # Part 2 Similarity Score
    map = {}

    for num in nums2:
        if num not in map:
            map[num] = 1
            continue
        map[num] += 1
    sim_scores = 0
    for num in nums1:
        if num not in map:
            continue
        sim_scores = sim_scores + num * map[num]

    print(f"similarity score: {sim_scores}")
