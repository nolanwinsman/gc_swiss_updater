# swiss_release_downloader.py

import os
import requests

class GitHubReleaseDownloader:
    """
    GitHubReleaseDownloader class provides methods for downloading the latest release from a GitHub repository.
    """

    @staticmethod
    def download_latest_release(repo_owner, repo_name, target_dir, file_extension):
        """
        Downloads the latest release from the specified GitHub repository with the specified file extension.
        Returns the path to the downloaded file.
        """
        response = requests.get(f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest")
        release_info = response.json()

        assets = release_info['assets']
        release_asset = next((asset for asset in assets if asset['name'].endswith(file_extension)), None)

        if release_asset is None:
            print(f"No file with '{file_extension}' extension found in the latest release.")
            return None

        asset_url = release_asset['browser_download_url']
        asset_name = os.path.basename(asset_url)
        asset_path = os.path.join(target_dir, asset_name)

        os.makedirs(target_dir, exist_ok=True)  # Create the target directory if it doesn't exist

        print(f"Downloading {asset_name}...")
        with open(asset_path, 'wb') as f:
            asset_response = requests.get(asset_url)
            f.write(asset_response.content)

        print(f"Downloaded {asset_name} to {asset_path}")
        return asset_path
