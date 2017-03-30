# jsonify

A python script to convert csv to json array

CSV structure should be formatted as such:

KEY1, KEY2, KEY3, KEY4

v11,v12,v13,v14

v21,v22,v23,v24


### Usage


#### student.csv

student,age

Nitesh,12

Ikram,9

Raman,15

Sunny,11


  ### Usage #1


 ```
 $ python3 jsonify.py student.csv[filename]
 ```
 

 ```
 $ {
   "students":[
      {
         "student":"Nitesh",
         "age":"12"
      },
      {
         "student":"Ikram",
         "age":"9"
      },
      {
         "student":"Raman",
         "age":"15"
      },
      {
         "student":"Sunny",
         "age":"11"
      }
   ]
  }
 ```
 
 ### Usage #2
 ```
 $ python3 jsonify.py student.csv myStudents
```

 ```
 $ {
   "myStudents":[
      {
         "student":"Nitesh",
         "age":"12"
      },
      {
         "student":"Ikram",
         "age":"9"
      },
      {
         "student":"Raman",
         "age":"15"
      },
      {
         "student":"Sunny",
         "age":"11"
      }
   ]
  }
 ```

