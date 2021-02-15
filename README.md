Instruction
----------------------

# 1. Question A
## 1.1. The question
Write a program that will generate four (4) types of printable random objects and store them in a single file, each object will be separated by a ",".  These are the 4 objects: alphabetical strings, real numbers, integers, alphanumerics. The alphanumerics should contain a random number of spaces before and after it (not exceeding 10 spaces). The output should be 10MB in size.

Sample extracted output:

hisadfnnasd, 126263, assfdgsga12348fas, 13123.123, 
lizierdjfklaasf, 123192u3kjwekhf, 89181811238,122, 
nmarcysfa900jkifh  , 3.781, 2.11, ....

## 1.2. Solution:
- File: __question-a.py__
- Run: 
```Python
python question-a.py
```

# 2. Question B
## 2.1. The question
Create a program that will read the generated file above and print to the console the object and its type. Spaces before and after the alphanumeric object must be stripped.

Sample output:

youruasdifafasd - alphabetical strings
127371237 - integer
asdfka12348fas - alphanumeric
13123.123 - real numbers
asjdfklasdjfklaasf - alphabetical strings
123192u3kjwekhf - alphanumeric

## 2.2. Solution
- File: __challenge_b.py__
- Run: 
```Python
python question-b.py
```

# 3. question C
## 3.1. The question
Dockerize question B. Write a docker file so that it reads the output from question A as an Input. Once this container is started,  the program in challenge B is executed to process this file. The output should be saved in a file and should be exposed to the Docker host machine.

## 3.2. Solution
- File: __Dockerfile__
- Build docker
```dockerfile
docker build -t omnilytics:latest -f ./Dockerfile

```
- Run docker:
```dockerfile
docker run omnilytics
```