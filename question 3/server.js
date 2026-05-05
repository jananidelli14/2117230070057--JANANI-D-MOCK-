const express=require("express");
const app=express();
app.use(express.json());

//GET USERS
app.get("/users",(req,res)=>{
    res.json([{id:1,name:"Janani"}]);
})
//POST USERS
#post users code where the user can add a new users

app.listen(3000,()+>{
    console.log("Server is running");
})