tutorial source : https://docs.prefect.io/v3/how-to-guides/deployment_infra/kubernetes

See this to find how to setup the kubernetes cluster first : https://github.com/nitirajrathore/kubernetes-demo/blob/main/prefect-cluster/commands.md

In this example we have created the docker image using prefect's deploy command itself.
In the other example called container_flow will separately create the docker image and use it.

Create the docker file automatically and docker image and the push it to the dockerreg server
And also create and register the deployment, this will only deploy `hello/default` flow

export the image nam

```

```

```
prefect deploy -n hello/default --prefect-file flows/kubernetes-container-example/prefect.yaml --pool kubernetes-pool

```

deploy all flows
```
prefect deploy --all --prefect-file flows/kubernetes-container-example/prefect.yaml --pool kubernetes-pool

```


Run one of the flow of the deployment

```
prefect deployment run 'hello/default'
```




