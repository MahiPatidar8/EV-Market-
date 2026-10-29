# EV Market site

1. `pip install -r requirements.txt`
2. Open `config.json` and paste your links:
   - `dashboard_url`: Tableau Public view, e.g. `https://public.tableau.com/views/YourWorkbook/YourDashboard`
   - `story_url`: Tableau Public story, e.g. `https://public.tableau.com/views/YourWorkbook/YourStory`
   - `github_url`: your repository
3. `python app.py` and open http://127.0.0.1:5000

Use the plain view URL (without `?:showVizHome=no` etc.). Publish the workbook to Tableau Public first so it can be embedded.
