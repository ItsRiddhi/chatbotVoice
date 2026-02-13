# How to Find Your Project ID, Location ID, and Agent ID

## 1. PROJECT_ID
1.  Go to the **Google Cloud Console Dashboard**: [https://console.cloud.google.com/home/dashboard](https://console.cloud.google.com/home/dashboard)
2.  Click the **Project Dropdown** at the top left (next to the Google Cloud logo).
3.  A modal will appear listing your projects.
4.  Find your project name. The **ID** is in the column next to the name.
    *   *Example*: `medical-companion-12345`

## 2. AGENT_ID and LOCATION_ID
1.  Go to the **Dialogflow CX Console**: [https://dialogflow.cloud.google.com/cx/projects](https://dialogflow.cloud.google.com/cx/projects)
2.  Select your project.
3.  You should see your Agent listed. If you haven't created one yet, click **Create Agent**.
    *   Select **Build your own**.
    *   Name it `MedicalCompanion`.
    *   Select a location (e.g., `us-central1`). **This is your LOCATION_ID**.
    *   Click **Create**.
4.  Once created, click the **three vertical dots** next to your Agent's name in the list, or if you are inside the agent, look at the URL.
5.  **The Easiest Way**:
    *   Open your Agent.
    *   Look at the browser URL. It looks like this:
        `https://dialogflow.cloud.google.com/cx/projects/PROJECT_ID/locations/LOCATION_ID/agents/AGENT_ID`
    *   **Copy the last part** (the long string of numbers/letters after `/agents/`). **This is your AGENT_ID**.
    *   **Copy the location part** (e.g., `us-central1`, `global`, etc.). **This is your LOCATION_ID**.
