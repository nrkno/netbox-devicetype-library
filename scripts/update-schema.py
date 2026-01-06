import json
import jsondiff
import os
from shutil import copy2
import tempfile
from urllib.request import urlopen, urlretrieve

FILENAME = "generated_schema.json"

releaseData = {}
_releaseURL_ = 'https://api.github.com/repos/netbox-community/netbox/releases/latest'


def gather_release_data():
  global releaseData
  # Gather Latest release JSON data from the GitHub API
  latestRelease = urlopen(_releaseURL_)

  if latestRelease.getcode() == 200:
    print("Successfully retrieved latest release data")
    releaseData = json.loads(latestRelease.read().decode('utf-8'))

    if 'tag_name' not in releaseData:
      print('Error: Could not find tag_name in JSON data')
      releaseData.update({'tag_name': 'unknown'})

    if 'zipball_url' not in releaseData:
      print('FATAL Error: Could not find zipball_url in JSON data')
      exit(1)


def extract_data(releaseTag: str, repo_path: str):
  with tempfile.TemporaryDirectory() as tempdir:
    tmpfile = f'{tempdir}/{FILENAME}'
    urlretrieve(f'https://raw.githubusercontent.com/netbox-community/netbox/{releaseTag}/contrib/generated_schema.json', tmpfile)

    if os.path.isfile(repo_path):
      print("Generated JSON already exists, checking diff.")
      tmpJSON = open(tmpfile, 'r').read()

      # The yaml plugin in vscode needs reference to filename to work, so the id of the remote schema is set to filename
      tmp_id = json.loads(tmpJSON)["$id"]
      tmpJSON = tmpJSON.replace(tmp_id, FILENAME)
      with open(tmpfile, 'w') as file:
        file.write(tmpJSON)

      repoJSON = open(repo_path, 'r').read()
      if jsondiff.diff(tmpJSON, repoJSON):
        print("New JSON data found, updating generated_schema.json")
        copy2(tmpfile, repo_path)
    else:
      print("Generated JSON not found. Copying generated_schema.json")
      copy2(tmpfile, repo_path)


def __init__():
  print("Initializing release data...")
  gather_release_data()

  print("Starting data extract...")
  os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
  repo_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), f'../schema/{FILENAME}'))
  extract_data(releaseData['tag_name'], repo_path)

  print("Completed data extract.")

__init__()
