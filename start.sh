docker build --tag ambrosia-apollo-api .
docker run --name ambrosia-apollo-api -d -p 4000:5000 ambrosia-apollo-api