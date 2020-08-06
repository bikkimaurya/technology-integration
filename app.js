const express= require("express");
const python = require("python-shell").PythonShell
const app = express();
const port= process.env.PORT || 8080
const body = require("body-parser")
app.use(body.urlencoded({extended:true}));
app.set("view engine","ejs");
app.use(express.static("public"));




app.get("/",function(req,res){
    res.render("home")
})

app.post("/predict",function(req,res){
    options={
        args:[req.body.Pregnancies,req.body.Glucose,req.body.BloodPressure,req.body.SkinThickness,req.body.Insulin,req.body.BMI,req.body.DiabetesPedigreeFunction,req.body.Age]}

    python.run("script.py", options, function (err, data) {
        if (err) {
            console.log(err)
            res.send("please try after some time");
        }
        else{
            console.log(data.toString())
            res.send(data.toString())
        }

    });
})

app.listen(port , function () {
    console.log("Sever is listening on port no :"+ port);
  })