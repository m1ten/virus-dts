import { Client, Intents, Collection } from "discord.js";
import { readdirSync } from "fs";
// import { config } from "dotenv";
// config();

// import { deploy } from "./deploy";
// deploy();

const client = new Client({
  intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES],
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
client.commands = new Collection();
const commandFiles = readdirSync(__dirname + "/commands").filter((file) => file.endsWith(".ts"));

for (const file of commandFiles) {
  const command = require(`./commands/${file}`);

  // @ts-ignore
  client.commands.set(command.data.name, command);
}

const eventFiles = readdirSync(__dirname + "/events").filter((file) => file.endsWith(".ts"));

for (const file of eventFiles) {
  const event = require(`./events/${file}`);
  if (event.once) {
    client.once(event.name, (...args) => event.execute(...args));
  } else {
    client.on(event.name, (...args) => event.execute(...args, client));
  }
}

console.error("Not Token = " + process.env["TOKEN"]);

// client.login(process.env["TOKEN"]);
