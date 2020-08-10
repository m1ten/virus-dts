const Discord = require("discord.js"),
  bot = new Discord.Client();

bot.once("ready", () => {
  console.log("Shark is online!");
});

bot.login("NzIxNDQwNTIwNDYyOTI1OTQ0.XuUj1w.tXE4_LnWrz669sfmYa78MdIJaTA");
