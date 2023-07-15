# Repository Updater

This script allows you to update or clone a list of repositories defined in `repositories.txt`. The script checks each repository, and if it exists locally, it pulls the latest changes. If it doesn't exist, it clones the repository.

## Usage

1. Create a file named `repositories.txt` containing the URLs of the repositories, one URL per line.

   Example `repositories.txt`:
   ```plaintext
   https://github.com/username/repo1.git
   https://github.com/username/repo2.git
   https://github.com/username/repo3.git

