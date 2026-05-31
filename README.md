# Procurement DSA Visualizer

**Live demo:** [link after deployment]

A Streamlit web app that visualizes 8 classic data structures and 3 essential algorithms using common procurement scenarios.

## Why I built this

Procurement operations often face challenges like incorrect cost centers, slow approvals, and disorganized material groups. After my Data Structures & Algorithms class, I realized these problems map directly to arrays, trees, hash tables, and graph algorithms. This project makes that connection visible – without using any real company data.

## What's inside

### Data Structures (8)
- Array – daily approval queue
- Linked List – order audit trail
- Stack – undo/redo in purchase forms
- Queue – support ticket triage
- Hash Table – cost center lookup
- Tree – material group hierarchy
- Graph – approval workflow structure
- Heap – priority orders

### Algorithms (3)
- Sorting – quick sort on purchase amounts
- Searching – binary search on cost center codes
- Graph Algorithms – BFS for shortest approval path

## Tech stack

- Python 3.10+
- Streamlit – web UI
- NetworkX – graph visualization

## How to run

```bash
git clone ...
pip install -r requirements.txt
streamlit run app.py

## About

Portfolio project for BIT studies. All data is synthetic. No real company information is used.