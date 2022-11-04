
const express = require('express');

const app = express();

app.get('/',(request,response)=>{
    response.send('hel')
});

app.listen(8000,()=>{
    console.log("inging");
})