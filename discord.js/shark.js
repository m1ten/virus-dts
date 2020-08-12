const Discord = require("discord.js"),
  client = new Discord.Client(),
  fs = require("fs"),
  readline = require("readline").createInterface({
    input: process.stdin,
    output: process.stdout,
  });

readline.question("Enter Name: ", (name) => {
  console.log(name);
  readline.close();
});

var bot = JSON.parse(fs.readFileSync("shark.json"));

client.once("ready", () => {
  console.log(`${bot.name} is online!`);
});

client.on("message", (message) => {
  if (!message.content.startsWith(bot.prefix)) return; // "message.author.bot" working on it
});

client.login(bot.token);
