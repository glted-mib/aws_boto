# pull this code/unzip somewhere

# install miniconda (if you don't have python)

# open anaconda powershell prompt

# run python
python --version

# add to path if problem running python (environment variables from windows search)
# path=c:\Users\Yourlanid\miniconda3
# https://stackoverflow.com/questions/65348890/python-was-not-found-run-without-arguments-to-install-from-the-microsoft-store

# create conda environment
conda create --name aws_s3

#activate your new environment
conda activate environment

#install python aws boto package to communicate with s3
conda install --file requirements.txt

#create s3 sync directory on machine

#install aws comman line interface tool
# https://anaconda.org/conda-forge/awscli
conda install -c conda-forge awscli

#create a aws cli profile
https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html
aws configure --profile-name mib_profile
aws_access_key_id = YOUR_KEY
aws_secret_access_key = YOUR_SECRET
region=us-east-1




