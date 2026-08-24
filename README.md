# WeBWorK Roster Formatter

This application is an internal ETL tool designed for faculty to convert roster exports directly into the formatted CSV required by WeBWorK.

---

## What It Does

The application cleans and restructures your exported roster automatically. Specifically, it:
* Removes unneeded columns (`Student ID` and `Class Level`).
* Splits student names into separate `First Name` and `Last Name` columns.
* Formats student email addresses and extracts usernames.
* Inserts necessary WeBWorK roster fields (`Status`, `Comment`, `Section`, `Recitation`, `Password`, and `Permission`).

---

## How to Use It

### Step 1: Export Your Roster
1. Log into **Merlin**.
2. Navigate to **Faculty Services**.
3. Select your course.
4. Click **Export** and download the roster as a **CSV** file.

---

### Windows Setup & Execution

1. **Download:** From the repository (the files above), download the file `WebWorkETL_Windows.exe`.
2. **Launch:** Double-click `WebWorkETL_Windows.exe` to run the tool.
   * *SmartScreen Prompt:* If Windows shows a *"Windows protected your PC"* popup, click **More info** and then click **Run anyway**.
3. **Format:**
   * Click **Browse...** and select the CSV file you exported from Merlin.
   * Click **Process & Save CSV**.
   * Choose where to save your formatted WeBWorK file and click **Save**.

---
### macOS Setup & Execution

1. **Download:** From the repository (the files above), download `webwork_ETL_mac.zip` (or `.app`).
2. **Launch:** Double-click the application to open it.
   * *Security Prompt:* If macOS blocks the app, **Right-Click** (or hold `Control` and click) `webwork_ETL.app`, select **Open**, and click **Open** in the confirmation popup.
3. **Format:**
   * Click **Browse...** and select the CSV file you exported from Merlin.
   * Click **Process & Save CSV**.
   * Choose where to save your formatted WeBWorK file and click **Save**.


