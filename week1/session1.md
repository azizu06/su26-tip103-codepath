# Week 1 · Session 1 — Strings & Arrays

**Date:** 2026-06-05  
**Theme:** Intro to arrays and strings; UPI problem-solving framework  
**Problem-solving method:** UPI — Understand, Plan, Implement

---

## What We Covered

Session 1 introduced the foundational data structures (lists and strings in Python) and a structured way to approach problems: **UPI**. The core idea is to resist jumping to code, and instead verbalize understanding, sketch a plan, then implement. Most bugs at this stage come from skipping the first two steps.

Key operations practiced:
- Indexing, iteration, and in-place mutation of lists
- String `.replace()`, `.lower()`, and character membership
- Nested loops over 2D arrays (matrices)
- Modulo for divisibility checks
- Sorting as a preprocessing step

---

## Problems

### Version 1

| # | Problem | Technique | File |
|---|---------|-----------|------|
| 1 | **Hunny Hunt** — linear search without builtins | Iteration | `session1.py::linear_search` |
| 2 | **Bouncy, Flouncy, Trouncy, Pouncy** — simulate variable with string ops | Iteration + conditionals | `session1.py::final_value_after_operations` |
| 3 | **T-I-Double Guh-Er II** — strip character substrings, case-insensitive | String `.replace()` | `session1.py::tiggerfy` |
| 4 | **Non-decreasing Array** — at most one violation allowed | Single pass, counter | `session1.py::non_decreasing` |
| 5 | **Missing Clues** — find missing ranges in `[lower, upper]` | Sort + gap scan | `session1.py::find_missing_clues` |
| 6 | **Vegetable Harvest** — count target values in 2D grid | Nested loops | `session1.py::harvest` |
| 7 | **Eeyore's House** — count pairs where `pile1[i] % (pile2[j] * k) == 0` | Brute force nested loops | `session1.py::good_pairs` |
| 8 | **Local Maximums** — find local max in each 3×3 window | Grid traversal + directions array | `session1.py::local_maximus` |

### Version 2

| # | Problem | Technique | File |
|---|---------|-----------|------|
| 1 | **Words Containing Character** — return indices of matching words | Iteration + `in` | `session1.py::words_with_char` |
| 2 | **HulkSmash** — FizzBuzz variant | Modulo + conditionals | `session1.py::hulk_smash` |
| 3 | **Encode** — shuffle string by index mapping | Index reassignment | `session1.py::shuffle` |
| 4 | **Good Samaritan** — minimum boxes to hold total meals | Sort descending + greedy | `session1.py::minimum_boxes` |
| 5 | **Heist** — find wealthiest customer in 2D accounts matrix | Nested loops + running max | `session1.py::wealthiest_customer` |
| 6 | **Smaller Than** — for each element, count how many others are smaller | Brute force O(n²) | `session1.py::smaller_than_current` |
| 7 | **Diagonal** — sum primary and secondary diagonals, no double-count center | Index math | `session1.py::diagonal_sum` |
| 8 | **Defuse the Bomb** — circular array sum of next/prev k elements | Modulo for wraparound | `session1.py::defuse` |

---

## Patterns to Remember

**Modulo for circular indexing:** `code[(i + j) % n]` — when you need to wrap around an array, `%` is the tool. Shows up in circular queues, ring buffers, and round-robin problems.

**Direction arrays for grid neighbors:** Instead of four separate if-blocks, define `dirs = [(-1,0),(1,0),(0,1),(0,-1),...]` and loop. Scales cleanly to 8-directional grids.

**Sort before gap-scanning:** In `find_missing_clues`, sorting first turns an O(n²) membership check into a single O(n) pass through gaps between consecutive elements.

**Greedy on sorted data:** `minimum_boxes` sorts capacity descending and subtracts greedily — the largest box first minimizes the count. A classic greedy pattern when order doesn't matter but size does.

---

## Notes

- The UPI framework felt slow at first but caught edge cases I would have missed by jumping straight to code (especially the `non_decreasing` off-by-one on the range check).
- `tiggerfy` is a good reminder that `str.replace()` is idempotent and can be chained — no need to track position manually when you're doing global substitutions.
- `diagonal_sum` tripped me up until I drew it out: the center cell of an odd-sized grid lands on both diagonals, so you have to handle `i == n - 1 - i` separately.
