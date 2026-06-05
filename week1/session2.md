# Week 1 · Session 2 — Strings & Arrays (Two Pointers)

**Date:** 2026-06-05  
**Theme:** Two-pointer technique; interval problems; in-place array manipulation  
**Problem-solving method:** UMPIRE — Understand, Match, Plan, Implement, Review, Evaluate

---

## What We Covered

Session 2 introduced the **two-pointer** pattern, one of the most frequently tested array techniques in technical interviews. The core insight: when an array is sorted (or can be made sorted), two pointers moving inward from opposite ends can replace a nested O(n²) loop with an O(n) pass.

We also covered **interval merging and insertion**, which requires thinking about how ranges overlap geometrically before touching code.

Key techniques:
- Two pointers: converging (palindrome, two-sum, container), partitioning (sort by parity), in-place reversal
- Interval overlap: merge by sorting start, insert by finding left/right overlap boundaries
- In-place array modification with a write-pointer (`l` index tracking where to write next)
- Matrix operations: transpose and element-wise addition

---

## Problems

### Version 1

| # | Problem | Technique | File |
|---|---------|-----------|------|
| 1 | **Transpose Matrix** — swap rows and columns | Nested loops, new grid `res[c][r] = matrix[r][c]` | `session2.py::transpose` |
| 2 | **Two-Pointer Reverse List** — reverse in-place | Two pointers, swap inward | `session2.py::reverse_list` |
| 3 | **Remove Duplicates** — in-place, sorted array | Two pointers (write pointer `l`) | `session2.py::remove_dupes` |
| 4 | **Sort Array by Parity** — evens first, odds last | Two pointers, partition in-place | `session2.py::sort_by_parity` |
| 5 | **Container with Most Honey** — maximize `width × min(height)` | Two pointers converging, move shorter side | `session2.py::most_honey` |
| 6 | **Merge Intervals** — collapse overlapping ranges | Sort by start, expand end greedily | `session2.py::merge_intervals` |

### Version 2

| # | Problem | Technique | File |
|---|---------|-----------|------|
| 1 | **Matrix Addition** — element-wise sum of two matrices | Nested loops | `session2.py::add_matrices` |
| 2 | **Two-Pointer Palindrome** — verify string reads same both ways | Two pointers converging | `session2.py::is_palindrome` |
| 3 | **Squash Spaces** — collapse consecutive spaces, trim | `str.split()` + `" ".join()` | `session2.py::squash_spaces` |
| 4 | **Two-Pointer Two Sum** — find index pair summing to target (sorted input) | Two pointers converging | `session2.py::two_sum` |
| 5 | **Three Sum** — all unique triplets summing to zero | Sort + fix one element + two-pointer inner loop | `session2.py::three_sum` |
| 6 | **Insert Interval** — insert and merge into sorted non-overlapping list | Three-phase scan: before, overlap, after | `session2.py::insert_interval` |

---

## Patterns to Remember

**Two-pointer converging (sorted array):** Start `l=0, r=len-1`, advance whichever side makes progress toward the target. Works for two-sum (sum too small → move l right), container problem (shorter side is the bottleneck → move it), palindrome (mismatch → return False).

**Write-pointer for in-place deduplication:** `l` marks the next safe write position. `r` scans forward; only write when `items[r] != items[r-1]`. This pattern reappears in "remove elements" and "compress array" problems.

**Three Sum = sort + fix anchor + two-sum:** Sort first, then for each anchor `k`, run a standard two-pointer two-sum on the remaining slice. Skip duplicate anchors with `if k > 0 and nums[k] == nums[k-1]: continue`.

**Interval insertion three-phase logic:**
1. Add all intervals that end *before* `new_interval` starts (no overlap).
2. Merge all intervals that overlap with `new_interval` by expanding its bounds.
3. Add all remaining intervals after the merge.

**Container / Most Honey intuition:** The water level is capped by the *shorter* wall. Moving the taller pointer can only make things worse (width shrinks, height stays capped by the short side). So always move the shorter pointer — it's the only move that could improve the result.

---

## Notes

- `three_sum` is the first problem where duplicate-skipping logic wasn't obvious from the problem statement — you have to handle it explicitly for both the outer anchor and the inner two pointers after each match.
- `insert_interval` is cleaner with the three-phase loop structure than trying to detect overlaps with a single conditional. Drawing the three zones on paper before coding made it click.
- `squash_spaces` ended up one line with `split()` + `join()` — the built-in handles consecutive spaces and leading/trailing automatically. Good reminder to know your string API before reaching for manual index tracking.
- The Container problem's proof that "move the shorter pointer" is optimal took a few minutes of argument by contradiction to convince myself — worth writing out once to internalize it.
