# Week 2 · Session 2 — Hash Maps & Frequency Counting

**Date:** 2026-06-12  
**Theme:** Frequency maps, complement counting, prefix remainders, and direct-pair lookup  
**Problem-solving method:** UMPIRE — Understand, Match, Plan, Implement, Review, Evaluate

---

## What We Covered

Session 2 continued using hash maps and sets to replace repeated searching with
constant-time lookups. The problems focused on counting exact frequencies,
matching complementary values, distributing repeated values without
duplication, and tracking previously assigned strings.

Several solutions had the correct high-level pattern but required careful
handling of boundary cases. Important examples included reserving the empty
prefix in a remainder map, processing bulls before cows, treating self-pairing
remainders separately, and recording generated nicknames as already occupied.

Key techniques:
- Frequency counting with `Counter` and `defaultdict`
- Direct relationship lookup with a set of tuples
- Prefix sums grouped by remainder
- Complement counting for powers of two
- Greedy distribution into the minimum number of rows
- Tracking occupied names and the next available numeric suffix
- Generating domain suffixes with `split()` and `join()`

---

## Problems

### Version 1

| # | Problem | Technique | File |
|---|---------|-----------|------|
| 1 | **Balanced Art Collection** — longest subsequence whose maximum and minimum differ by one | Frequency map + adjacent-value lookup | `session2.py::find_balanced_subsequence` |
| 2 | **Verifying Authenticity** — validate the required values and duplicate maximum | Frequency map + exact count validation | `session2.py::is_authentic_collection` |
| 3 | **Gallery Wall** — distribute duplicates across the minimum number of distinct rows | Maximum frequency + direct row distribution | `session2.py::organize_exhibition` |
| 4 | **Gallery Subdomain Traffic** — accumulate visits for every parent domain | Domain splitting + suffix aggregation | `session2.py::subdomain_visits` |
| 5 | **Beautiful Collection** — sum frequency differences across all substrings | Fixed start + expanding frequency map | `session2.py::beauty_sum` |
| 6 | **Counting Divisible Collections** — count subarrays whose sum is divisible by `k` | Prefix sum + remainder frequencies | `session2.py::count_divisible_collections` |

### Version 2

| # | Problem | Technique | File |
|---|---------|-----------|------|
| 1 | **Cook Off** — determine how many copies of a target can be formed | Two frequency maps + limiting ratio | `session2.py::max_attempts` |
| 2 | **Dialogue Similarity** — compare aligned words using direct similarity pairs | Set of bidirectional tuples | `session2.py::is_similar` |
| 3 | **Cows and Bulls** — count exact and misplaced digit matches | Two-pass frequency counting | `session2.py::get_hint` |
| 4 | **Count Winning Pairings** — count index pairs whose sum is a power of two | Prior-frequency map + complement lookup | `session2.py::count_winning_pairings` |
| 5 | **Assigning Unique Nicknames** — generate the smallest unused suffix | Occupied-name map + next-suffix pointer | `session2.py::assign_unique_nicknames` |
| 6 | **Pair Contestants** — pair scores whose sums are divisible by `k` | Remainder frequency matching | `session2.py::pair_contestants` |

---

## Patterns to Remember

**Adjacent frequency lookup:** When a valid result can contain only values `x`
and `x + 1`, count all values once and compare each frequency with its adjacent
value. There is no need to construct the subsequence explicitly.

**Minimum rows equal maximum frequency:** If each row may contain a value only
once, a value appearing `f` times requires at least `f` rows. Creating that many
rows and placing its occurrences into different rows reaches the lower bound.

**Generate structured suffixes from components:** For hierarchical strings such
as domains, split into components and join each suffix. This is clearer and less
error-prone than scanning individual characters backward.

**Seed the empty prefix:** In divisible-subarray problems, initialize remainder
zero with one occurrence. This represents the empty prefix and counts valid
subarrays that begin at index zero.

**Direct similarity is not transitive:** Store each permitted word pair
directly. A set of tuples preserves multiple relationships for the same word
without implying that two words are similar through an intermediate word.

**Count exact matches before partial matches:** In Bulls and Cows, bulls consume
specific occurrences first. Only unmatched digits may be considered for cows;
otherwise, an early cow can consume a digit needed for a later bull.

**Count pairs using earlier values only:** For each current value, look up all
complements among values already processed, then add the current value to the
frequency map. This counts each index pair exactly once.

**Store generated names as occupied:** A generated name such as `"Ace(1)"` can
also appear as a later direct request. Record every assigned name and remember
the next suffix worth trying for each requested base name.

**Handle self-complementary remainders separately:** Remainder `0`, and
remainder `k / 2` when `k` is even, pair with themselves and therefore require
even frequencies. Every other remainder `r` must have the same frequency as
`k - r`.

---

## Notes

- Exact frequency validation can prove both that required values exist and that
  unexpected values do not fit when the input length is fixed.
- The beauty-sum solution is O(n²) for a fixed-size character alphabet because
  every substring is extended once and frequency extrema scan a bounded map.
- The winning-pair solution includes the maximum possible power-of-two sum and
  applies the required modulo `10**9 + 7`.
- Nested conditions in the remainder-pairing solution fully handle special
  remainders before ordinary complement logic runs.
- The final review covered all prompt examples, previously failing edge cases,
  duplicate-heavy cases, and exhaustive small inputs for the core counting
  algorithms.
