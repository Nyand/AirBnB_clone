<p align="center">
  <img src="https://github.com/Hagos2022/AirBnB_clone/blob/master/assets/hbnb_logo.png" alt="HolbertonBnB logo">
</p>

<h1 align="center">HBnB</h1>
<p align="center">An AirBnB clone Project</p>

---

## Description:

AirBnB is a complete web application, integrating database storage,
a back-end API, and front-end interfacing in a clone of AirBnB.

The project currently implements the back-end console only.

## Classes:

AirBnB utilizes the following classes:

|     | BaseModel | FileStorage | User | State | City | Amenity | Place | Review |
| --- | --------- | ----------- | -----| ----- | -----| ------- | ----- | ------ |
| **PUBLIC INSTANCE ATTRIBUTES** | `id`<br>`created_at`<br>`updated_at` | | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` |
| **PUBLIC INSTANCE METHODS** | `save`<br>`to_dict` | `all`<br>`new`<br>`save`<br>`reload` | "" | "" | "" | "" | "" | "" |
| **PUBLIC CLASS ATTRIBUTES** | | | `email`<br>`password`<br>`first_name`<br>`last_name`| `name` | `state_id`<br>`name` | `name` | `city_id`<br>`user_id`<br>`name`<br>`description`<br>`number_rooms`<br>`number_bathrooms`<br>`max_guest`<br>`price_by_night`<br>`latitude`<br>`longitude`<br>`amenity_ids` | `place_id`<br>`user_id`<br>`text` | 
| **PRIVATE CLASS ATTRIBUTES** | | `file_path`<br>`objects` | | | | | | |

## Storage:

The above classes are handled by the abstracted storage engine defined in the
[FileStorage](./models/engine/file_storage.py) class.

Every time the backend is initialized, AirBnB instantiates an instance of
`FileStorage` called `storage`. The `storage` object is loaded/re-loaded from
any class instances stored in the JSON file `file.json`. As class instances are
created, updated, or deleted, the `storage` object is used to register
corresponding changes in the `file.json`.

## Console:

The console is a command line interpreter that permits management of the backend 
of AirBnB. It can be used to handle and manipulate all classes utilized by
the application (achieved by calls on the `storage` object defined above).

### Using the Console

The AirBnB console can be run both interactively and non-interactively.
To run the console in non-interactive mode, pipe any command(s) into an execution 
of the file `console.py` at the command line.

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
$
```

Alternatively, to use the AirBnB console in interactive mode, run the
file `console.py` by itself:

```
$ ./console.py
```

While running in interactive mode, the console displays a prompt for input:

```
$ ./console.py
(hbnb)
```

To quit the console, enter the command `quit`, or input an EOF signal
(`ctrl-D`).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```

### Console Commands

The AirBnB console supports the following commands:

* **create**
  * Usage: `create <class>`

Creates a new instance of a given class. The class' ID is printed and
the instance is saved to the file `file.json`.

```
$ ./console.py
(hbnb) create BaseModel
3b6ab950-8ee2-466f-99bb-09cf3f5b2eab
(hbnb) quit
$ cat file.json ; echo ""
{"BaseModel.3b6ab950-8ee2-466f-99bb-09cf3f5b2eab": {"id":
"3b6ab950-8ee2-466f-99bb-09cf3f5b2eab", "created_at":
"2023-03-08T12:13:06.605601", "updated_at": "2023-03-08T12:13:06.605608",
"__class__": "BaseModel"}}

