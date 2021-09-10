export const name = "ready";
export const once = true;

export function execute(client: { user: { tag: any } }) {
  console.log(`${client.user.tag} is online.`);
}
