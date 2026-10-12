# School Board Result Analysis — Streamlit app

This package contains:

- `ss.py` — the original Python program, included unchanged.
- `app.py` — the web interface. It displays `ss.py`, accepts a `.txt` upload, runs the original script, displays the output and offers `students.csv` for download.
- `requirements.txt` — the app dependency.

## Important detail about the input file

The original `ss.py` opens a file named `kk.py`. The web interface therefore takes the uploaded `.txt` file and temporarily makes it available to the unchanged script under the expected name `kk.py`. The upload is used in a temporary working directory; the repository's files are not overwritten.

The uploaded text must follow the exact record format expected by the original program. Test with a sample file first. Only upload student information you are authorized to process.

## Deploy on Streamlit Community Cloud

1. Extract this ZIP on your device.
2. Upload `app.py`, `requirements.txt`, and `ss.py` to the root of your GitHub repository (for example, `Nikhik001/project`). Do not replace or edit your existing `ss.py`; compare the ZIP's copy with yours if you already have it in GitHub.
3. Open https://share.streamlit.io/ and sign in with GitHub.
4. Choose **Create app** → **Yup, I have an app**.
5. Select your repository, branch `main`, and main file path `app.py`.
6. Click **Deploy**. Streamlit will provide the live app URL.

GitHub Pages alone cannot execute Python. Use the Streamlit app URL for uploading a file and running the Python program. Your existing GitHub Pages site can remain separate.
