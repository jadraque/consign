# Local File Storage

How to store files locally with Consign

## Quickstart

Eager to get started? This page gives a good introduction in how to get started
with Consign.

First, make sure that:

- Consign is installed.
- Consign is up-to-date.

Let’s get started with some simple examples.

## Store a local file

Storing a file with Consign is very simple.

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
into a JSON file in your current path:

``` 
consign.json(data, path)
``` 

Under the hood, Consign makes a number of validations such as your permissions
to write in the given path or verifying that data has a valid JSON format.

That’s all well and good, but it’s also only the start of what Consign can do.

## CSV Files

As seen before, Consign makes it simple to store text files.

``` 
consign.csv(data, path)
```

Under the hood, Consign verifies that:

- The `path` exists,
- You have proper permissions to write into the `path`,
- `data` has a valid CSV format,
- The `delimiter` (read more below) is not used inside of any of the `data`
  values, to prevent displaced columns.
- Windows does not add an extra carriage return (a.k.a. a blank row) after each
  one of your CSV rows.

| Params     | Mandatory | Type | Default | Definition                                   |
| ---------- | --------- | ---- | ------- |--------------------------------------------- |
| data       | yes       | lst  |         | Matrix to be printed into the CSV file       |
| path       | yes       | str  |         | Local path to the CSV file                   |
| delimiter  | no        | str  | ,       | Character to use as value delimiter          |
| update     | no        | boo  | False   | True to update previous file                 |
| initialize | no        | boo  | False   | True to initialize path if it does not exist |

### File Update

By default, Consign will automatically overwrite any previous CSV found in your
given path.

If you don't want it to be overwritten, just set `update=True` to ensure that
the content inside of your `data` variable gets appended at the end of the file.

``` 
consign.csv(data, path, update=True)
```

### Custom Delimiter

By default, Consign uses commas (',') as value delimiter character.

If you want to customize the delimiter character, you can do so by passing the
`delimiter` param in your call:

``` 
consign.csv(data, path, delimiter=',')
```

### Path Initialization

By default, if you try to print data into a path that does not exist, Consign
will raise an InvalidPath exception.

To modify this behaviour you can ask Consign to automatically create the path
with the `initialize` param in your call:

``` 
consign.csv(data, path, initialize=True)
```


## JSON files

As seen before, Consign makes it simple to store text files.

``` 
consign.json(data, path)
```

Under the hood, Consign verifies that:

- The `path` exists,
- You have proper permissions to write into the `path`,
- `data` has a valid JSON format,

| Params     | Mandatory | Type | Default | Definition                                   |
| ---------- | --------- | ---- | ------- | -------------------------------------------- |
| data       | yes       | dic  |         | Dictionary to be printed into the JSON file  |
| path       | yes       | str  |         | Local path to the CSV file                   |
| update     | no        | boo  | False   | True to update previous file                 |
| initialize | no        | boo  | False   | True to initialize path if it does not exist |

### File Update

By default, Consign will automatically overwrite any previous JSON found in
your provided path.

If you don't want it to be overwritten, just set `update=True` to ensure that
the content inside of your `data` variable gets appended at the end of the file.

``` 
consign.json(data, path, update=True)
```

### Path Initialization

By default, if you try to print data into a path that does not exist, Consign
will raise an InvalidPath exception.

To modify this behaviour you can ask Consign to automatically create the path
with the `initialize` param in your call:

``` 
consign.json(data, path, initialize=True)
```
​
## Other Text Files

Likely, Consign supports storage in HTML and TXT format with similar use:

``` 
consign.html(data, path)
consign.txt(data, path)
```

## Binary Files

Consign also support binary files, such as PDFs and images, with similar naming
as in the other text files:

``` 
consign.html(data, path)
consign.txt(data, path)
```

The only difference being that the `data` variable should be of binary type.
