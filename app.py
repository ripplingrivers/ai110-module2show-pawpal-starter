import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
st.title("🐾 PawPal+ Care Assistant")

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan", available_time_minutes=90)

owner = st.session_state.owner

st.sidebar.header("Profile Settings")
owner.name = st.sidebar.text_input("Owner Name", value=owner.name)
owner.available_time_minutes = st.sidebar.number_input("Available Time (mins)", min_value=10, max_value=1440, value=owner.available_time_minutes)

st.sidebar.divider()
st.sidebar.subheader("Register Pet")
p_name = st.sidebar.text_input("Pet Name")
p_spec = st.sidebar.selectbox("Species", ["Dog", "Cat", "Other"])

if st.sidebar.button("Register Profile"):
    if p_name:
        owner.add_pet(Pet(name=p_name, species=p_spec))
        st.sidebar.success(f"Registered {p_name}!")

st.subheader("Design a Care Task")
if not owner.pets:
    st.info("Please register a pet profile via the sidebar configuration first.")
else:
    c1, c2, c3 = st.columns(3)
    with c1:
        target_name = st.selectbox("Assign To", options=[p.name for p in owner.pets])
    with c2:
        t_title = st.text_input("Task Title", value="Grooming")
    with c3:
        t_dur = st.number_input("Duration (mins)", min_value=5, max_value=240, value=30)
        
    c4, c5 = st.columns(2)
    with c4:
        t_start = st.text_input("Start Time (HH:MM)", value="08:00")
    with c5:
        t_freq = st.selectbox("Frequency", ["Once", "Daily"])

    if st.button("Commit Task to System"):
        pet_obj = next(p for p in owner.pets if p.name == target_name)
        pet_obj.add_task(Task(title=t_title, duration_minutes=int(t_dur), priority="high", start_time_str=t_start, frequency=t_freq))
        st.success(f"Added '{t_title}' successfully!")

st.divider()

st.subheader("Master Chronological Itinerary")
all_pairs = Scheduler.get_all_task_pairs(owner)

if not all_pairs:
    st.info("No active planning data recorded yet.")
else:
    warnings = Scheduler.detect_conflicts(all_pairs)
    for alert in warnings:
        st.warning(alert)
        
    sorted_pairs = Scheduler.sort_by_time(all_pairs)
    display_grid = []
    for pet_name, task in sorted_pairs:
        display_grid.append({
            "Time": task.start_time_str,
            "Pet Target": pet_name,
            "Activity": task.title,
            "Duration": f"{task.duration_minutes}m",
            "Frequency": task.frequency
        })
    st.table(display_grid)