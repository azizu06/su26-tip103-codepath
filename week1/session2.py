def two_sum(nums, target):
    l, r = 0, len(nums) - 1
    while True:
        if nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] > target:
            r -= 1
        else:
            return [l, r]


def is_palindrome(s):
    l, r = 0, len(s) - 1
    while l <= r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1
    return True


def most_honey(heights):
    l, r = 0, len(heights) - 1
    res = 0
    while l < r:
        w, h = r - l, min(heights[l], heights[r])
        res = max(res, w * h)
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return res


def merge_intervals(intervals):
    intervals.sort()
    res = []
    i = 0
    while i < len(intervals):
        end = intervals[i][1]
        j = i + 1
        while j < len(intervals) and end >= intervals[j][0]:
            end = max(end, intervals[j][1])
            j += 1
        res.append([intervals[i][0], end])
        i = j
    return res


def insert_interval(intervals, new_interval):
    i = 0
    res = []
    n = len(intervals)
    while i < n and new_interval[0] > intervals[i][1]:
        res.append(intervals[i])
        i += 1
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    res.append(new_interval)
    while i < n:
        res.append(intervals[i])
        i += 1
    return res


def reverse_list(lst):
    l, r = 0, len(lst) - 1
    while l < r:
        lst[l], lst[r] = lst[r], lst[l]
        l, r = l + 1, r - 1
    return lst


def remove_dupes(items):
    if not items:
        return 0
    l = 1
    for r in range(1, len(items)):
        if items[r] != items[r - 1]:
            items[l] = items[r]
            l += 1
    return l


def three_sum(nums):
    nums.sort()
    res = []
    for k in range(len(nums) - 2):
        if k > 0 and nums[k] == nums[k - 1]:
            continue
        i, j = k + 1, len(nums) - 1
        while i < j:
            total = nums[k] + nums[i] + nums[j]
            if total == 0:
                res.append([nums[k], nums[i], nums[j]])
                i, j = i + 1, j - 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
            elif total < 0:
                i += 1
            else:
                j -= 1
    return res


def transpose(matrix):
    R, C = len(matrix), len(matrix[0])
    res = [[0] * R for _ in range(C)]
    for r in range(R):
        for c in range(C):
            res[c][r] = matrix[r][c]
    return res


def add_matrices(matrix1, matrix2):
    rows, cols = len(matrix1), len(matrix1[0])
    res = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            res[r][c] = matrix1[r][c] + matrix2[r][c]
    return res


def squash_spaces(s):
    words = s.split()
    return " ".join(words)


def sort_by_parity(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] % 2 == 0:
            l += 1
        elif nums[r] % 2 == 1:
            r -= 1
        else:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
    return nums