```

* **show**
  * Usage: `show <class> <id>` or `<class>.show(<id>)`

Prints the string representation of a class instance based on a given id.

```
$ ./console.py
(hbnb) create User
f641eac7-16d4-4dca-851f-12590d7c8ddd
(hbnb)
(hbnb) show User 1e32232d-5a63-4d92-8092-ac3240b29f46
[User] (f641eac7-16d4-4dca-851f-12590d7c8ddd) {'id': 'f641eac7-16d4-4dca-851f-12
590d7c8ddd', 'created_at': datetime.datetime(2023, 3, 8, 12, 29, 30, 254591),
'updated_at': datetime.datetime(2023, 3, 8, 12, 29, 30, 254599)}
(hbnb)
(hbnb) User.show(f641eac7-16d4-4dca-851f-12590d7c8ddd)
[User] (f641eac7-16d4-4dca-851f-12590d7c8ddd) {'id': 'f641eac7-16d4-4dca-851f-
12590d7c8ddd', 'created_at': datetime.datetime(2023, 3, 8, 12, 29, 30, 254591),
'updated_at': datetime.datetime(2023, 3, 8, 12, 29, 30, 254599)}
(hbnb)
```
* **destroy**
  * Usage: `destroy <class> <id>` or `<class>.destroy(<id>)`

Deletes a class instance based on a given id. The storage file `file.json`
is updated accordingly.

```
$ ./console.py
(hbnb) create State
97a99431-05e7-41a7-abd0-2eddd78a3dbe
(hbnb) create Place
7a02c630-2dc6-49ba-a447-7209b42c2e2b
(hbnb)
(hbnb) destroy State 97a99431-05e7-41a7-abd0-2eddd78a3dbe
(hbnb) Place.destroy(7a02c630-2dc6-49ba-a447-7209b42c2e2b)
(hbnb) quit
$ cat file.json ; echo ""
{}
```

* **all**
  * Usage: `all` or `all <class>` or `<class>.all()`

Prints the string representations of all instances of a given class. If no
class name is provided, the command prints all instances of every class.

```
$ ./console.py
(hbnb) create BaseModel
a28fc3de-8bf8-4d50-9908-ee55ba2b55d1
(hbnb) create BaseModel
35f4e77f-d1b6-4cd6-8e15-100122cc075d
(hbnb) create User
fe25b797-5be4-43ef-a74b-e603ee66a9b0
(hbnb) create User
78073e0e-e652-49bc-a929-596c89de04be
(hbnb)
(hbnb) all BaseModel
["[BaseModel] (c51022f7-a3ab-4e7e-82a4-893ef08be813) {'id': 'c51022f7-a3ab-4e7e-
82a4-893ef08be813', 'created_at': datetime.datetime(2023, 3, 8, 9, 47, 39, 7783
64), 'updated_at': datetime.datetime(2023, 3, 8, 9, 47, 39, 778374)}",
"[BaseModel] (3b6ab950-8ee2-466f-99bb-09cf3f5b2eab) {'id': '3b6ab950-8ee2-466f
-99bb-09cf3f5b2eab', 'created_at': datetime.datetime(2023, 3, 8, 12, 13, 6,
605601), 'updated_at': datetime.datetime(2023, 3, 8, 12, 13, 6, 605608)}",
"[BaseModel] (a28fc3de-8bf8-4d50-9908-ee55ba2b55d1) {'id': 'a28fc3de-8bf8-4d50-
9908-ee55ba2b55d1', 'created_at': datetime.datetime(2023, 3, 8, 12, 52, 17,
820860), 'updated_at': datetime.datetime(2023, 3, 8, 12, 52, 17, 820867)}",
"[BaseModel] (35f4e77f-d1b6-4cd6-8e15-100122cc075d) {'id': '35f4e77f-d1b6-4cd6-
8e15-100122cc075d', 'created_at': datetime.datetime(2023, 3, 8, 12, 53, 24,
216947), 'updated_at': datetime.datetime(2023, 3, 8, 12, 53, 24, 216956)}"]
(hbnb)
(hbnb) User.all()
["[User] (f641eac7-16d4-4dca-851f-12590d7c8ddd) {'id': 'f641eac7-16d4-4dca-851f
-12590d7c8ddd', 'created_at': datetime.datetime(2023, 3, 8, 12, 29, 30, 254591),
 'updated_at': datetime.datetime(2023, 3, 8, 12, 29, 30, 254599)}", "[User]
