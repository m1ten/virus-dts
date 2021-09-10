import fs from "fs";
import Discord from "discord.js";
import dotenv from "dotenv";
dotenv.config();

const client = new Discord.Client({
  intents: [Discord.Intents.FLAGS.GUILDS, Discord.Intents.FLAGS.GUILD_MESSAGES],
  presence: {
    status: "online",
    activities: [
      {
        name: "Discord",
        type: "WATCHING",
      },
    ],
  },
});

// @ts-ignore
client.commands = new Discord.Collection();
const commandFiles = fs
  .readdirSync(__dirname + "/commands")
  .filter((file) => file.endsWith(".ts"));

for (const file of commandFiles) {
  const command = require(`./commands/${file}`);

  // @ts-ignore
  client.commands.set(command.data.name, command);
}

const eventFiles = fs
  .readdirSync(__dirname + "/events")
  .filter((file) => file.endsWith(".ts"));

for (const file of eventFiles) {
  const event = require(`./events/${file}`);
  if (event.once) {
    client.once(event.name, (...args) => event.execute(...args));
  } else {
    client.on(event.name, (...args) => event.execute(...args, client));
  }
}

client.login(process.env.TOKEN);
