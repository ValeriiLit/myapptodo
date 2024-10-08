import streamlit as st
import functions

def add_todo():
    new_todo = st.session_state['new_todo'] + '\n'
    todos.append(new_todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("Todo app")
st.subheader("Your todos:")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.capitalize(), key= todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.rerun()


st.text_input(label="",placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')