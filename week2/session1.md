# Week 2 · Session 1 — Hash Maps & Sets

**Date:** 2026-06-10  
**Theme:** Hash maps, sets, frequency counting, and grouped data  
**Problem-solving method:** UMPIRE — Understand, Match, Plan, Implement, Review, Evaluate

---

## What We Covered

Session 1 focused on recognizing when a hash map or set can replace repeated
searching. The main pattern was to store information while scanning the input,
then use constant-time lookups to count frequencies, find complements, detect
duplicates, or organize related values.

The session also emphasized matching the exact output contract. Several
solutions had the right core idea but still needed careful handling of
duplicate values, numeric sorting of strings, punctuation boundaries, and
string conversion in display tables.

Key techniques:
- Frequency maps with dictionaries and `Counter`
- Membership and intersection with sets
- Complement lookup for pair problems
- Sliding windows backed by a set
- Grouping values with dictionaries and `defaultdict`
- Cleaning text character by character
- Sorting string values with a numeric key

---

## Problems

### Version 1

| # | Problem | Technique | File |
|---|---------|-----------|------|
| 1 | **Counting Treasure** — total all treasure values | Dictionary values + `sum()` | `session1.py::total_treasure` |
| 2 | **Pirate Message Check** — verify every alphabet letter appears | Frequency map + whitespace filtering | `session1.py::can_trust_message` |
| 3 | **Duplicate Treasure Chests** — find values appearing exactly twice | Frequency map | `session1.py::find_duplicate_chests` |
| 4 | **Booby Trap** — remove one character to equalize frequencies | Frequency map + temporary mutation | `session1.py::can_make_balanced` |
| 5 | **Overflowing With Gold** — find two indices summing to target | Hash map complement lookup | `session1.py::find_treasure_indices` |
| 6 | **Organize the Pirate Crew** — partition pirates by required group size | Grouping with a dictionary | `session1.py::organize_pirate_crew` |
| 7 | **Match Treasure Maps** — minimum replacements to form an anagram | Two frequency maps | `session1.py::min_steps_to_match_maps` |
| 8 | **Pirates' Action Minutes** — count unique active minutes per pirate | Dictionary of sets | `session1.py::counting_pirates_action_minutes` |

### Version 2

| # | Problem | Technique | File |
|---|---------|-----------|------|
| 1 | **Library of Alexandria** — compare expected and actual scroll counts | Dictionary traversal | `session1.py::analyze_library` |
| 2 | **Grecian Artifacts** — find artifacts shared by two lists | Set intersection | `session1.py::find_common_artifacts` |
| 3 | **Souvenir Declutter** — retain occurrences below a frequency threshold | `Counter` + original-order scan | `session1.py::declutter` |
| 4 | **Time Portals** — count ordered concatenation pairs | Frequency map + prefix/suffix matching | `session1.py::num_of_time_portals` |
| 5 | **Detect Temporal Anomaly** — find nearby duplicate events | Sliding window + set | `session1.py::detect_temporal_anomaly` |
| 6 | **Time Portal Race Rankings** — group travelers by loss count | Sets + loss frequency map | `session1.py::find_travelers` |
| 7 | **Lingual Frequencies** — find the most frequent allowed word | Text normalization + frequency map | `session1.py::find_most_frequent_word` |
| 8 | **Time Portal Usage** — build a sorted portal/time count table | Tuple-key frequency map + sorted sets | `session1.py::display_time_portal_usage` |

---

## Patterns to Remember

**Frequency map:** When a problem repeatedly asks "how many times does this
value appear?", count once and reuse the result. `Counter(items)` is a concise
version of the standard dictionary counting pattern.

**Complement lookup:** In pair problems, store values already seen and ask
whether the value needed to complete the target exists. This changes many
O(n²) nested-loop solutions into O(n) scans.

**Preserve occurrences by scanning the original list:** A frequency map stores
counts, but iterating over its keys removes repeated output values. When the
answer must preserve duplicates and order, build the map first and then scan
the original input.

**Validate before slicing:** Taking
`destination[len(portal):]` finds a suffix of the correct length, but it does
not prove that `portal` matches the beginning. Check the prefix first, then
count matching suffixes.

**Punctuation should create word boundaries:** Deleting punctuation from
`"alpha,beta"` produces `"alphabeta"`. Replacing non-letter characters with
spaces produces two separate words that `.split()` can parse correctly.

**Sorting numeric strings:** `sorted(portals, key=int)` compares each portal by
its integer value while returning the original strings. The `key` changes the
comparison, not the stored data.

**Output shape matters:** A correct algorithm can still fail if the grader
expects sorted rows, string counts, or exact table dimensions. Recheck both the
values and their types against the prompt.

---

## Notes

- `isspace()` was useful because whitespace includes tabs and newlines, not
  only the literal space character.
- Temporarily changing a frequency map requires restoring the previous state
  before testing the next candidate.
- In the ordered portal-pair problem, the frequency map counts possible second
  indices. When both portal strings are equal, subtract one so an index cannot
  pair with itself.
- Sets are unordered, but `sorted()` accepts a set and returns a new list.
  Using `key=int` made numeric portal ordering work without converting the
  output values away from strings.
- The portal usage table reinforced that building the required output already
  takes O(portals × times), so the nested table-building loop is necessary.
