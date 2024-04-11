const express = require("express");
const PythonShell = require("python-shell").PythonShell
const fileUpload = require('express-fileupload');
const cors = require('cors'); 
const path = require('path')

const app = express();
app.use(fileUpload());
app.use(express.static("public"));
app.use(express.json());
app.use(cors());

app.post('/upload', (req, res) => {
    const { image } = req.files;

    if (!image) return res.sendStatus(400);

    image.mv(__dirname + '/ImageProcessing/TestImages/' + image.name);

    res.sendStatus(200);
});

app.get("/:id", (req, res) => {
  const id = req.params.id;
  let path =`E:/mini_project/Underwater-image-processing/Backend/ImageProcessing/TestImages/${id}`
  
  let pyshell = new PythonShell(scriptPath='ImageProcessing/main.py');

  pyshell.send(path);
  
  pyshell.on("message", function (message) {
    console.log(message);
  });

  pyshell.end(function (err, code, signal) {
    if (err) throw err;
    res.status(200).json({
      message: "Image processed successfully",
      path: `../../Backend/ImageProcessing/OutputImages/processed_image.png`,
    });
    console.log("finished");
  });
});

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});
