const express = require("express");
const fs = require("fs");
const path = require("path");
const app = express();
const PORT = process.env.PORT || 10000;

app.use(express.static("public"));
app.use(express.json());

app.post("/save", (req, res) => {
  const { input } = req.body;
  fs.appendFile("log.txt", input + "\n", (err) => {
    if (err) return res.status(500).send("Failed to save.");
    res.sendStatus(200);
  });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
