import Discord, { Intents } from "discord.js";
import dotenv from "dotenv";
dotenv.config();

const client = new Discord.Client({
	intents: [
		Intents.FLAGS.GUILDS,
		Intents.FLAGS.GUILD_MESSAGES
	]
});

client.on('ready', () => {
	console.log('Atlas is online.');
});

client.on('messageCreate', (message) => {
	if (message.content === 'ping') {
		message.reply({
			content: 'pong'
		})
	};
})

client.login(process.env.TOKEN);