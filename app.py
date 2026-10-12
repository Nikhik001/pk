import csv
import io
import subprocess
import sys
import tempfile
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="School Board Result Analysis", page_icon="🎓", layout="wide")
st.title("🎓 School Board Result Analysis")
st.write(
    "Upload a text file, run the original Python program, and view or download the resulting CSV."
)

ss_path = Path(__file__).with_name("ss.py")

st.header("1. Introduction")
st.write(
    "This project processes student result records, calculates totals, sorts the records, "
    "and creates a CSV file."
)

st.header("2. See the original code")
if ss_path.exists():
    st.code(ss_path.read_text(encoding="utf-8"), language="python")
else:
    st.error("The original ss.py file was not found. Put ss.py in the same folder as app.py.")

st.header("3. Upload your text file")
uploaded_file = st.file_uploader("Choose a text file", type=["txt"])

st.header("4. Run the original Python program")
if st.button("Run code and show result", type="primary"):
    if not ss_path.exists():
        st.error("The original ss.py file was not found.")
    elif uploaded_file is None:
        st.warning("Please upload a .txt file first.")
    else:
        try:
            with tempfile.TemporaryDirectory() as folder:
                workdir = Path(folder)
                # The original script expects its input to be named kk.py.
                (workdir / "kk.py").write_bytes(uploaded_file.getvalue())
                result = subprocess.run(
                    [sys.executable, str(ss_path)],
                    cwd=workdir,
                    capture_output=True,
                    text=True,
                    timeout=30,
                    check=False,
                )

                if result.returncode != 0:
                    st.error("The Python program reported an error.")
                    st.code(result.stderr or result.stdout or "No error message was returned.")
                else:
                    st.success("The program finished running.")
                    if result.stdout.strip():
                        st.subheader("Program output")
                        st.code(result.stdout)

                    csv_path = workdir / "students.csv"
                    if csv_path.exists():
                        csv_bytes = csv_path.read_bytes()
                        csv_text = csv_bytes.decode("utf-8-sig", errors="replace")
                        records = list(csv.DictReader(io.StringIO(csv_text)))
                        if records:
                            st.subheader("5. Result")
                            st.dataframe(records, use_container_width=True, hide_index=True)
                        else:
                            st.info("The CSV file was created, but it contains no result rows.")
                        st.download_button(
                            "Download students.csv",
                            data=csv_bytes,
                            file_name="students.csv",
                            mime="text/csv",
                        )
                    else:
                        st.warning("The program ran, but students.csv was not created.")
        except subprocess.TimeoutExpired:
            st.error("The program took too long to finish.")
        except Exception as exc:
            st.error(f"Error: {type(exc).__name__}: {exc}")
