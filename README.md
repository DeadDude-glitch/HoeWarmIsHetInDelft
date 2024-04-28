# HoeWarmIsHetInDelft



## Task Description

1. Create a Python script called ‘HoeWarmIsHetInDelft.py’ that retrieves from [weerindelft site](http://www.weerindelft.nl/) the current temperature in Delft and prints it to standard output, **rounded** to degrees Celsius. Example expected output: `18 degrees Celsius`
2. Write an appropriate dockerfile to containerize the script developed in point 1
3. Write a simple pipeline on [GitLab](https://www.gitlab.com) that builds the container above and then executes it.

>We’ll review the code based on clarity and correctness. It is important for the code to be robust, run correctly in a pipeline environment and to be easily troubleshootable by other DevOps engineers.

## TODO
this is a functional programming approach to the solution. for an OOP approach check the other branch. 

- [X] Python script
    - [X] Deeply understand the website functionality
    - [ ] Try to limit the usage to only Built-in python modules
    - [X] Handle errors and add debugging feature  
    - [X] Develop testing scripts 
- [X] Docker Image
    - [X] Optimize the layers order for caching
- [X] GitLab Pipeline
    - [X] Constantly update a remote docker repository 
    - [X] Separate the build from the deployment stage
- [X] Add a GitHub repo

