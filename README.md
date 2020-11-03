# Up Ping - Fast Api

A project created by Orchestrated Energy to get started in GCP.

# Quick Start Local Development

**Start up the app:**
```sh
$ docker-compose up -d
```

**Stop the app:**
```sh
$ docker-compose down
```

**Lint and Test:**
```sh
$ sh ./docker_test.sh
```

**DB:**


# CI and Deployment

**On Commit (any branch except `master`)**:
- Tests are run
- docker image is built
- `terraform plan` is run

**On merge to `master`**:
- docker image is built and pushed to registry
- `terraform apply` is run and image is deployed to `dev`

**On Tag**:
- most recent docker image* is re-tagged
- image is deployed to `stg`

\* This is the most recent image built from what ever branch you are tagging
