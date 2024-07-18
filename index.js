const express = require("express");
const app = express();
const port = 8080;

app.get("/poison", (req, res) => {
    const string = req.query.string;
    const num = parseInt(req.query.num);
    res.send(poison(string, num));
});

app.listen(port, () => {
    console.log(`App poisoning on port ${port}`);
});

function poison(s, n) {
    let poisonedString = s.split("");
    let hyphenAsterisk = true;

    for (let i = n - 1; i < s.length; i += n) {
        hyphenAsterisk
            ? (poisonedString[i] = "-" + poisonedString[i].toUpperCase() + "-")
            : (poisonedString[i] = "*" + poisonedString[i] + "*");

        hyphenAsterisk = !hyphenAsterisk;
    }
    return poisonedString.join("");
}