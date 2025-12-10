Example of manual approval flow

but it also gives example of creating a workpool with ttl for job pods life. [[simple-ttl-job-template.yaml]]

## Create a new workpool

```
prefect work-pool create simple-ttl-workpool --type kubernetes --base-job-template simple-ttl-job-template.json --overwrite
```

## Create a worker for the pool

```
helm install prefect-ttl-worker prefect/prefect-worker  -f ./worker-values.yaml
```

## inspect the workpool

```
prefect work-pool inspect schoolinfo-pool --output json > working-workpool-template.json
```

## inspect deployments

```
prefect deployment inspect container-flow/default --output json > container-deployment-config.json
```

