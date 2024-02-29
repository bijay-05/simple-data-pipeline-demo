### Run the frontend

Run following commands from root directory of frontend

```
$ npm install

$ npm run dev

```


### Run the backend

Run the following commands from root directory of backend

```
$ npm install -g yarn

$ yarn    # install all dependencies

$ yarn migration:make todo(db_name)

$ yarn migrate   # after adding commands in migration file under src/db/migrations/blah-blahmigration.ts

$ yarn start   # run the backend server
```
