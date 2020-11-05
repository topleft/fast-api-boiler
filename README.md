# Fast Api Boiler Plate

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
$ docker-compose exec app python -m pytest /usr/app -p no:warnings --cov=/usr/app --cov-config=/usr/app/.coveragerc
```

**Lint:**
```sh
$ docker-compose exec app flake8 --max-line-length 120 --inline-quotes=\" ./app/.
```


**Todo:**

- Configure Production build
- Integrate with circleCI
