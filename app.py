import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
st.title("🐾 PawPal+ Care Assistant")

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan", available_time_minutes=90)

owner = st.session_state.owner

st.subheader("User and Pet Profiles")
col1, col2 = st.columns(2)
with col1:
    owner.name = st.text_input("Owner Name", value=owner.name)
with col2:
    pet_name_input = st.text_input("New Pet Name", value="Mochi")

if st.button("Register Pet"):
    if pet_name_input:
        owner.add_pet(Pet(name=pet_name_input, species="dog"))
        st.success(f"Successfully registered {pet_name_input}!")

if owner.pets:
    st.caption(f"Currently tracking: {', '.join([p.name for p in owner.pets])}")

st.divider()

st.subheader("Activity Planning")
if not owner.pets:
    st.info("Please register a pet profile above before designing tasks.")
else:
    target_pet = st.selectbox("Assign Task To", options=[p.name for p in owner.pets])
    
    col_t, col_d, col_p = st.columns(3)
    with col_t:
        task_title = st.text_input("Task Title", value="Morning Walk")
    with col_d:
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    with col_p:
        priority = st.selectbox("Priority", ["high", "medium", "low"], index=0)

    if st.button("Add Task"):
        pet_obj = next(p for p in owner.pets if p.name == target_pet)
        pet_obj.add_task(Task(title=task_title, duration_minutes=int(duration), priority=priority))
        st.success(f"Added '{task_title}' to schedule!")

st.divider()

st.subheader("Build Schedule")
if st.button("Generate Today's Plan"):
    plan = Scheduler.generate_plan(owner)
    if plan:
        st.write("Current Generated Plan:")
        st.table(plan)
    else:
        st.info("No active planning records present yet.")