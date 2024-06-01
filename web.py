import streamlit as st
import functions

# https://stilllearning4ever-web-todoapp-web-cw8qkg.streamlit.app/
def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos = functions.get_todos()
    todos.append(new_todo)
    functions.set_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")

todos = functions.get_todos()
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos = functions.get_todos()
        todos.pop(index)
        functions.set_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label=" ", placeholder="Add new todo...", on_change=add_todo, key="new_todo")
