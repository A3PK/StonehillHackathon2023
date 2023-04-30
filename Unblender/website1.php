<!DOCTYPE html>
<html>
<head>

    <title>HealthTest</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: teal;
           
        }
       
        form {
                   
            max-width: 500px;
            margin: 0 auto;
            background-color: #FF7F50;
            padding: 15px;
            border-radius: 50px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
        }
       
        h2 {
            text-align: center;
            color: white;
            margin-top: 5;
        }
       
        input[type=text], input[type=email], input[type=password], textarea, select {
   
            width: 100%;
            padding: 12px 20px;
            margin: 25px 0;
            display: inline-block;
            border: 1px solid #ccc;
            border-radius: 50px;
            box-sizing: border-box;
        }
       
        input[type=submit] {
            background-color: teal;
            color: white;
            padding: 12px 20px;
            margin: 10px 0;
            border: none;
            border-radius:50px;
            cursor: pointer;
            width: 101%;
           
        }
       
        input[type=submit]:hover {
            background-color: grey;
        }
       
        .container {
            background-color: white;
            padding: 16px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
        }
       
        @media screen and (max-width: 600px) {
            form {
                max-width: 100%;
            }
        }
    </style>
</head>
<body>
    <form>
        <h2>Health Test</h2>
       
        <div class="container">
            <label for="name"><b>Name</b></label>
            <input type="text" placeholder="Enter Name" name="name" required>
       
            <label for="email"><b>Email</b></label>
            <input type="email" placeholder="Enter Email" name="email"
           
                   
            <label for="age"><b>Age</b></label>
            <input type="text" placeholder="Enter Age" name="age" required>
           
            <label for="message"><b>How much would you grade your eyesight out of 10</b></label>
            <select>
  <option value="option1">1</option>
  <option value="option2">2</option>
  <option value="option3">3</option>
  <option value="option3">4</option>
  <option value="option3">5</option>
  <option value="option3">6</option>
  <option value="option3">7</option>
  <option value="option3">8</option>
  <option value="option3">9</option>
  <option value="option3">10</option>
 

            <select>
           

  <label for="message"><b>Are you able to speak properly
     

<input type="radio" id="yes" name="options" value="Yes">
<label for="yes">Yes </label>

<input type="radio" id="no" name="no" value="No">
<label for="no">No</label>
</select>
           
   
       
          <button onclick="location.href='http://localhost/website.php';" target="_blank">Submit </button>

        </div>
    </form>
</body>
</html>