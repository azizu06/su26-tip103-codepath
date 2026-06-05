def local_maximus(grid):
    n = len(grid)
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    res = [[0] * (n - 2) for _ in range(n - 2)]
    for r in range(n - 2):
        for c in range(n - 2):
            best = grid[r + 1][c + 1]
            for dr, dc in dirs:
                best = max(best, grid[(r + 1 + dr)][(c + 1 + dc)])
            res[r][c] = best
    return res


def defuse(code, k):
    n = len(code)
    res = [0] * n
    if k == 0:
        return res
    for i in range(len(code)):
        total = 0
        if k > 0:
            for j in range(1, k + 1):
                total += code[(i + j) % n]
        else:
            for j in range(1, abs(k) + 1):
                total += code[(i - j) % n]
        res[i] = total
    return res


def non_decreasing(nums):
    limit = 0
    for i in range(len(nums) - 1):
        if nums[i] <= nums[i + 1]:
            continue
        limit += 1
        if limit > 1:
            return False
        if i == 0 or nums[i - 1] <= nums[i + 1]:
            nums[i] = nums[i + 1]
        else:
            nums[i + 1] = nums[i]
    return True


def linear_search(items, target):
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1


def final_value_after_operations(operations):
    res = 1
    for o in operations:
        if o in ("bouncy", "flouncy"):
            res += 1
        else:
            res -= 1
    return res


def tiggerfy(word):
    banned = ["t", "i", "gg", "er"]
    word = word.lower()
    for b in banned:
        word = word.replace(b, "")
    return word


def find_missing_clues(clues, lower, upper):
    if not clues:
        return [[lower, upper]]
    clues.sort()
    res = []
    if lower < clues[0]:
        res.append([lower, clues[0] - 1])
    for i in range(len(clues) - 1):
        if clues[i + 1] - clues[i] == 1:
            continue
        res.append([clues[i] + 1, clues[i + 1] - 1])
    if upper > clues[-1]:
        res.append([clues[-1] + 1, upper])
    return res


def harvest(vegetable_patch):
    res = 0
    for r in range(len(vegetable_patch)):
        for c in range(len(vegetable_patch[0])):
            if vegetable_patch[r][c] == "c":
                res += 1
    return res


def good_pairs(pile1, pile2, k):
    res = 0
    for p1 in pile1:
        for p2 in pile2:
            res += 1 if p1 % (p2 * k) == 0 else 0
    return res


def words_with_char(words, x):
    res = []
    for i, w in enumerate(words):
        if x in w:
            res.append(i)
    return res


def hulk_smash(n):
    answer = []
    for i in range(1, n + 1):
        if not i % 15:
            answer.append("HulkSmash")
        elif not i % 3:
            answer.append("Hulk")
        elif not i % 5:
            answer.append("Smash")
        else:
            answer.append(str(i))
    return answer


def shuffle(message, indices):
    res = [""] * len(message)
    for i, m in enumerate(message):
        res[indices[i]] = m
    return "".join(res)


def minimum_boxes(meals, capacity):
    capacity.sort(reverse=True)
    total = sum(meals)
    i = 0
    while total > 0:
        total -= capacity[i]
        i += 1
    return i


def wealthiest_customer(accounts):
    c = w = 0
    for i in range(len(accounts)):
        total = 0
        for j in range(len(accounts[0])):
            total += accounts[i][j]
        if total > w:
            w = total
            c = i
    return [c, w]


def smaller_than_current(nums):
    res = [0] * len(nums)
    for i, n in enumerate(nums):
        cnt = 0
        for j in range(len(nums)):
            if i != j and n > nums[j]:
                cnt += 1
        res[i] = cnt
    return res


def diagonal_sum(grid):
    res = 0
    n = len(grid)
    for i in range(n):
        res += grid[i][i] + grid[i][n - 1 - i] if i != n - 1 - i else grid[i][i]
    return res
