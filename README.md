# DSA Practice — @gkuchar

> Systematic DSA preparation following the NeetCode 150 roadmap, with solutions automatically organized by topic via a custom CI/CD pipeline.

---

## Project Structure

```
dsa-practice/
  .github/workflows/
    reorganize.yml        ← GitHub Action pipeline
  src/
    arrays_and_hashing/ ← Partitioned by Topic
      two_integer_sum/ ← Each Topic Divided into Problems
        two_integer_sum_0.py ← Each Problem Subdivided into Submissions
    trees/
      invert_a_binary_tree/
        invert_a_binary_tree_0.py
    ...
  problem_topic_map.py    ← 150-problem slug-to-topic mapping
  reorganize.py           ← reorganization script
```

---

## Pipeline

Accepted solutions submitted on [NeetCode.io](https://neetcode.io) are auto-committed to this repo via GitHub Sync. A GitHub Action triggers on every solution push, running a Python script that parses the commit diff, maps the problem to its topic, and moves the file into the structured `src/` directory, all without manual intervention.

```
NeetCode submission → GitHub Sync commit → GitHub Action → src/{topic}/{problem}/{problem}_{n}.py
```

---

## Full Problems Breakdown

| Topic | Count |
|---|---|
| Arrays & Hashing | 9 |
| Two Pointers | 5 |
| Stack | 6 |
| Binary Search | 7 |
| Sliding Window | 6 |
| Linked List | 11 |
| Trees | 15 |
| Tries | 3 |
| Backtracking | 10 |
| Heap / Priority Queue | 7 |
| Graphs | 13 |
| 1-D Dynamic Programming | 12 |
| Intervals | 6 |
| Greedy | 8 |
| Advanced Graphs | 6 |
| 2-D Dynamic Programming | 11 |
| Bit Manipulation | 7 |
| Math & Geometry | 8 |