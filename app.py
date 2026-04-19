import streamlit as st
from pathlib import Path
import shutil

st.set_page_config(page_title="File Manager", layout="centered")

st.title("📁 File Manager App")

menu = st.sidebar.selectbox("Choose Option", [
    "Create Folder", "View Files",
    "Delete Folder", "Create File",
    "Read File", "Delete File"
])

# Show files
def show_files():
    files = [f.name for f in Path.cwd().iterdir() if not f.name.startswith(".")]
    st.write(files)


if menu == "Create Folder":
    name = st.text_input("Enter folder name")
    if st.button("Create"):
        p = Path(name)
        if not p.exists():
            p.mkdir()
            st.success("Folder created")
        else:
            st.warning("Already exists")


elif menu == "View Files":
    if st.button("Refresh"):
        show_files()


elif menu == "Delete Folder":
    name = st.text_input("Folder name")
    if st.button("Delete"):
        p = Path(name)
        if p.exists():
            shutil.rmtree(p)
            st.success("Deleted")
        else:
            st.error("Not found")


elif menu == "Create File":
    name = st.text_input("File name")
    data = st.text_area("Write content")

    if st.button("Create File"):
        Path(name).write_text(data)
        st.success("File created")


elif menu == "Read File":
    name = st.text_input("File name")
    if st.button("Read"):
        p = Path(name)
        if p.exists():
            st.text(p.read_text())
        else:
            st.error("File not found")


elif menu == "Delete File":
    name = st.text_input("File name")
    if st.button("Delete File"):
        p = Path(name)
        if p.exists():
            p.unlink()
            st.success("Deleted")
        else:
            st.error("Not found")