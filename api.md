# API Resource chart

|Resource|Address|Protocol|Params|Response +Status code|
|---|---|---|---|---|
|Register user|/register|POST|username, password :string| 200 OK|
|Store sentence|/store|POST|username, password,sentence :string|200 OK, 301 out of tokens,302 Invalid username or password|
|Retrieve sentence|/get|GET|username, password :string|200 OK, 301 out of tokens,302 Invalid username or password|
||||||