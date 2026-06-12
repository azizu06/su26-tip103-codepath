from collections import Counter, defaultdict

# Version 1


def find_balanced_subsequence(art_pieces):
    freq = Counter(art_pieces)
    res = 0
    for num, cnt in freq.items():
        if num + 1 in freq:
            res = max(freq[num + 1] + cnt, res)
    return res


def is_authentic_collection(art_pieces):
    target = len(art_pieces) - 1
    if target < 1:
        return False
    freq = Counter(art_pieces)

    for i in range(1, target):
        if freq[i] != 1:
            return False
    return freq[target] == 2


def organize_exhibition(collection):
    freq = Counter(collection)
    res = [[] for _ in range(max(freq.values(), default=0))]
    for name, cnt in freq.items():
        for row in range(cnt):
            res[row].append(name)
    return res


def subdomain_visits(cpdomains):
    freq = defaultdict(int)
    for domain in cpdomains:
        cnt, site = domain.split()
        parts = site.split(".")
        for i in range(len(parts)):
            key = ".".join(parts[i:])
            freq[key] += int(cnt)
    res = []
    for domain, cnt in freq.items():
        res.append(str(cnt) + " " + domain)
    return res


def beauty_sum(collection):
    res = 0
    for i in range(len(collection)):
        freq = defaultdict(int)
        for j in range(i, len(collection)):
            freq[collection[j]] += 1
            res += max(freq.values()) - min(freq.values())
    return res


def count_divisible_collections(collection_sizes, k):
    freq = defaultdict(int)
    pre = 0
    res = 0
    freq[0] = 1
    for c in collection_sizes:
        pre += c
        res += freq[pre % k]
        freq[pre % k] += 1
    return res


# Version 2


def max_attempts(ingredients, target_meal):
    ingreds = Counter(ingredients)
    meals = Counter(target_meal)
    res = float("inf")
    for meal, cnt in meals.items():
        res = min(res, ingreds[meal] // cnt)
    return res


def is_similar(sentence1, sentence2, similar_pairs):
    if len(sentence1) != len(sentence2):
        return False
    matches = set()
    for s1, s2 in similar_pairs:
        matches.add((s1, s2))
        matches.add((s2, s1))
    for s1, s2 in zip(sentence1, sentence2):
        if s1 != s2 and (s1, s2) not in matches:
            return False
    return True


def get_hint(secret, guess):
    freq = Counter(secret)
    bulls = 0
    for i in range(len(secret)):
        if secret[i] != guess[i]:
            continue
        bulls += 1
        freq[guess[i]] -= 1
    cows = 0
    for i in range(len(secret)):
        if secret[i] != guess[i] and freq[guess[i]]:
            cows += 1
            freq[guess[i]] -= 1
    return str(bulls) + "A" + str(cows) + "B"


def count_winning_pairings(star_power):
    if not star_power:
        return 0
    powers = []
    i = 1
    while i <= 2 * max(star_power):
        powers.append(i)
        i *= 2
    res = 0
    freq = defaultdict(int)
    for s in star_power:
        for p in powers:
            res += freq[p - s]
        freq[s] += 1
    return res % (10**9 + 7)


def assign_unique_nicknames(nicknames):
    freq = defaultdict(int)
    res = []
    for name in nicknames:
        if name not in freq:
            res.append(name)
            freq[name] = 1
            continue
        k = freq[name]
        new = name + "(" + str(k) + ")"
        while new in freq:
            k += 1
            new = name + "(" + str(k) + ")"
        res.append(new)
        freq[name] = k + 1
        freq[new] = 1
    return res


def pair_contestants(scores, k):
    if len(scores) % 2 != 0:
        return False
    freq = Counter(s % k for s in scores)
    for rem, cnt in freq.items():
        if rem == 0:
            if cnt % 2 != 0:
                return False
        elif k % 2 == 0 and rem == k // 2:
            if cnt % 2 != 0:
                return False
        elif cnt != freq[k - rem]:
            return False
    return True
