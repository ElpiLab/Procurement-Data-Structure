import streamlit as st

st.set_page_config(page_title="Procurement DSA Visualizer", layout="wide")

st.title("📊 Procurement DSA Visualizer")
st.markdown("### 8 Data Structures + 3 Algorithms · Procurement Scenarios")

st.write("""
This interactive tool visualizes classic data structures and algorithms using common procurement scenarios.
All data is synthetic. Select a module from the dropdown to explore.
""")

# Define all modules (8 DS + 3 algo + intro)
modules = [
    "🏠 Introduction",
    "1️⃣ Array – Approval Queue",
    "2️⃣ Linked List – Audit Trail",
    "3️⃣ Stack – Undo/Redo in Orders",
    "4️⃣ Queue – Support Tickets",
    "5️⃣ Hash Table – Cost Center Lookup",
    "6️⃣ Tree – Material Group Hierarchy",
    "7️⃣ Graph – Approval Workflow Structure",
    "8️⃣ Heap – Priority Orders",
    "📊 Sorting – Purchase Orders by Amount",
    "🔍 Searching – Binary Search on Cost Centers",
    "🔄 Graph Algorithms – Shortest Approval Path (BFS/DFS)",
]

selected = st.selectbox("Choose a module to visualize:", modules)

# Introduction
if selected == "🏠 Introduction":
    st.info("""
    **What you'll see here:**
    - Each data structure is shown with a procurement example.
    - Interactive buttons let you add, remove, or search items.
    - Python code snippets explain the underlying logic.
    - Time complexity notes help you understand efficiency.
    
    **Start by picking a module from the dropdown above.**
    """)
    st.markdown("""
    ---
    ### Roadmap (you implement these)
    - ✅ App skeleton
    - ⏳ Array demo (add/remove POs)
    - ⏳ Tree demo (material group hierarchy)
    - ⏳ Sorting demo (quick sort on PO amounts)
    - ⏳ Searching demo (binary search on cost centers)
    - ⏳ Graph BFS/DFS (approval workflows)
    - ... and the rest
    """)

# ---------- 1. Array ----------
elif selected == "1️⃣ Array – Approval Queue":
    st.subheader("Daily Approval Queue as an Array")
    
    if "array_approvals" not in st.session_state:
        st.session_state.array_approvals = ["PO-101", "PO-102", "PO-103"]
    
    # Visual boxes
    cols = st.columns(len(st.session_state.array_approvals))
    for i, po in enumerate(st.session_state.array_approvals):
        with cols[i]:
            st.markdown(f"**{po}**  \nindex {i}")
            st.button("🗑️", key=f"del_arr_{i}", on_click=lambda idx=i: st.session_state.array_approvals.pop(idx) if st.session_state.array_approvals else None)
    
    col1, col2 = st.columns(2)
    with col1:
        new_po = st.text_input("New PO number", "PO-104")
        if st.button("➕ Append (add to end)"):
            st.session_state.array_approvals.append(new_po)
            st.rerun()
    with col2:
        if st.button("⏪ Pop first item"):
            if st.session_state.array_approvals:
                removed = st.session_state.array_approvals.pop(0)
                st.success(f"Removed {removed}")
                st.rerun()
    
    with st.expander("📘 Python code & complexity"):
        st.code("""
# Array = Python list
approvals = ['PO-101', 'PO-102', 'PO-103']
approvals.append('PO-104')   # O(1) amortized
approvals.pop(0)             # O(n) – shifts remaining elements
# Access by index: O(1)
        """)
        st.caption("Arrays are perfect for fixed-size queues where you often access by position.")

# ---------- 2. Linked List ----------
elif selected == "2️⃣ Linked List – Audit Trail":
    st.subheader("Audit Trail (Linked List of Order Changes)")
    st.warning("🚧 Under construction – will show order version history with next/prev pointers.")
    st.code("""
# Planned: each change points to previous version
class AuditNode:
    def __init__(self, order_id, prev=None):
        self.order_id = order_id
        self.prev = prev
    """)

# ---------- 3. Stack ----------
elif selected == "3️⃣ Stack – Undo/Redo in Orders":
    st.subheader("Undo/Redo Stack for Purchase Order Forms")
    st.warning("🚧 Under construction – will demonstrate LIFO behavior (last change undone first).")

# ---------- 4. Queue ----------
elif selected == "4️⃣ Queue – Support Tickets":
    st.subheader("Support Ticket Queue (FIFO)")
    st.warning("🚧 Under construction – first ticket in = first ticket resolved.")

# ---------- 5. Hash Table ----------
elif selected == "5️⃣ Hash Table – Cost Center Lookup":
    st.subheader("Cost Center Lookup (Hash Table)")
    st.warning("🚧 Under construction – O(1) lookup of manager by cost center code.")

# ---------- 6. Tree ----------
elif selected == "6️⃣ Tree – Material Group Hierarchy":
    st.subheader("Material Group Tree")
    st.warning("🚧 Under construction – your essay's star structure: parent/child material groups.")
    st.code("""
# Planned tree representation:
Services (1000)
├── Consulting (1100)
│   ├── Strategy (1110)
│   └── IT Consulting (1120)
└── Facilities (1200)
    ├── Cleaning (1210)
    └── Security (1220)
    """)

# ---------- 7. Graph ----------
elif selected == "7️⃣ Graph – Approval Workflow Structure":
    st.subheader("Approval Workflow as a Graph")
    st.warning("🚧 Under construction – nodes = roles, edges = 'can approve'.")

# ---------- 8. Heap ----------
elif selected == "8️⃣ Heap – Priority Orders":
    st.subheader("Priority Queue (Heap) for Urgent Orders")
    st.warning("🚧 Under construction – urgent orders jump to front regardless of arrival time.")

# ---------- Algorithm: Sorting ----------
elif selected == "📊 Sorting – Purchase Orders by Amount":
    st.subheader("Sorting Purchase Orders by Amount (Quick Sort Demo)")
    st.warning("🚧 Under construction – will animate Quick Sort on sample order amounts.")

# ---------- Algorithm: Searching ----------
elif selected == "🔍 Searching – Binary Search on Cost Centers":
    st.subheader("Binary Search on Sorted Cost Center Codes")
    st.warning("🚧 Under construction – O(log n) search vs O(n) linear search.")

# ---------- Algorithm: Graph Algorithms ----------
elif selected == "🔄 Graph Algorithms – Shortest Approval Path (BFS/DFS)":
    st.subheader("BFS/DFS on Approval Workflow Graph")
    st.warning("🚧 Under construction – will find shortest path from Requester to VP.")

# Footer
st.divider()
st.caption("Portfolio project – BIT studies · All data synthetic · More modules coming soon.")