There are multiple ways to create a prefect job and deploy it. 
Here are some ways to do it

## 1. files directly in the root of the github
my_flow.py
prefect.yaml
requirements.txt

Here the prefect.yaml defines the deployment to explicitly get the code from github and do the setup so that it is available in the pod.
For this you have create block -> github credentials in prefect using the github token generated from the github website and use that in the prefect.yaml file.

### install the github prefect plugin for blocks
First on you local machine (where you run the prefect client) install the prefect-github plugin.
```
pip install prefect_github
```
OR
```
pip install "prefect[github]"
```
If using uv make sure to use `uv pip` instead of just pip.

### register the plugin
```
prefect block register -m prefect_github
```

This will help you setup github credentials in the prefect UI (also can be done from cli or python code.)

Goto http://prefect-server:4200 (eg. http://localhost:4200)

then Blocks -> [+] -> GitHub Credentials

Block Name : 'my-private-repo-creds'
Token: 'your github token'

### Make sure to commit the git repo to github
git commit -m 
git push

### Register the deployment

`prefect deploy`

In the cli options select the flow name. Select 'no' 'n' for scheduling as we don't want to schedule

### Run the deployment

```
prefect deployment run 'simple-k8s-flow/my-k8s-deployment'
```


## 2. flow file inside a folder in the project.
Note that when running the `prefect deploy` we will have to run it from the root of the project and give the right path of the flow file in the prefect.yaml file.
since this repo already has prefect.yaml file in the root location, so I am explicitly giving path of custom prefect.yaml for the flow1 like below

```
prefect deploy --prefect-file flows/flow1/prefect.yaml
```
Note in the flows/flow1/prefect.yaml the entry point is : ` entrypoint: flows/flow1/flow1.py:simple_k8s_flow `
which is relative path of flow to the repo.

then run as usual 

```
prefect deployment run 'simple-k8s-flow/my-k8s-deployment'
```








