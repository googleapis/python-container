import os

import quickstart

PROJECT_ID = os.environ["GOOGLE_CLOUD_PROJECT"]
ZONE = "us-central1-b"


def test_list_models(capsys: object) -> None:
    outputPrefix = "There were "
    outputSuffix = f" clusters in {ZONE} for project {PROJECT_ID}."

    quickstart.list_clusters(PROJECT_ID, ZONE)
    out, _ = capsys.readouterr()

    '''
    Typical output looks as follows:

      There were 3 clusters in us-central1-b for project test-project.
       - cluster1
       - cluster2
       - cluster3

    Split array by '\n'
        [
            "There were 3 clusters in us-central1-b for project test-project.",
            "- cluster1",
            "- cluster2",
            "- cluster3",
            "",
        ]
    '''
    outLines = out.split("\n")
    firstLine = outLines[0]
    firstLine = firstLine.replace(outputPrefix, "")
    firstLine = firstLine.replace(outputSuffix, "")
    clusterCount = int(firstLine)   # get the cluster count in the first line

    assert outputSuffix in out
    assert clusterCount == len(outLines) - 2
