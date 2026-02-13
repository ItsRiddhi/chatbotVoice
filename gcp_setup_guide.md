# How to Create a Google Cloud Service Account and Download the JSON Key

1.  **Go to the Google Cloud Console**:
    - Visit [https://console.cloud.google.com/iam-admin/serviceaccounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
    - Ensure your project is selected in the top dropdown.

2.  **Create Service Account**:
    - Click **+ CREATE SERVICE ACCOUNT** (top center).
    - **Name**: `medical-companion-sa` (or anything you like).
    - **Description**: "For voice medical companion app".
    - Click **CREATE AND CONTINUE**.

3.  **Grant Access (Roles)**:
    - In the "Select a role" filter, search for and select **Basic** > **Owner**.
    - *Why?* This gives your service account full access to all resources in your project, which is easiest for development.
    - *Alternative (if you prefer specific roles)*:
        - **Dialogflow API Client**
        - **Cloud Speech Client**
        - **Cloud Text-to-Speech Admin**
    - Click **CONTINUE** and then **DON E**.

4.  **Create Key**:
    - You will see your new service account in the list.
    - Click the **three vertical dots** under "Actions" (far right).
    - Select **Manage keys**.
    - Click **ADD KEY** > **Create new key**.
    - Choose **JSON** (Radio button should be selected by default).
    - Click **CREATE**.

5.  **Download & Save**:
    - The JSON file will automatically download to your computer.
    - **Move this file** to your project folder: `C:\Users\ARYAN ANGRAL\Desktop\RiddhiGupta_Project_Internship\`
    - **Rename it** to something simple like `service.json`.

6.  **Update .env**:
    - Open your `.env` file.
    - Set `GOOGLE_APPLICATION_CREDENTIALS` to the absolute path of this file.
    - Example: `GOOGLE_APPLICATION_CREDENTIALS="C:\\Users\\ARYAN ANGRAL\\Desktop\\RiddhiGupta_Project_Internship\\service.json"` (Note the double backslashes for Windows paths in some editors, though usually single forward slashes work too: `C:/Users/.../service.json`).
