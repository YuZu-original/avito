<h1 align="center">Avito<br>"Django App"</h1>

## API

| URL                         | methods      | description                                 |
|-----------------------------|--------------|---------------------------------------------|
| **`cat/`**                  | **`GET`**    | get all categories                          |
| **`cat/<id>/`**             | **`GET`**    | get detail information about category by id |
| **`cat/create/`**           | **`POST`**   | add new category                            |
| **`cat/<id>/update/`**      | **`PATCH`**  | update category's info by id                |
| **`cat/<id>/delete/`**      | **`DELETE`** | delete category by id                       |
| **`ad/`**                   | **`GET`**    | get all ads                                 |
| **`ad/<id>/`**              | **`GET`**    | get detail information about ad by id       |
| **`ad/create/`**            | **`POST`**   | add new ad                                  |
| **`ad/<id>/update/`**       | **`PATCH`**  | update ad's info by id                      |
| **`ad/<id>/delete/`**       | **`DELETE`** | delete ad by id                             |
| **`ad/<id>/upload_image/`** | **`POST`**   | upload image to ad by id                    |
| **`user/`**                 | **`GET`**    | get all users                               |
| **`user/<id>/`**            | **`GET`**    | get detail information about user by id     |
| **`user/create/`**          | **`POST`**   | add new user                                |
| **`user/<id>/update/`**     | **`PATCH`**  | update user's info by id                    |
| **`user/<id>/delete/`**     | **`DELETE`** | delete user by id                           |
| **`location/`**             | **`GET`**    | get all locations                           |
| **`location/<id>/`**        | **`GET`**    | get detail information about location by id |
| **`location/`**             | **`POST`**   | add new location                            |
| **`location/<id>/`**        | **`PATCH`**  | update location's info by id                |
| **`location/<id>/`**        | **`DELETE`** | delete location by id                       |
| **`media/`**                | **`GET`**    | load (uploaded) image by name               |

> made by YuZu :D