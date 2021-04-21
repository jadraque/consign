# Cloud Storage

How to store files on the cloud with Consign

## Quickstart

Eager to get started? This page gives a good introduction in how to get started
with cloud storage on Consign.

First, make sure that:

- Consign is installed.
- Consign is up-to-date.

Let’s get started with some simple examples.


## Cloud Provider

At the moment Consign only supports Microsoft Azure cloud.

Check the following provider table to know the valid `provider` values:

| Cloud provider    | Param value |
| ----------------- | ----------- |
| Microsoft Azure   | azure       |


## Authentication

Though the different cloud providers allow a wide range of authentication
methods, at the moment Consign only supports `connection strings`.

Read your cloud provider's documentation to know how to obtain the valid
`connection string` to connect to your account.

You can find [Azure's here](https://pypi.org/project/azure-storage-blob/)


## Store a Blob

Storing a blob with Consign is very simple.

Begin by importing the Consign module:

``` 
import consign
``` 

Now, let’s try to store some dummy data into a text file.

``` 
data = {
        "Asia": 4581757408,
        "Africa": 1216130000,
        "Europe": 738849000,
        "North America": 579024000,
        "South America": 422535000,
        "Oceania": 38304000,
        "Antarctica": 1106
    }
path = "./population_by_continent.json"
``` 

For instance, let's say you have proudly built the previous Python's dictionary
with Wikipedia's population by continent data, and now you want to store it
into a blob in Microsoft Azure Storage:

``` 
consign.blob(
    data,
    path,
    provider='azure',
    connection_string=connection_string,
    container_name=container_name
)
``` 

Under the hood, Consign makes a number of validations such as your permissions
to write in the container, that both paths and container names are valid, and
data has a valid format.

That’s all well and good, but it’s also only the start of what Consign can do.

## Blobs

As seen before, Consign makes it simple to store blobs.

``` 
consign.blob(
    data,
    path,
    provider='azure',
    connection_string=connection_string,
    container=container
)
```

Under the hood, Consign verifies that:

- Your account has permission to write in the provided `container`,
- The `container` exists,
- Both `container` and the blob's `path` have valid names,
- `data` has a valid format,

| Params            | Mandatory | Type |  Definition                                  |
| ----------------- | --------- | ---- | -------------------------------------------- |
| data              | yes       | lst  |  Data to be printed into the blob            |
| path              | yes       | str  |  Blob name                                   |
| provider          | yes       | str  |  The name of your cloud provider (see below) |
| connection_string | yes       | str  |  Your account keys to connect to your cloud  |
| container         | yes       | str  |  The name of your blobs container            |


## Tables

Table storage works pretty similarly to Blob storage in Consign.

``` 
consign.table(
    data,
    path,
    provider='azure',
    connection_string=connection_string
)
```

Under the hood, Consign verifies that:

- Your account has permission to write in the provided `path`,
- The table's `path` is valid,
- `data` has a valid format,

| Params            | Mandatory | Type |  Definition                                  |
| ----------------- | --------- | ---- | -------------------------------------------- |
| data              | yes       | lst  |  Data to be printed into the blob            |
| path              | yes       | str  |  Blob name                                   |
| provider          | yes       | str  |  The name of your cloud provider (see below) |
| connection_string | yes       | str  |  Your account keys to connect to your cloud  |
