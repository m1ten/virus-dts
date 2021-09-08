import { SlashCommandBuilder } from "@discordjs/builders";

export const data = new SlashCommandBuilder()
  .setName("ping")
  .setDescription("Replies Pong!");

export async function execute(interaction: {
  reply: (arg0: { content: string; ephemeral: boolean }) => any;
}) {
  return interaction.reply({ content: "Pong!", ephemeral: true });
}
