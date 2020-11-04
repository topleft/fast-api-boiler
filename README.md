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
**Migrate DB:**
```sh
$ cd project/db && sh scripts/migrate_db.sh
```

**Apply Migrations:**
```sh
$ cd project/db && sh scripts/upgrade_db.sh
```

**Test:**
```sh
$ docker-compose exec app pytest ./app
```

