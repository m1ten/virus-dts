import { SlashCommandBuilder } from "@discordjs/builders";
import { Permissions } from "discord.js";

export const data = new SlashCommandBuilder()
	.setName("prune")
	.setDescription("Prune chat!")
	.addIntegerOption((option) =>
		option.setName("amount").setDescription("Number of messages to prune").setRequired(true)
	)
	.addBooleanOption((option) =>
		option.setName("ephemeral").setDescription("Show or hide message"));

export async function execute(interaction: any) {
	if (interaction.member.permissions.has(Permissions.FLAGS.MANAGE_MESSAGES)) {
		let amount: number = interaction.options.getInteger("amount");
		const ephemeral = interaction.options.getBoolean("ephemeral");

		if (amount < 1) {
			amount = 1;
		} else if (amount > 100) {
			amount = 100;
		}

		await interaction.channel.bulkDelete(amount, true);

		return interaction.reply({ content: `Successfully pruned \`${amount}\` messages.`, ephemeral: ephemeral });
	}
}