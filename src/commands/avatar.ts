import { SlashCommandBuilder } from "@discordjs/builders";

export const data = new SlashCommandBuilder()
  .setName("avatar")
  .setDescription(
    "Get the avatar URL of the selected user, or your own avatar."
  )
  .addUserOption((option) =>
    option.setName("user").setDescription("The user's avatar to show")
  );

export async function execute(interaction: {
  options: { getUser: (arg0: string) => any };
  reply: (arg0: { content: string; ephemeral: boolean }) => any;
  user: { displayAvatarURL: (arg0: { dynamic: boolean }) => any };
}) {
  const user = interaction.options.getUser("user");
  if (user)
    return interaction.reply({
      content: `${user.username}'s avatar: ${user.displayAvatarURL({
        dynamic: true,
      })}`,
      ephemeral: true,
    });
  return interaction.reply({
    content: `Your avatar: ${interaction.user.displayAvatarURL({
      dynamic: true,
    })}`,
    ephemeral: true,
  });
}