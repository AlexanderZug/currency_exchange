## Currency Exchange Rates

This project fetches the latest exchange rates for US Dollars using data from the Central Bank of Russia. 
The data is updated every two hours.

### How to run

1. Clone the repository
```
    git clone https://github.com/AlexanderZug/currency_exchange.git
```
- You can specify enviroment variables in the .env file. 
As example, you can use the .env.example file. 
But it is not necessary for the project to run.

2. Navigate to the project directory.
```
    cd currency-exchange
```

3. Start Docker and run the following command:
```
    docker-compose up --build
```
- If needed, run the command with root privileges:
```
    sudo docker-compose up --build
```

4. Open the browser and go to  http://localhost:8000/get-current-usd/

### Notes

- The exchange rates are updated every two hours.
- The project uses data from the Central Bank of Russia.
- For Docker commands, make sure Docker is installed and running on your machine.
