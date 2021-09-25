export const name = "interactionCreate";

export async function execute(
  interaction: {
    isCommand: () => any;
    commandName: any;
    reply: (arg0: { content: string; ephemeral: boolean }) => any;
  },
  client: { commands: { get: (arg0: any) => any } }
) {
  if (!interaction.isCommand()) return;

  const command = client.commands.get(interaction.commandName);

  if (!command) return;

  try {
    await command.execute(interaction);
  } catch (error) {

    //@ts-ignore
    if (error.code == 50013) {
      return interaction.reply({
        content:
          ":exclamation: I don't have permission to execute this command!",
        ephemeral: true,
      });
    }

    console.error(error);

    await interaction.reply({
      content:
        ":exclamation: There was an error while executing this command!",
      ephemeral: true,
    });
  }
}
