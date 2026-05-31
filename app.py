import streamlit as st

# Set the page config
st.set_page_config(page_title="Workflow DSA Visualizer", layout="wide")

# The Header (Anonymized)
st.title("🏢 Enterprise Workflow Optimizer")
st.markdown("### Visualizing Data Structures for ERP Efficiency")

# The Intro (Generic Business Case)
st.write("""
**The Business Problem:**
*   High operational costs in legacy ERP systems.
*   Manual errors in master data (e.g., incorrect categorization).
*   Slow approval cycles and missed strategic opportunities.

**The Technical Solution:**
*   Using Data Structures to organize complex workflow data.
*   Using Algorithms to prioritize tasks and automate routing.
""")

st.info("👇 Select a module to visualize the underlying logic.")

# Placeholder for the visualizers (Generic names)
option = st.selectbox(
    'Choose a module to view:',
    ('Introduction', 
     'Stacks (Change History Log)', 
     'Queues (Ticket Routing)', 
     'Trees (Product Categories)', 
     'Graphs (Approval Workflows)'))

if option == 'Introduction':
    st.write("Welcome to the dashboard. This project demonstrates how computer science fundamentals apply to business operations.")
    
elif option == 'Stacks (Change History Log)':
    st.warning("Visualizer for Change History Log is under construction!")
    st.write("*Concept: Track changes to master data records (Last-In, First-Out).")
    
elif option == 'Queues (Ticket Routing)':
    st.warning("Visualizer for Ticket Routing is under construction!")
    st.write("*Concept: First-Come, First-Served support ticket management.")
    
else:
    st.warning(f"Visualizer for {option} is under construction!")
    st.write("*This module will demonstrate the algorithmic efficiency of the selected structure.*")


# streamlit run app.py