### Task 2

How would you approach test automation of an HTTP API of some service? 

Choose a service from this list ​https://github.com/toddmotto/public-apis ​or any other of your choice. It is better to pick one without authorization as it is easier to test.
Document several test cases. Implement one or two automated tests based on the test cases. Write the tests as if they were a part of a real project.

----

##### Choose service

According to task let's choose something without auth and with ability to create test data (because it often require to prepare state for test cases)

For this requirements perfectly match [JSONPlaceholder](http://jsonplaceholder.typicode.com/) from [Test Data](https://github.com/public-apis/public-apis#test-data) section


##### Test Cases
Functional TestCases
* /posts
    * positive cases
        * [x] create post, check it exist
        * [x] get existed post
        * [ ] get all posts (paging)
        * [x] delete post, check it deleted
        * [ ] modify post ...
    * negative cases
        * [x] get deleted post
        * [ ] get unexist post
        * [ ] delete unexist post
        * [ ] requests with wrong format
* ...

Non-functional testcases
- ...


##### Implementation Details

For this small tests demo we will require only two dependencies: `requests` and `pytest`
To install them locally we will run:
```sh
$ pip install --upgrade -r requirements.txt
```

I [freezed deps versions](requirements.txt) in requirements.txt for deterministic tests behaviour, we don't need surprises when new version of some deps will be incompatible with others or their behaviour will unexpectedly changed. 


For current tests we will require 2 components: tests themselves and client which will simplify making requests each time.

`Client` class providing us simple DSL for making requests to endpoints (like `create_post`, `delete_post` and so on), encapsulating low-level requests logic (headers, urls, params and so on). For simplifying readability it would be good to extract requests and responses with simple DTO/DataClasses objects.

`test_posts` contains tests for desired domain (in our case for Posts). For reusing common code for prepare test states I used `fixtures` functionality. 