(fe25b797-5be4-43ef-a74b-e603ee66a9b0) {'id': 'fe25b797-5be4-43ef-a74b-e603ee66a
9b0', 'created_at': datetime.datetime(2023, 3, 8, 12, 54, 58, 121355), 'updated
_at': datetime.datetime(2023, 3, 8, 12, 54, 58, 121363)}", "[User] (78073e0e-
e652-49bc-a929-596c89de04be) {'id': '78073e0e-e652-49bc-a929-596c89de04be',
'created_at': datetime.datetime(2023, 3, 8, 13, 5, 9, 178703), 'updated_at':
datetime.datetime(2023, 3, 8, 13, 5, 9, 178710)}"]
(hbnb)
(hbnb) all
["[BaseModel] (c51022f7-a3ab-4e7e-82a4-893ef08be813) {'id': 'c51022f7-a3ab-4e7e-
82a4-893ef08be813', 'created_at': datetime.datetime(2023, 3, 8, 9, 47, 39,
778364), 'updated_at': datetime.datetime(2023, 3, 8, 9, 47, 39, 778374)}",
"[BaseModel] (3b6ab950-8ee2-466f-99bb-09cf3f5b2eab) {'id': '3b6ab950-8ee2-466f-
99bb-09cf3f5b2eab', 'created_at': datetime.datetime(2023, 3, 8, 12, 13, 6,605601
), 'updated_at': datetime.datetime(2023, 3, 8, 12, 13, 6, 605608)}", "[User]
(f641eac7-16d4-4dca-851f-12590d7c8ddd) {'id': 'f641eac7-16d4-4dca-851f-12590d7c
8ddd', 'created_at': datetime.datetime(2023, 3, 8, 12, 29, 30, 254591), 'updated
_at': datetime.datetime(2023, 3, 8, 12, 29, 30, 254599)}", "[BaseModel]
(a28fc3de-8bf8-4d50-9908-ee55ba2b55d1) {'id': 'a28fc3de-8bf8-4d50-9908-ee55ba2b
55d1', 'created_at': datetime.datetime(2023, 3, 8, 12, 52, 17, 820860), 'updated
_at': datetime.datetime(2023, 3, 8, 12, 52, 17, 820867)}", "[BaseModel]
(35f4e77f-d1b6-4cd6-8e15-100122cc075d) {'id': '35f4e77f-d1b6-4cd6-8e15-100122cc0
75d', 'created_at': datetime.datetime(2023, 3, 8, 12, 53, 24, 216947), 'updated
_at': datetime.datetime(2023, 3, 8, 12, 53, 24, 216956)}", "[User] (fe25b797-5be
4-43ef-a74b-e603ee66a9b0) {'id': 'fe25b797-5be4-43ef-a74b-e603ee66a9b0', 'created
_at': datetime.datetime(2023, 3, 8, 12, 54, 58, 121355), 'updated_at': datetime.
datetime(2023, 3, 8, 12, 54, 58, 121363)}", "[User] (78073e0e-e652-49bc-a929-596
c89de04be) {'id': '78073e0e-e652-49bc-a929-596c89de04be', 'created_at': datetime
.datetime(2023, 3, 8, 13, 5, 9, 178703), 'updated_at': datetime.datetime(2023,
3, 8, 13, 5, 9, 178710)}"]
(hbnb)
```

* **count**
  * Usage: `count <class>` or `<class>.count()`

Retrieves the number of instances of a given class.

```
$ ./console.py
(hbnb) create Place
c24174ab-3310-49ac-b6d4-13f1e6b3ccb5
(hbnb) create Place
c6ad2490-c925-441f-b118-cb80863333e3
(hbnb) create City
caec6947-ae3e-4dca-a4ca-38cda4221e86
(hbnb)
(hbnb) count Place
2
(hbnb) City.count()
1
(hbnb)
```

* **update**
  * Usage: `update <class> <id> <attribute name> "<attribute value>"` or
`<class>.update(<id>, <attribute name>, <attribute value>)` or `<class>.update(
<id>, <attribute dictionary>)`.

Updates a class instance based on a given id with a given key/value attribute
pair or dictionary of attribute pairs. If `update` is called with a single
key/value attribute pair, only "simple" attributes can be updated (ie. not
`id`, `created_at`, and `updated_at`). However, any attribute can be updated by
providing a dictionary.

```
$ ./console.py
(hbnb) create User
c97fdfd4-691a-420e-9844-6cc7814178a9
(hbnb)
(hbnb) update User c97fdfd4-691a-420e-9844-6cc7814178a9 first_name "AirBnB"
(hbnb) show User c97fdfd4-691a-420e-9844-6cc7814178a9
[User] (c97fdfd4-691a-420e-9844-6cc7814178a9) {'id': 'c97fdfd4-691a-420e-9844-
6cc7814178a9', 'created_at': datetime.datetime(2023, 3, 8, 13, 43, 3, 658005),
'updated_at': datetime.datetime(2023, 3, 8, 13, 43, 3, 658012), 'first_name':
'AirBnB'}
(hbnb)
(hbnb) User.update(c97fdfd4-691a-420e-9844-6cc7814178a9, address, "98 Mission St")
(hbnb) User.show(c97fdfd4-691a-420e-9844-6cc7814178a9)
[User] (c97fdfd4-691a-420e-9844-6cc7814178a9) {'id': 'c97fdfd4-691a-420e-9844-
6cc7814178a9', 'created_at': datetime.datetime(2023, 3, 8, 13, 43, 3, 658005),
'updated_at': datetime.datetime(2023, 3, 8, 13, 43, 3, 658012), 'first_name':
'AirBnB', 'address': '98 Mission St'}
(hbnb)
```

## Testing:

Unittests for the AirBnB project are defined in the [tests](./tests)
folder. To run the entire test suite simultaneously, execute the following command:

```
$ python3 unittest -m discover tests
```

Alternatively, you can specify a single test file to run at a time:

```
$ python3 -m unittest tests/test_console.py
```
