# Consign: data storage for humans

Consign is a simple library to handle data storage for Python.

## Intro

Consign handles all the validation steps needed to store data in Python, from
basic text file in local storage, up to large datasets in databases.

## Check this out

Do you want to write a CSV file?

```
consign.csv(data, path)
``` 

What about a JSON file?

``` 
consign.json(data, path)
``` 

What if I want to write to Azure Blobs or any other cloud blob storage?

``` 
consign.blob(
        data,
        path,
        provider='azure',
        connection_string=connection_string,
        container_name=container_name
    )
``` 

Under the hood, Consign validates your permissions and data format, and gives
you rich feedback on any issue that may arise, thanks to its carefully designed
exception module.
