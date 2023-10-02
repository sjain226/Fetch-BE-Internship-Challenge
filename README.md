# Overview
Built  REST API to keep track of points and transactions like add, spend and balance The APIs are documented below. We use 2 APIs : POST and GET to add and spend the point, and to get balance of points left.

## Summary of API specification
### Endpoint : Add Points
- Path: /add
- Method: POST
- Description: Adds the payer name, points added and timestamp for when the transaction takes place. A successful additon will give a status of code 200.

Example body:
{"payer" : "DANNON", "points" : 5000, "timestamp" : "2020-11-02T14:00:00Z"}

### Endpoint: Spend Points
- Path: /spend
- Method: POST
- Description: Points deducted from a payer based on the oldest transaction timestamp to exist. Succesful spend will respond with status of code 200.
Example body: 
{"points" : 3000}

Example Response:
[
{ "payer": "DANNON", "points": -3000 }}
]

## Rules
the payers points should not go in negative and if the points spent is more than the what payer has in total , a status of code 400 would be displayed with a message saying "user doesn't have enough points.".

### Endpoint : Get Balance
- Path: /balance
- Method: GET
- Description: Displays the points payer has in their account after adding and/or spending points.

Example Response:
{
"DANNON": 2000
}

## Example

```json
{
        {
        "payer": "DANNON",
        "points": 5000,
        "timestamp": "2020-11-02T14:00:00Z"
        }
        
        "/spend"
        [
            { "payer": "DANNON", "points": -3000 }
        ]

        "/balance"
        { "DANNON": 2000}

}
```
Total points: 2000. Added 5000 to DANNON, spent 3000 points, left with 2000 points so the balance shows 2000.

## Running the program 
Requires Flask, virtual env and Postman to be installed.

- Install virtual env using : pip install virtualenv and activate using : source env/bin/activate  (macOS)
- Once in virtualenv, install flask using: pip install flask
- To run on 8000 port, use: flask run -h localhost -p 8000
- Import the project on Postman.

- Once the application is running we can make the following POST requests and GET requests using curl on Postman. Import the commands onto the project file and click send on Postman.

/add: curl -X POST -H "Content-Type: application/json" -d '{"payer": "DANNON", "points": 5000, "timestamp": "2020-11-02T14:00:00Z"}' http://localhost:8000/add
/spend: curl -X POST -H "Content-Type: application/json" -d '{"points": 5000}' http://localhost:8000/spend
/balance: curl http://localhost:8000/balance















