
This program was tested in Solus linux and Docker version 18.09.3-ce.
PostgresSQL docker image was used here as a database server.

To run the script ,go to repository root directory and run this command in the terminal

chmod u+x run.sh
./run.sh

!!!!! Note - The first python script(init_review.py)  that load the review data from the json file  takes more than 20 minutes.

The file structure of this repo is given below:

.
├── clean.sh
├── output_unique_reviewers.txt
├── output_user_more_than_5_reviews.txt
├── postgres_docker
│   ├── Dockerfile
│   ├── init.sql
│   └── run.sh
├── python_test
│   ├── database.py
│   ├── data.json
│   ├── Dockerfile
│   ├── helper.py
│   ├── init_review.py
│   ├── init_userinfo.py
│   ├── n_reviewers_query.py
│   ├── program.sh
│   ├── reviewers_twitter.py
│   ├── review.py
│   ├── review_table.py
│   ├── run.sh
│   ├── test_reviews_table.py
│   ├── twitter_api.py
│   ├── unique_reviewers.py
│   └── user_info_table.py
├── README.md
└── run.sh

Here i am running two containers , one is for postgres server and the other is for running all the python scripts.

A brief discussion of the files are given below:

./clean.sh = automates the cleaning proocess of the container and images.
./output_unique_reviewers.txt = output file.
./output_user_more_than_5_reviews.txt = outputfile.

./postgres_docker = The dockerfiles  for postgres server.
./postgres_docker/Dockerfile = Dockerfile
./postgres_docker/init.sql = Postgres Docker image uses this file for creating the tables when the image is created.
./postgres_docker/run.sh  = used by ./run.sh for creating postgres container.

./python_test = all the python codes
./python_test/database.py  = code for connecting to the database.
./python_test/data.json = json file given for the test.
./python_test/Dockerfile = the Dockerfile for python container.
./python_test/helper.py = This a hack i wrote to the the postgres server address in the python container after getting linked.
./python_test/init_reviews.py  = Loads the reviews from json to postgres.Note it takes more than 20 minutes.
./python_test/init_userinfo.py = This code is written to load the twitter user data to postgres database.This code is not tested.There was
problem getting  the API key for twitter app.As of 8th April 2019 , after you requested a app in twitter, twitter will review your reason for 
creating an app.At the time i was coding this , i did not get a reply.
./python_test/n_reviewers_query.py = gets the user with more than 'n' reviews.
./python_test/review.py = The python object that has the same data as the reviews table in database except 'id'.
./python_test/review_table.py = All the database operation function for the review  table are given here.
./python_test/run.sh  = used by ./run.sh for creating python container
./python_test/test_reviews_table.py = test script for review table operation.
./python_test/twitter_api.py  = For connecting  to twitter api  and getting the user data.(Not tested.)
./python_test/unique_reviewers.py = to get the unique reviewers count.
./python_test/user_info_table.py = All the operation for the user info table are given here.


