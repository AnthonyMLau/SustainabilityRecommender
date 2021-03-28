// var http = require('http');

// //create a server object:
// http.createServer(function (req, res) {
//     res.write('Hello World!'); //write a response to the client
//     res.end(); //end the response
//   }).listen(8080); //the server object listens on port 8080

const express = require('express')
var bodyParser = require('body-parser')
const app = express()
const port = 3000
var jsonParser = bodyParser.json()
var urlencodedParser = bodyParser.urlencoded({ extended: false })
app.use(express.json({limit: '50mb'}));
app.use(express.urlencoded({limit: '50mb'}));




app.post('/picture', urlencodedParser, function (req, res) {
    // console.log(req.body.username)
    
    
    var base64Data = req.body.username.replace(/^data:image\/png;base64,/, "");
    
    require("fs").writeFile("out.jpg", base64Data, 'base64', function(err) {
      console.log(err);
    });

    const spawn = require("child_process").spawn;
    const pythonProcess = spawn('python3',["getBarcode.py"]);
console.log("111111111")
    pythonProcess.stdout.on('data', (data) => {
      console.log("22222222")
      console.log(data.toString())
  });


    res.send('welcome, ' + req.body.username)
  })

app.get('/', (req, res) => {
  res.send('Hello World!')
})


app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})