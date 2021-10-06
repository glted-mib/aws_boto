import os
import boto3

local_dir = r"c:\git\s3\glted-mib"
session = boto3.session.Session(profile_name='mib_profile')
creds = session.get_credentials()
s3 = session.resource('s3')
mib_staged_bucket = s3.Bucket('glted-mib')


def upload_file(local, remote):
    print("{} -> {}".format(local, remote))
    try:
        mib_staged_bucket.upload_file(local, remote)
    except Exception as e:
        raise e


def main():
    for a, _, c in os.walk(local_dir):
        print(a)
        if r"scenarios\Intermediate" in a:
            for f in c:
                if write:
                    local_file = os.path.join(a, f)
                    remote_file = local_file.lstrip(local_dir).replace("\\", "/")
                    print(local_file)
                    print(remote_file)
                    upload_file(local_file, remote_file)

main()
