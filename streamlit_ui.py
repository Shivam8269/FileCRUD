import streamlit as st
from pathlib import Path
import os

st.set_page_config(page_title="File Manager", page_icon="📁", layout="wide")

st.title("📁 File & Folder Manager")
st.markdown("---")

# ── Helper ──────────────────────────────────────────────────────────────────
def list_items():
    p = Path('')
    return sorted(p.rglob('*'))

def refresh():
    st.rerun()

# ── Sidebar – file/folder browser ───────────────────────────────────────────
with st.sidebar:
    st.header("📂 Current Directory")
    items = list_items()
    if items:
        for item in items:
            icon = "📁" if item.is_dir() else "📄"
            st.text(f"{icon} {item}")
    else:
        st.info("No files or folders found.")
    if st.button("🔄 Refresh", use_container_width=True):
        refresh()

# ── Tabs ─────────────────────────────────────────────────────────────────────
tabs = st.tabs([
    "➕ Create File",
    "📖 Read File",
    "✏️ Update File",
    "🗑️ Delete File",
    "🔤 Rename File",
    "📁 Create Folder",
    "🗂️ Remove Folder",
])

# ── 1. Create File ────────────────────────────────────────────────────────────
with tabs[0]:
    st.subheader("Create a New File")
    file_name = st.text_input("File name (e.g. hello.txt)", key="create_name")
    content   = st.text_area("File content", key="create_content", height=150)
    if st.button("Create File", type="primary"):
        if not file_name.strip():
            st.warning("Please enter a file name.")
        else:
            p = Path(file_name.strip())
            if p.exists():
                st.error("⚠️ File already exists!")
            else:
                try:
                    p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_text(content)
                    st.success(f"✅ '{file_name}' created successfully!")
                    refresh()
                except Exception as e:
                    st.error(f"Error: {e}")

# ── 2. Read File ──────────────────────────────────────────────────────────────
with tabs[1]:
    st.subheader("Read a File")
    files = [str(i) for i in list_items() if i.is_file()]
    if files:
        file_name = st.selectbox("Select file", files, key="read_select")
        if st.button("Read File", type="primary"):
            try:
                st.code(Path(file_name).read_text(), language="text")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.info("No files available.")

# ── 3. Update File ────────────────────────────────────────────────────────────
with tabs[2]:
    st.subheader("Update a File")
    files = [str(i) for i in list_items() if i.is_file()]
    if files:
        file_name  = st.selectbox("Select file", files, key="update_select")
        update_mode = st.radio("Update mode", ["Overwrite", "Append"], horizontal=True)
        new_content = st.text_area("New content", height=150, key="update_content")
        if st.button("Update File", type="primary"):
            try:
                mode = 'w' if update_mode == "Overwrite" else 'a'
                with open(file_name, mode) as f:
                    f.write(new_content)
                st.success(f"✅ '{file_name}' updated successfully!")
                refresh()
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.info("No files available.")

# ── 4. Delete File ────────────────────────────────────────────────────────────
with tabs[3]:
    st.subheader("Delete a File")
    files = [str(i) for i in list_items() if i.is_file()]
    if files:
        file_name = st.selectbox("Select file to delete", files, key="delete_select")
        st.warning(f"⚠️ This will permanently delete **{file_name}**.")
        if st.button("🗑️ Delete File", type="primary"):
            try:
                os.remove(file_name)
                st.success(f"✅ '{file_name}' deleted.")
                refresh()
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.info("No files available.")

# ── 5. Rename File ────────────────────────────────────────────────────────────
with tabs[4]:
    st.subheader("Rename a File")
    files = [str(i) for i in list_items() if i.is_file()]
    if files:
        file_name = st.selectbox("Select file to rename", files, key="rename_select")
        new_name  = st.text_input("New file name", key="rename_new")
        if st.button("Rename File", type="primary"):
            if not new_name.strip():
                st.warning("Please enter a new name.")
            else:
                try:
                    Path(file_name).rename(new_name.strip())
                    st.success(f"✅ Renamed to '{new_name}'.")
                    refresh()
                except Exception as e:
                    st.error(f"Error: {e}")
    else:
        st.info("No files available.")

# ── 6. Create Folder ──────────────────────────────────────────────────────────
with tabs[5]:
    st.subheader("Create a Folder")
    folder_name = st.text_input("Folder name", key="folder_create")
    if st.button("Create Folder", type="primary"):
        if not folder_name.strip():
            st.warning("Please enter a folder name.")
        else:
            p = Path(folder_name.strip())
            if p.exists():
                st.error("⚠️ Folder already exists!")
            else:
                try:
                    p.mkdir(parents=True)
                    st.success(f"✅ Folder '{folder_name}' created.")
                    refresh()
                except Exception as e:
                    st.error(f"Error: {e}")

# ── 7. Remove Folder ──────────────────────────────────────────────────────────
with tabs[6]:
    st.subheader("Remove a Folder")
    folders = [str(i) for i in list_items() if i.is_dir()]
    if folders:
        folder_name = st.selectbox("Select folder to remove", folders, key="folder_remove")
        st.warning(f"⚠️ Folder must be **empty** to be removed.")
        if st.button("🗑️ Remove Folder", type="primary"):
            try:
                Path(folder_name).rmdir()
                st.success(f"✅ Folder '{folder_name}' removed.")
                refresh()
            except OSError:
                st.error("❌ Folder is not empty. Remove contents first.")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.info("No folders available.")