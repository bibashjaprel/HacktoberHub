'''
Greenify : For automating the commit so that streak goes on.

This needs to be setup in your repository. For setup guide you can visit my repo here:

<--------- https://www.github.com/Xtha-Sunil/Greenify ---------->
'''

from github import Github
from datetime import datetime
import os

# ------------------- Configuration Section ------------------- #
# Define the GitHub API key from an environment variable.
# Make sure the API key is set up as 'api_key' in the .yml file inside .github/workflows.
api_key = os.environ['api_key']

# Define the repository where commits will be made in "<username>/<repo_name>" format.
REPO = "Xtha-Sunil/Greenify"

'''
Setup Complete: The following code will now automatically commit files daily 
to help keep your GitHub contributions heatmap green. 

Adjustments (Optional):
You can customize these parameters if desired:
- Folder structure
- Number of commits
- File name format
- Commit message
- File content 
'''

# ------------------- GitHub Setup ------------------- #
# Authenticate with GitHub using the API key and connect to the specified repository.
g = Github(api_key)
repo = g.get_repo(REPO)

# ------------------- Generate Current Date ------------------- #
# Get the current date in "YYYY-MM-DD" format to organize commits by day.
now = datetime.now()
date = now.strftime("%Y-%m-%d")

# ------------------- File Creation Loop ------------------- #
# Loop to create multiple files for each commit.
for i in range(10):  # Adjust the range if you want more or fewer commits.
    # Define the file path within the repository, using the current date and file number.
    file_path = f"Greenified/{date}/file{i:02}.txt"  # Example: "Greenify/2023-10-20/file00.txt"
    file_content = "Let's make Amazon forest in heatmap."  # Define content for each created file.
    
    try:
        # Create a new file with a commit message in the specified repository.
        repo.create_file(
            path=file_path,             # Path in the repo where the file will be created.
            message="Automated commit for streak.",  # Commit message for tracking.
            content=file_content         # Content to write in the file.
        )
        print(f"Created file: {file_path}")
    except Exception as e:
        # Handle errors if the file creation fails (e.g., duplicate files).
        print(f"Failed to create file: {file_path}. Error: {e}")
