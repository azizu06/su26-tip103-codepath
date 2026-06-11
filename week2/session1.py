from collections import Counter, defaultdict

# Version 1


def total_treasure(treasure_map):
    return sum(treasure_map.values())


def can_trust_message(message):
    letters = {}
    for c in message:
        if c.isspace():
            continue
        letters[c] = letters.get(c, 0) + 1
    return len(letters) == 26


def find_duplicate_chests(chests):
    freq = {}
    for c in chests:
        freq[c] = freq.get(c, 0) + 1
    res = []
    for num, cnt in freq.items():
        if cnt == 2:
            res.append(num)
    return res


def can_make_balanced(code):
    freq = {}
    for c in code:
        freq[c] = freq.get(c, 0) + 1
    for c in code:
        prev = freq[c]
        freq[c] -= 1
        if not freq[c]:
            del freq[c]
        if len(set(freq.values())) <= 1:
            return True
        freq[c] = prev
    return False


def find_treasure_indices(gold_amounts, target):
    seen = {}
    for i, g in enumerate(gold_amounts):
        if target - g in seen:
            return [seen[target - g], i]
        seen[g] = i


def organize_pirate_crew(group_sizes):
    groups = {}
    for pirate, size in enumerate(group_sizes):
        if size not in groups:
            groups[size] = []
        groups[size].append(pirate)
    res = []
    for size, group in groups.items():
        cur = []
        for i in range(len(group)):
            cur.append(group[i])
            if len(cur) == size:
                res.append(cur)
                cur = []
    return res


def min_steps_to_match_maps(map1, map2):
    freq1, freq2 = Counter(map1), Counter(map2)
    res = 0
    for letter, cnt in freq1.items():
        if cnt > freq2[letter]:
            res += cnt - freq2[letter]
    return res


def counting_pirates_action_minutes(logs, k):
    actions = defaultdict(set)
    for id, time in logs:
        actions[id].add(time)
    res = [0] * (k + 1)
    for times in actions.values():
        res[len(times)] += 1
    return res[1:]


# Version 2


def analyze_library(library_catalog, actual_distribution):
    res = {}
    for room, cnt in library_catalog.items():
        res[room] = actual_distribution[room] - cnt
    return res


def find_common_artifacts(artifacts1, artifacts2):
    return list(set(artifacts1) & set(artifacts2))


def declutter(souvenirs, threshold):
    freq = Counter(souvenirs)
    res = []
    for s in souvenirs:
        if freq[s] < threshold:
            res.append(s)
    return res


def num_of_time_portals(portals, destination):
    freq = Counter(portals)
    res = 0
    for p in portals:
        if not destination.startswith(p):
            continue
        target = destination[(len(p)) :]
        res += freq[target] if p != target else freq[target] - 1
    return res


def detect_temporal_anomaly(time_points, k):
    seen = set()
    l = 0
    for r in range(len(time_points)):
        while r - l > k:
            seen.remove(time_points[l])
            l += 1
        if time_points[r] in seen:
            return True
        seen.add(time_points[r])
    return False


def find_travelers(races):
    winners, losers = set(), defaultdict(int)
    for winner, loser in races:
        if loser in winners:
            winners.remove(loser)
        if winner not in losers:
            winners.add(winner)
        losers[loser] += 1
    res = [sorted(winners)]
    group = []
    for loser, cnt in losers.items():
        if cnt == 1:
            group.append(loser)
    return res + [sorted(group)]


def find_most_frequent_word(text, illegibles):
    banned = set()
    for i in illegibles:
        banned.add(i.lower())
    clean = []
    for c in text:
        clean.append(c.lower() if c.isalpha() else " ")
    freq = Counter("".join(clean).split())
    best = 0
    res = ""
    for w, cnt in freq.items():
        if w in banned:
            continue
        if cnt > best:
            best = cnt
            res = w
    return res


def display_time_portal_usage(usage_records):
    freq = defaultdict(int)
    times = set()
    portals = set()
    for _, portal, time in usage_records:
        freq[(time, portal)] += 1
        times.add(time)
        portals.add(portal)
    times, portals = sorted(times), sorted(portals, key=int)
    res = [["Portal"] + times]
    for p in portals:
        row = [p]
        for t in times:
            row.append(str(freq[(t, p)]))
        res.append(row)
    return res
