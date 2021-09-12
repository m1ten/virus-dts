import { SlashCommandBuilder } from "@discordjs/builders";

export const data = new SlashCommandBuilder()
	.setName("prune")
	.setDescription("Prune chat!")
	.addIntegerOption((option) =>
		option.setName("amount").setDescription("Number of messages to prune").setRequired(true)
	)
	.addBooleanOption((option) =>
		option.setName("ephemeral").setDescription("Show or hide message"));

export async function execute(interaction: any) {
	let amount: number = interaction.options.getInteger("amount");
	const ephemeral = interaction.options.getBoolean("ephemeral");

	if (amount < 1) {
		amount = 1;
	} else if (amount > 100) {
		amount = 100;
	}

	await interaction.channel.bulkDelete(amount, true).catch((error: any) => {
		console.error(error);
		interaction.reply({ content: 'There was an error trying to prune messages in this channel!', ephemeral: ephemeral });
	});

	return interaction.reply({ content: `Successfully pruned \`${amount}\` messages.`, ephemeral: ephemeral });
}