# aws_boto

Our AWS buckets for bioinformatic data storage are for glted-mib (active projects) and glted-mib-glacier (archived projects). This repo contains python, R and command line access information to push and pull data from these buckets. We have common credentials (a shared user/key) that allow us to access the bucket without an aws account. 

The AWS software development kit for cloud access is the python-based [boto3](https://aws.amazon.com/sdk-for-python/). The S3 buckets are managed using command line tools using this boto library. We can use python and R libraries to wrap that command line interface with the code in this repo, but note that you can also interact with the buckets from the command line without using this code. This python library can be accessed by R using the [reticulate](https://mraess.rbind.io/2020/01/python-boto3-reticulate-r/) package, however, you still must have a python environment on your machine with boto3 installed as R just accesses the python library.

We will organize active project files within the glted-mib bucket in separate folders for storage purposes. Push and pull data to relevant subdirectories during the active life of a project.

For archival storage we have a separate bucket, glted-mib-glacier. Essentially upload data to be archived in this bucket, and after 30 days (to allow time for verification) the data will be moved to a Glacier vault. Glacier storage is cheaper than regular S3 storage but it takes a bit more time to retrieve the data when access is needed. The glted-mib-glacier bucket uses the same credentials as the glted-mib bucket.

We share the access credentials separately from this repo. We (of course) should not push the credentials to github repos or otherwise make them public. If the keys get compromised then we will get new ones.
